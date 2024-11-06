from PyQt6.QtCore import QObject, pyqtSignal, QEvent
from PyQt6.QtGui import QWheelEvent, QMouseEvent, QKeyEvent, QHoverEvent


class ResizeEventDeliverer(QObject):
	resized = pyqtSignal(int, int)

	def __init__(self):
		super().__init__()

	def eventFilter(self, obj: QObject, event: QEvent) -> bool:
		if event.type() == QEvent.Type.Resize:
			self.resized.emit(obj.width(), obj.height())

		return False


class MouseEventDeliverer(QObject):
	resized = pyqtSignal(int, int)
	mouse_pressed = pyqtSignal(QObject, QMouseEvent)
	mouse_released = pyqtSignal(QObject, QMouseEvent)
	mouse_moved = pyqtSignal(QObject, QMouseEvent)
	mouse_scrolled = pyqtSignal(QObject, QWheelEvent)
	mouse_hover_moved = pyqtSignal(QObject, QHoverEvent)

	def __init__(self):
		super().__init__()

	def eventFilter(self, obj: QObject, event: QEvent) -> bool:
		if event.type() == QEvent.Type.Resize:
			self.resized.emit(obj.width(), obj.height())
		elif event.type() == QEvent.Type.MouseButtonPress:
			self.mouse_pressed.emit(obj, event)
		elif event.type() == QEvent.Type.MouseButtonRelease:
			self.mouse_released.emit(obj, event)
		elif event.type() == QEvent.Type.MouseMove:
			self.mouse_moved.emit(obj, event)
		elif event.type() == QEvent.Type.Wheel:
			self.mouse_scrolled.emit(obj, event)
		elif event.type() == QEvent.Type.HoverMove:
			self.mouse_moved.emit(obj, event)
		
		return super().eventFilter(obj, event)


class KeyEventDeliverer(QObject):
	key_pressed = pyqtSignal(QObject, QKeyEvent)
	key_released = pyqtSignal(QObject, QKeyEvent)

	def __init__(self):
		super().__init__()

	def eventFilter(self, obj: QObject, event: QEvent) -> bool:
		if event.type() == QEvent.Type.KeyPress:
			self.key_pressed.emit(obj, event)
		elif event.type() == QEvent.Type.KeyRelease:
			self.key_released.emit(obj, event)

		return super().eventFilter(obj, event)