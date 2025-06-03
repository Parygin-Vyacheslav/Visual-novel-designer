import controllers.novel_controller as nc
from utils.singleton import singleton

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QVBoxLayout, QButtonGroup, QGridLayout
from PyQt6.QtWidgets import QFileDialog, QLabel, QPushButton, QRadioButton

# @singleton
class View(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/welcome.ui', self)
        self.initUI()

    def initUI(self):
        self.show_novels_list()
        self.createProject.clicked.connect(self.click_create_project)
        self.deleteProject.clicked.connect(self.click_delete_project)

    # Отображение списка всех новелл
    def show_novels_list(self):
        novels = nc.get_novels_list()
        self.button_group = QButtonGroup()
        
        for col, novel in enumerate(novels):
        #for col in range(5):
            coverLbl = QLabel()
            coverLbl.setFixedSize(200, 200)
            coverLbl.setPixmap(novel.cover)
            
            nameLbl = QLabel()
            nameLbl.setFixedSize(200, 40)
            nameLbl.setText(f'{novel.name}')
            
            vBox = QVBoxLayout()
            vBox.setContentsMargins(8, 8, 8, 8)
            vBox.addWidget(coverLbl)
            vBox.addWidget(nameLbl)

            button = QPushButton()
            button.setProperty('class', 'novel-button')
            button.setFixedSize(216, 264)
            button.setCheckable(True)
            button.setAutoExclusive(True)
            button.setLayout(vBox)
            self.button_group.addButton(button)
            
            self.projectsGrd.addWidget(QLabel(), col//5, col)
            self.projectsGrd.addWidget(button, col//5, col)        
    
    # Создание новой новеллы
    def click_create_project(self):
        file_name = QFileDialog.getOpenFileName(
        self,
        'Select to image',
        '',
        '(*.jpg);;(*.png)'
        )
        nc.create_novel(file_name)
        self.show_novels_list()

    def click_delete_project(self):
        btn = self.button_group.checkedButton()
        childn = btn.children()
        select_novel = childn[2].text()
        print(select_novel)
        nc.delete_novel(select_novel)