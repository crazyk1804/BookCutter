from abc import ABC, abstractmethod
from typing import List, Tuple
from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QImage, QPainter
from PyQt6.QtGui import QPen, QColor, QBrush, QFont, QFontMetrics, QPolygonF
import cv2
import numpy as np


PEN_DEFAULT_OUTLINE = QPen(Qt.GlobalColor.white, 2)
PEN_DEFAULT_TEXT = QPen(QColor(179, 39, 18), 2)
BRUSH_DEFAULT_ANN = QBrush(QColor(255, 255, 255, 50))


class FrameDecorator(ABC):
    @abstractmethod
    def decorate(self, image: QImage, meta: dict, scale=1.0):
        pass
    
    def draw_text(self, image: QImage, text: str, pos: Tuple[int, int], size=20, bold=True, background_color=None, padding=3):
        painter = QPainter(image)
        text_font = QFont()
        text_font.setBold(bold)
        text_font.setPixelSize(size)
        font_metrics = QFontMetrics(text_font)
        text_width = font_metrics.horizontalAdvance(text)
        text_height = font_metrics.height()
        point_text = QPointF(pos[0], pos[1])
        
        if background_color:
            background_pen = QPen(background_color)
            brush = QBrush(background_color)
            painter.setPen(background_pen)
            painter.setBrush(brush)
            # point_text = QPointF(padding, text_height)
            painter.drawRect(
                int(point_text.x() - padding),
                int(point_text.y() - text_height),
                text_width + padding * 2,
                text_height + padding * 2,
            )
        
        painter.setFont(text_font)
        painter.setPen(PEN_DEFAULT_TEXT)
        painter.drawText(point_text, text)
        painter.end()
        
    def draw_box(self, image: QImage, box: Tuple[int, int, int, int], color=Qt.GlobalColor.white, fill_color=QColor(255, 255, 255, 50), scale=1.0):
        box = np.array(box)
        x1, y1, x2, y2 = (box * scale).astype(int)
        
        painter = QPainter(image)
        if color is not None:
            painter.setPen(QPen(color, 2))
        painter.setBrush(QBrush(fill_color))
        painter.drawRect(x1, y1, x2-x1, y2-y1)
        painter.end()
        
    def draw_polygon(self, image: QImage, coords: List[List[float]], color: QColor, scale=1.0):
        polygon = QPolygonF()
        for coord in coords:
            polygon.append(QPointF(coord[0]*scale, coord[1]*scale))
            # polygon.append(QPointF(coord[0] , coord[1]))
        painter = QPainter(image)
        painter.setPen(QPen(color, 2))
        painter.drawPolygon(polygon)
        painter.end()