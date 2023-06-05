import atexit
import json
import os.path
import shutil
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import TYPE_CHECKING, NamedTuple, overload
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if TYPE_CHECKING:
    from concurrent.futures import Future
    from http.client import HTTPResponse
    from typing import Any, NewType

    APIResponse = NewType('APIResponse', dict[str, Any])


class Image(NamedTuple):
    user: str
    posted_on: str
    img_src: str
    thumb_file_path: str


class ImagePostInfo(NamedTuple):
    user: str
    timestamp: int
    img_url_list: list[str]


# TODO: filter


class ImageResourceHandler:
    def __init__(self, topic_id: str) -> 'None':
        if not topic_id.isdigit():
            raise ValueError('Invalid topic id!')
        self._topic_id: 'str' = topic_id
        self._offset: str = ''
        self._has_more: bool = True
        self._image_list: 'list[Image]' = []
        self._tp_executor: 'ThreadPoolExecutor' = ThreadPoolExecutor(32)
        self._temp_location: str = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, self._temp_location)

    def __del__(self) -> 'None':
        self._tp_executor.shutdown(cancel_futures=True)

    def __len__(self) -> 'int':
        return len(self._image_list)

    @overload
    def __getitem__(self, index: 'int') -> 'Image':
        ...

    @overload
    def __getitem__(self, index: 'slice') -> 'list[Image]':
        ...

    def __getitem__(self, index: 'int | slice') -> 'Image | list[Image]':
        return self._image_list[index]

    @property
    def has_more(self) -> 'bool':
        return self._has_more

    def fetch_data(self):
        if not self._has_more:
            raise Exception('No more image.')

        future_to_image: 'dict[Future[None], Image]' = {}
        for post_info in self._parse(self._request_json()):
            for img_url in post_info.img_url_list:
                file_path: 'str' = os.path.join(self._temp_location, 'thmb_' + img_url[img_url.rfind('/') + 1:])
                future_to_image[self._tp_executor.submit(self._dowload_image, img_url + '@176w_132h', file_path)] = Image(
                    post_info.user,
                    datetime.strftime(datetime.fromtimestamp(post_info.timestamp), r'%Y-%m-%d %H:%M:%S'),
                    img_url,
                    file_path
                )

        for future in as_completed(future_to_image.keys()):
            try:
                future.result()
            except HTTPError as http_error:
                # eg. 404 Not Found
                # https://www.bilibili.com/opus/738026813574348833
                print('-' * 50)
                print(str(http_error))
                print(future_to_image[future])
                print('-' * 50)
            else:
                self._image_list.append(future_to_image[future])

    def _parse(self, data: 'APIResponse') -> 'list[ImagePostInfo]':
        if (error_code := data['code']) != 0:
            raise Exception(f'Error code: {error_code}')

        self._offset = data['data']['topic_card_list']['offset']
        self._has_more = data['data']['topic_card_list']['has_more']

        img_post_info_list: 'list[ImagePostInfo]' = []

        for card in data['data']['topic_card_list']['items']:
            # check the type of a post
            if card['dynamic_card_item']['type'] != 'DYNAMIC_TYPE_DRAW':
                continue
            if card['dynamic_card_item']['modules']['module_dynamic']['major']['type'] != 'MAJOR_TYPE_DRAW':
                continue

            img_url_list: 'list[str]' = []
            for img_info in card['dynamic_card_item']['modules']['module_dynamic']['major']['draw']['items']:
                img_url_list.append(img_info['src'])

            img_post_info_list.append(
                ImagePostInfo(
                    card['dynamic_card_item']['modules']['module_author']['name'],  # user
                    card['dynamic_card_item']['modules']['module_author']['pub_ts'],  # timestamp
                    img_url_list  # img_url_list
                )
            )

        return img_post_info_list

    def _request_json(self) -> 'APIResponse':
        response: 'HTTPResponse' = urlopen(Request(
            url='https://app.bilibili.com/x/topic/web/details/cards?' + urlencode({
                    'topic_id': self._topic_id,
                    'offset': self._offset,
                    'sort_by': 0,
                    'page_size': 20
                }),
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'},
            method='GET'
        ))
        data: 'APIResponse' = json.loads(response.read())
        response.close()
        return data

    def _dowload_image(self, img_url: 'str', file_name_with_dir: 'str') -> 'None':
        response: 'HTTPResponse' = urlopen(img_url)
        with open(file_name_with_dir, 'wb') as img_file:
            img_file.write(response.read())
        response.close()


if __name__ == '__main__':
    import time
    from pprint import pprint

    img_handler: 'ImageResourceHandler' = ImageResourceHandler('9064')

    # breakpoint()

    print(len(img_handler))

    start_time: float = time.monotonic()
    img_handler.fetch_data()
    img_handler.fetch_data()
    img_handler.fetch_data()
    img_handler.fetch_data()
    img_handler.fetch_data()
    img_handler.fetch_data()
    img_handler.fetch_data()
    end_time: float = time.monotonic()
    print('网络链接总耗时：', round(end_time - start_time, 2), 's')
    print('网络链接平均耗时：', round((end_time - start_time) / 7, 2), 's')

    print(len(img_handler))
    print(img_handler.has_more)

    for i in range(len(img_handler)):
        pprint(img_handler[i])
