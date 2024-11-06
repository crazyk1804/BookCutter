import zipfile

import cv2
import numpy as np


class Book:
    def __init__(self, path_book: str):
        self.path_book = path_book
        self.book_files = []
        self.book = self.open_book()
        
    def open_book(self):
        # listup all files in the zip file
        with zipfile.ZipFile(self.path_book) as book:
            self.book_files = book.namelist()
            
    def get_page(self, page_num: int):
        # get the page content
        with zipfile.ZipFile(self.path_book) as book:
            with book.open(self.book_files[page_num]) as page:
                b_page = page.read()
                img_page = cv2.imdecode(np.frombuffer(b_page, np.uint8), cv2.IMREAD_COLOR)
                return img_page
        
    def get_page_name(self, page_num: int):
        return self.book_files[page_num]
        
    def get_page_count(self):
        return len(self.book_files)
    
    def get_meta(self):
        return {
            'path_book': self.path_book,
            'total_page': len(self.book_files),
        }