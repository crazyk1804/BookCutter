import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal, QPoint, Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QImage, QPixmap, QMouseEvent

from book_cutter_app.gui.components.event import MouseEventDeliverer
from book_cutter_app.gui.components.frame_decorator import FrameDecorator
from book_cutter_app.model.shapes import Rect

class Canvas(QObject):
    def __init__(self, lbl: QLabel):
        super().__init__()
        self.lbl = lbl
        self.img_original: np.ndarray = None
        self.img: QImage = None
        self.decorator = CanvasDecorator()
        
        self.scale = 1.0
        self.pin_point: QPoint = None
        self.rect: Rect = None
        
        self.mouse_event = MouseEventDeliverer()
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
        # pixmap = QPixmap.fromImage(self.img.scaled(w, h))
        pixmap = QPixmap.fromImage(self.img)
        pixmap = pixmap.scaled(
            self.lbl.size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )
        
        self.lbl.setPixmap(pixmap)
        self.scale = scale
        
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
    def on_mouse_pressed(self, src: QObject, event: QMouseEvent):
        self.pin_point = event.pos()
        
    def on_mouse_released(self, src: QObject, event: QMouseEvent):
        self.pin_point = None
        
    def on_mouse_moved(self, src: QObject, event: QMouseEvent):
        if self.pin_point is None:
            return
        
        if self.rect is None:
            self.rect = Rect(
                self.pin_point.x(), self.pin_point.y(),
                0, 0
            )
            
        delta = event.pos() - self.pin_point
        self.rect.w = delta.x()
        self.rect.h = delta.y()
        # TODO: draw rect 여기서가 아니라 setPixmap 하기 전에 해야함
        self.decorator.decorate(self.img, {'rect': self.rect.to_tuple()})
        self.lbl.update()
        
        
    def bind_event(self):
        self.lbl.installEventFilter(self.mouse_event)
        self.mouse_event.resized.connect(self.__fit_img)
        self.mouse_event.mouse_pressed.connect(self.on_mouse_pressed)
        self.mouse_event.mouse_released.connect(self.on_mouse_released)
        self.mouse_event.mouse_moved.connect(self.on_mouse_moved)


class CanvasDecorator(FrameDecorator):
    def __init__(self):
        super().__init__()
        
    def decorate(self, image: QImage, meta: dict, scale=1.0):
        if 'rect' in meta:
            self.draw_box(image, meta['rect'], color=Qt.GlobalColor.red, scale=scale)