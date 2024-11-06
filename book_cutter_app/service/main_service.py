import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal

from book_cutter_app.model.book import Book


class Service(QObject):
    book_opened = pyqtSignal(Book)
    
    def __init__(self):
        super().__init__()
        self.book = None
        self.cutter = None
        self.path_workshop = 'workshop'
        
    def set_path_book(self, path_book):
        self.book = Book(path_book)
        self.book_opened.emit(self.book)
    
        