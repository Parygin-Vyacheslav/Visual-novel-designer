from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDialog
from PyQt6.QtWidgets import QButtonGroup, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton
#from PyQt6.QtCore import pyqtSignal
from utility.observer import Observer
from utility.meta import ViewMeta
from view import welcome, device_select

class WelcomeView(QMainWindow, Observer, metaclass=ViewMeta):
    def __init__(self, controller, model, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.controller = controller #
        self.novel_list_model = model #

        self.ui = welcome.Ui_MainWindow()
        self.ui.setupUi(self)

        self.novel_list_model.add_observer(self) # 

        self.ui.createProject.clicked.connect(self.select_device) #
        #self.ui.editProject.clicked.connect()
        #self.ui.playProject.clicked.connect()
        self.ui.deleteProject.clicked.connect(self.delete_project) #

        self.update() #

    def update(self):
        self.show_novels_list() #

    # Отображение списка всех новелл
    def show_novels_list(self):
        # Очистка контейнера от кнопок с новеллами
        grid_rows = self.ui.projectsGrd.rowCount() #
        grid_cols = self.ui.projectsGrd.columnCount() #
        print(f'rows = {grid_rows}, cols = {grid_cols}')
        if (grid_rows != 1 or grid_cols != 1): #
            for row in range(grid_rows):
                for col in range(grid_cols):
                    widget = self.ui.projectsGrd.itemAtPosition(row, col).widget() #
                    print(f'Out row{row}; col{col} delete {widget}')
                    widget.deleteLater() #
        
        # Заполнение контейнера кнопками с новеллами
        novels = self.novel_list_model.select_all() #
        self.ui.button_group = QButtonGroup()
        #print('Group created')
        self.ui.button_group.buttonToggled.connect(self.button_status_changed) #
        #print('Group connect to command')
        
        rows = len(novels) // 5 + 1
        for row in range(rows):
            col = 0
            for novel in novels:
                coverLbl = QLabel()
                coverLbl.setFixedSize(200, 200)
                coverLbl.setPixmap(novel.cover)
                
                nameLbl = QLabel()
                nameLbl.setFixedSize(200, 40)
                nameLbl.setText(novel.name)
                
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
                self.ui.button_group.addButton(button)
                
                #self.ui.projectsGrd.addWidget(QLabel(), row, col)
                self.ui.projectsGrd.addWidget(button, row, col) #
                print(f'In row{row}; col{col} create QButton')
                col += 1
            while col < 5: #
                self.ui.projectsGrd.addWidget(QLabel(), row, col)
                print(f'In row{row}; col{col} create QLabel')
                col += 1
        #print('Group filled')

    def select_device(self):
        self.device_select = device_select.Ui_Form()
        self.device_select_form = QDialog()
        self.device_select.setupUi(self.device_select_form)
        self.device_select.device_buttons = QButtonGroup()
        self.device_select.device_buttons.addButton(self.device_select.desktop_btn)
        self.device_select.device_buttons.addButton(self.device_select.phone_btn)
        self.device_select.device_buttons.buttonToggled.connect(self.device_button_toggled)
        self.device_select.cancel_btn.clicked.connect(self.device_select_form.reject)
        self.device_select.create_project_btn.clicked.connect(self.create_project)
        self.device_select_form.exec()

    def device_button_toggled(self):
        if self.device_select.device_buttons.checkedButton:
            self.device_select.create_project_btn.setEnabled(True)
        else:
            self.device_select.create_project_btn.setEnabled(False)

    def create_project(self):
        self.device_select_form.accept()
        selected_device = self.device_select.device_buttons.checkedId()
        self.controller.create_novel(960, 640) if selected_device == -2 else self.controller.create_novel(917, 412)

    def delete_project(self):
        project_name = self.ui.button_group.checkedButton().children()[2].text() # [0] - VBox, [1] - Label (cover), [2] - Label (name)
        delete_confirmation = QMessageBox.question(
            self, 
            'Подтверждение удаления проекта', # Название окна
            f'Вы действительно хотите навсегда удалить проект {project_name}?', # Текст в окне
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) # Кнопки
        if delete_confirmation == QMessageBox.StandardButton.Yes: # Если нажата кнопка "Yes"
            self.controller.delete_novel(project_name) # Удалить новеллу
    
    def button_status_changed(self):
        if self.ui.button_group.checkedButton() == None:
            print('Button NOT selected')
            self.ui.deleteProject.setEnabled(False)
            self.ui.playProject.setEnabled(False)
            self.ui.editProject.setEnabled(False)
        else:
            print('Button selected')
            self.ui.deleteProject.setEnabled(True)
            #self.ui.playProject.setEnabled(True)
            self.ui.editProject.setEnabled(True)
        print('Button states is changed')
    


    def save_project(self):
        file_name = QFileDialog.getOpenFileName(
        self,
        'Выберите обложку для новеллы', # Название окна
        '', # Название файла
        'JPEG(*.jpg; *.jpeg);;PNG(*.png)' # тип файла
        )