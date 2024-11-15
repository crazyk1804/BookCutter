import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal, QThread

from book_cutter_app.model.book import Book


class Service(QObject):
    book_opened = pyqtSignal(Book)
    
    def __init__(self):
        super().__init__()
        self.book = None
        self.cutter = None
        self.path_workshop = 'workshop'
        self.task = None
        
    def load_book(self, path_book):
        self.book = Book(path_book)
        self.book_opened.emit(self.book)
        
    def set_path_book(self, path_book):
        self.task = QThread()
        self.task.run = lambda: self.load_book(path_book)
        self.task.finished.connect(self.task_finished)
        
        self.task.start()

    def task_finished(self):
        self.task.deleteLater()
        self.task = None
        