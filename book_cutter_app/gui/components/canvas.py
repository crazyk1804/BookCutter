import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QImage, QPixmap

from book_cutter_app.gui.components.event import MouseEventDeliverer

class Canvas(QObject):
    def __init__(self, lbl: QLabel):
        super().__init__()
        self.lbl = lbl
        self.mouse_event = MouseEventDeliverer()
        self.img_original: np.ndarray = None
        self.img: QImage = None
        
        self.bind_event()
        
    def set_img(self, img: np.ndarray):
        self.img_original = img
        self.img = QImage(
            img.data, img.shape[1], img.shape[0], img.strides[0],
            QImage.Format.Format_RGB888
        )
        self.__fit_img()
        
    def __scale_img(self, scale):
        if self.img is None:
            return
        
        h, w, _ = self.img_original.shape
        h = int(h * scale)
        w = int(w * scale)
        pixmap = QPixmap.fromImage(self.img.scaled(w, h))
        self.lbl.setPixmap(pixmap)
        
    def __fit_img(self):
        if self.img is None:
            return
        
        h, w, _ = self.img_original.shape
        h_lbl, w_lbl = self.lbl.height(), self.lbl.width()
        scale = min(h_lbl / h, w_lbl / w)
        self.__scale_img(scale)
        
    # ========================================
    # Event Handler
    # ========================================
    def bind_event(self):
        self.lbl.installEventFilter(self.mouse_event)
        self.mouse_event.resized.connect(self.__fit_img)