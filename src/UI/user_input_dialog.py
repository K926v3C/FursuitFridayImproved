from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

if __name__ == '__main__':
    from skeleton_forms import skeleton_InputDialog
else:
    from .skeleton_forms import skeleton_InputDialog

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class InputDialog(QDialog):
    def __init__(self, parent: 'QWidget | None') -> 'None':
        super(InputDialog, self).__init__(parent)
        self.wc = skeleton_InputDialog()
        self.wc.setupUi(self)  # type: ignore
        self.setFixedSize(self.width(), self.height())
        self._temp_str: 'None | str' = None
        self.wc.dialogButtonBox.accepted.connect(self.read_user_input)

    @Slot()
    def read_user_input(self) -> 'None':
        self._temp_str = self.wc.lineEdit.text()

    def get_user_input(self, title: 'str', desc: 'str') -> 'None | str':
        self.setWindowTitle(title)
        self.wc.label.setText(desc)
        if self._temp_str is None:
            self.wc.lineEdit.clear()
        self._temp_str = None
        self.exec()
        return self._temp_str
