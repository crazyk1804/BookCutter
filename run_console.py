import cv2
import os
from tqdm import tqdm

from book_cutter_app.model.book import Book

class Cutter:
    def __init__(self, book, path_workshop='workshop'):
        self.book = book
        self.cut_from_top = 0
        self.cut_from_bottom = 0
        self.cut_from_left = 0
        self.cut_from_right = 0
        self.odd_offset = (0, 0)
        self.path_workshop = path_workshop
        
    def set_cut_offset(self, top, bottom, left, right):
        self.cut_from_top = top
        self.cut_from_bottom = bottom
        self.cut_from_left = left
        self.cut_from_right = right
        
    def cut(self, img_page, odd=False):
        img = img_page.copy()
        stx = self.cut_from_left
        sty = self.cut_from_top
        edx = img.shape[1] - self.cut_from_right
        edy = img.shape[0] - self.cut_from_bottom
        if odd:
            stx += self.odd_offset[0]
            sty += self.odd_offset[1]
            edx += self.odd_offset[0]
            edy += self.odd_offset[1]
            
        img_cut = img[sty:edy, stx:edx]
        
        return img_cut
    
    def do_work(self):
        os.makedirs(self.path_workshop, exist_ok=True)
        
        total_page = self.book.get_page_count()
        print('total page:', total_page)
        for i in tqdm(range(total_page), desc='cutting pages', total=total_page):
            img_page = self.book.get_page(i)
            page_name = self.book.get_page_name(i)
            
            img_cut = self.cut(img_page, i % 2 != 0)
            img_cut_name = page_name.split('/')[-1]
            path_img_cut = os.path.join(self.path_workshop, img_cut_name)
            
            name, ext = os.path.splitext(img_cut_name)
            ext = ext.lower()
            if ext in ['.jpg', '.jpeg']:
                cv2.imwrite(path_img_cut, img_cut, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            else:
                cv2.imwrite(path_img_cut, img_cut)


if __name__ == '__main__':
    # book = Book('c:/books/딥러닝을위한수학.zip')
    book = Book('n:/개인/books/프로그래밍/러닝깃허브액션.zip')
    cutter = Cutter(book)
    cutter.odd_offset = (80, 0)
    cutter.set_cut_offset(top=100, bottom=100, left=90, right=170)
    cutter.do_work()
    