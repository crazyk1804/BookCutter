from book_cutter_app.gui.components.canvas import Canvas
from book_cutter_app.gui.ui.ui_main_window import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QMovie

from book_cutter_app.model.book import Book
from book_cutter_app.service.main_service import Service


class WIN_MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        
        self.service = Service()
        self.canvas = Canvas(self.lbl_canvas)
        self.book: Book = None
        
        self.bind_event()

    def init_ui(self):
        self.setWindowTitle('Book Cutter')
        # self.setWindowIcon(QIcon(':/icon/book_cutter.png'))

        # self.actionOpen.triggered.connect(self.open_file)
        # self.actionExit.triggered.connect(self.close)
    
    def show_loading(self):
        movie = QMovie(r'book_cutter_app/assets/loading.gif')
        self.lbl_canvas.setMovie(movie)
        movie.start()
    
    def show_page(self, page_num: int):
        img_page = self.book.get_page(page_num)
        self.canvas.set_img(img_page)
        
    # ========================================
    # Event Handler
    # ========================================
    def find_book(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Find Book',
            '',
            'ZIP Files (*.zip);;PDF Files (*.pdf);;All Files (*)'
        )
        if file_name:
            self.tbox_path_book.setText(file_name)
            self.show_loading()
            self.service.set_path_book(file_name)
            
    def on_book_opened(self, book: Book):
        self.book = book
        self.bar_progress.setMaximum(self.book.get_page_count())
        self.bar_progress.setValue(0)
        self.slide_page.setMaximum(self.book.get_page_count() - 1)
        self.slide_page.setValue(0)
        self.show_page(0)
    
    def bind_event(self):
        self.btn_find_book.clicked.connect(self.find_book)
        self.service.book_opened.connect(self.on_book_opened)
        self.slide_page.valueChanged.connect(self.show_page)
        self.btn_prev_page.clicked.connect(lambda: self.slide_page.setValue(self.slide_page.value() - 1))
        self.btn_next_page.clicked.connect(lambda: self.slide_page.setValue(self.slide_page.value() + 1))
        