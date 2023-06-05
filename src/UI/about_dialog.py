from typing import TYPE_CHECKING

from PySide6.QtWidgets import QDialog

from .skeleton_forms import skeleton_AboutDialog

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class AboutDialog(QDialog):
    def __init__(self, parent: 'QWidget | None') -> 'None':
        super(AboutDialog, self).__init__(parent)
        self.wc = skeleton_AboutDialog()
        self.wc.setupUi(self)  # type: ignore
        self.setFixedSize(self.width(), self.height())
