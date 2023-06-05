import os
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING
from urllib.request import urlopen

from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox)

from core_utilities import ImageResourceHandler
from UI import AboutDialog, InputDialog
from UI.skeleton_forms import skeleton_MainForm

if TYPE_CHECKING:
    from http.client import HTTPResponse

    from PySide6.QtWidgets import QCheckBox, QLabel

    from core_utilities import Image


class MainWindow(QMainWindow):
    def __init__(self) -> 'None':
        # Set up the main form and auxiliary windows
        super(MainWindow, self).__init__()
        self.wc = skeleton_MainForm()
        self.wc.setupUi(self)  # type: ignore
        self.about_dialog = AboutDialog(self)
        self.input_dialog = InputDialog(self)
        self.message_box = QMessageBox(self)

        # Bond slots with signals
        self.wc.prev_button.clicked.connect(self.to_previous_page)
        self.wc.next_button.clicked.connect(self.to_next_page)
        self.wc.action_select_all.triggered.connect(self.select_all_images)
        self.wc.action_change_folder.triggered.connect(self.change_download_folder)
        self.wc.action_download.triggered.connect(self.download_selected_images)
        self.wc.action_about.triggered.connect(self.display_about_dialog)
        self.wc.action_change_topic.triggered.connect(self.change_topic)
        self.wc.action_filter_by_user.triggered.connect(self.developing_function)

        # Data initializaion
        self.curr_page_num: 'int' = 1
        self.download_location: 'str' = os.path.join(os.getcwd(), 'images')
        self.download_QThread: 'QThread' = QThread(self)
        self.thread_pool: 'ThreadPoolExecutor' = ThreadPoolExecutor(8)
        self.img_handler: 'ImageResourceHandler' = ImageResourceHandler('9064')
        self.handler_idx: 'int' = 0
        self.initialize_page()

    def __del__(self) -> 'None':
        self.thread_pool.shutdown()

    def initialize_page(self):
        self.download_QThread.moveToThread
        self.ensure_img_sufficient()
        self.load_images(self.img_handler[self.handler_idx:self.handler_idx + 9])
        self.wc.prev_button.setEnabled(False)
        self.wc.next_button.setEnabled(True)
        # whether it is the last page
        if not self.img_handler.has_more and not len(self.img_handler) > self.handler_idx + 9:
            self.wc.next_button.setEnabled(False)
        self.display_page_num()

    def ensure_img_sufficient(self) -> 'None':
        while len(self.img_handler) - self.handler_idx < 9:
            if self.img_handler.has_more:
                self.img_handler.fetch_data()
                # TODO: diaplay the loading dialog
            else:
                break

    def load_images(self, img_list: 'list[Image]') -> 'None':
        for i in range(9):
            label: 'QLabel' = getattr(self.wc, f'label_{i + 1}')
            check_box: 'QCheckBox' = getattr(self.wc, f'checkBox_{i + 1}')
            label.setPixmap(QPixmap(img_list[i].thumb_file_path if i < len(img_list) else ''))
            check_box.setChecked(False)
            check_box.setText(f'{img_list[i].user} - {img_list[i].posted_on}' if i < len(img_list) else '')

    def display_page_num(self) -> 'None':
        self.wc.page_indicator.setText(f'第{self.curr_page_num}页')

    @Slot()
    def to_previous_page(self) -> 'None':
        self.handler_idx -= 9
        self.load_images(self.img_handler[self.handler_idx:self.handler_idx + 9])

        self.wc.next_button.setEnabled(True)
        self.curr_page_num -= 1
        # whether it is the first page
        if self.curr_page_num == 1:
            self.wc.prev_button.setEnabled(False)
        self.display_page_num()

    @Slot()
    def to_next_page(self) -> 'None':
        self.handler_idx += 9
        self.ensure_img_sufficient()
        self.load_images(self.img_handler[self.handler_idx:self.handler_idx + 9])

        # whether it is the last page
        if not self.img_handler.has_more and not len(self.img_handler) > self.handler_idx + 9:
            self.wc.next_button.setEnabled(False)
        self.wc.prev_button.setEnabled(True)
        self.curr_page_num += 1
        self.display_page_num()

    @Slot()
    def select_all_images(self):
        for i in range(9):
            check_box: 'QCheckBox' = getattr(self.wc, f'checkBox_{i + 1}')
            check_box.setChecked(True)

    def _dowload_image(self, img_url: 'str', file_name_with_dir: 'str') -> 'None':
        response: 'HTTPResponse' = urlopen(img_url)
        with open(file_name_with_dir, 'wb') as img_file:
            img_file.write(response.read())
        response.close()

    @Slot()
    def change_download_folder(self):
        self.download_location = QFileDialog.getExistingDirectory(self, '选择下载文件夹', os.getcwd())

    @Slot()
    def download_selected_images(self):
        img_list: 'list[Image]' = []
        for i in range(9):
            check_box: 'QCheckBox' = getattr(self.wc, f'checkBox_{i + 1}')
            if check_box.isChecked():
                img_list.append(self.img_handler[self.handler_idx + i])
                check_box.setChecked(False)

        if img_list and not os.path.exists(self.download_location):
            os.mkdir(self.download_location)

        for img in img_list:
            file_path: 'str' = os.path.join(
                self.download_location,
                f'{img.user}_{img.posted_on.replace(":", "-").replace(" ", "_")}_{img.img_src[img.img_src.rfind(".") - 7:]}'
            )
            self.thread_pool.submit(self._dowload_image, img.img_src, file_path)

        self.message_box.information(self, '下载完成', f'所选图片已下载至文件夹：\n{self.download_location}')

    @Slot()
    def display_about_dialog(self):
        self.about_dialog.show()

    @Slot()
    def change_topic(self) -> 'None':
        if (topic_id := self.input_dialog.get_user_input('更改话题', '请输入话题ID：')) is None:
            return
        if not topic_id.isdigit():
            self.message_box.critical(self, '无效的话题ID', '请输入正确的话题ID！')
        else:
            self.img_handler = ImageResourceHandler(topic_id)
            self.initialize_page()

    @Slot()
    def developing_function(self):
        self.message_box.information(self, '尚在开发的功能', '该功能正在开发中……')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainWindow()
    main_form.show()
    app.exec()
