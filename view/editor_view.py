from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFrame, QLineEdit, QGraphicsView
from PyQt6.QtCore import Qt #pyqtSignal
from utility.observer import Observer
from utility.meta import ViewMeta
from view.editor import Ui_MainWindow
from PyQt6.QtGui import QPixmap, QColor, QKeyEvent

class EditorView(QMainWindow, Observer, metaclass=ViewMeta):
    def __init__(self, controller, novel, novel_model, scene_model, persona_model, replica_model, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.controller = controller #
        self.novel = novel
        self.novel_model = novel_model #
        self.scene_model = scene_model
        self.persona_model = persona_model
        self.replica_model = replica_model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.parent().setWindowTitle(novel.name)

        self.ui.to_welcome_btn.clicked.connect(self.to_welcome)

        self.space_scene = QGraphicsScene()

        self.scene_frame = QFrame()

        self.scene_background = QLabel(self.scene_frame)
        self.scene_background.setPixmap(scene_model.scenes[0].background)

        self.hbox_w = QWidget(self.scene_frame)
        self.hbox = QHBoxLayout(self.hbox_w)
        self.left_persona = QLabel('Left Persona')
        self.center_persona = QLabel('Center Persona')
        self.right_persona = QLabel('Right Persona')
        self.hbox.addWidget(self.left_persona)
        self.hbox.addWidget(self.center_persona)
        self.hbox.addWidget(self.right_persona)

        self.vbox_w = QWidget(self.scene_frame)
        self.vbox = QVBoxLayout(self.vbox_w)
        self.vspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.replica_lbl = QLabel('Here is replica of Persona.')
        self.vbox.addItem(self.vspacer)
        self.vbox.addWidget(self.replica_lbl)
        
        self.space_scene.addWidget(self.scene_frame)
        self.ui.space.setScene(self.space_scene)

        self.scale_count = -3
        self.scale = 0.7
        self.ui.scale_cmb.addItem(f'{int(self.scale * 100)}%')
        self.ui.scale_cmb.addItems(['190%', '150%', '100%', '50%', '10%'])
        self.ui.scale_cmb.currentIndexChanged.connect(self.zoom_button_current)
        self.ui.space.scale(self.scale, self.scale)
        self.ui.space.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.ui.space.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.ui.space.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        #print(f'Interactive is {self.ui.space.isInteractive()}')
        self.ui.space.wheelEvent = self.zoom_with_wheel

        self.update() #
        
    def keyPressEvent(self, event):
        if event.modifiers() == (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.NoModifier):
            #self.ui.scale_cmb.setCurrentIndex(0)
            if event.key() == Qt.Key.Key_Equal:
                self.zoom(True)
            elif event.key() == Qt.Key.Key_Minus:
                self.zoom(False)
        if event.modifiers() == (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.NoModifier):
            if event.key() == Qt.Key.Key_S:
                self.controller.save_project()
                print('Project is saved')

    def zoom_with_wheel(self, event):
        # Получаем угол поворота колеса мыши
        angle = event.angleDelta().y()
        #key_event = QKeyEvent(QKeyEvent)
        #self.ui.scale_cmb.setCurrentIndex(0)
        if event.modifiers() == (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.NoModifier):
            self.zoom(True) if angle > 0 else self.zoom(False)
        elif event.modifiers() == (Qt.KeyboardModifier.ShiftModifier | Qt.KeyboardModifier.NoModifier):
            self.ui.space.scrollContentsBy(2, 0) if angle > 0 else self.ui.space.scrollContentsBy(-2, 0)
            #self.ui.space.translate(1.2, 1) if angle > 0 else self.ui.space.translate(0.8, 1)
        else:
            #self.ui.space.scroll(0, 2) if angle > 0 else self.ui.space.scroll(0, -2)
            self.ui.space.translate(1, 1.2) if angle > 0 else self.ui.space.translate(1, 0.8)
        
    def zoom(self, plus):
        # Определяем коэффициент масштабирования
        if plus:
            self.scale_count += 1 # увеличение
            if self.scale_count > 9:
                self.scale_count = 9
            else:
                if self.scale_count > 0:
                    self.scale = (1 - 0.1 * (self.scale_count-1)) / (1 - 0.1 * self.scale_count)
                else:
                    self.scale = (1 + 0.1 * self.scale_count) / (1 + 0.1 * int(self.scale_count-1))
                self.ui.space.scale(self.scale, self.scale) # увеличение
        else:
            self.scale_count -= 1 # уменьшение
            if self.scale_count < -9:
                self.scale_count = -9
            else:
                if self.scale_count < 0:
                    self.scale = (1 + 0.1 * self.scale_count) / (1 + 0.1 * (self.scale_count+1))
                else:
                    self.scale = (1 - 0.1 * (self.scale_count+1)) / (1 - 0.1 * self.scale_count)
                self.ui.space.scale(self.scale, self.scale) # уменьшение
        self.ui.scale_cmb.setItemText(0,f'{100 + self.scale_count * 10}%')
        print(self.scale_count)

    def zoom_button_current(self):
        current_index = self.ui.scale_cmb.currentIndex()
        current_text = self.ui.scale_cmb.currentText()

        self.ui.scale_cmb.setItemText(0, current_text)
        #self.ui.scale_cmb.setCurrentIndex(0)

        match (current_index):
            case 1:
                self.scale = 1.9 / self.scale #/ 1.9
                self.scale_count = 9
                self.ui.space.scale(self.scale, self.scale)
            case 2:
                self.scale = 1.5 / self.scale #/ 1.5
                self.scale_count = 5
                self.ui.space.scale(self.scale, self.scale)
            case 3:
                self.scale = 1.0 / self.scale #/ 1.0
                self.scale_count = 0
                self.ui.space.scale(self.scale, self.scale)
            case 4:
                self.scale = 0.5 / self.scale #/ 0.5
                self.scale_count = -5
                self.ui.space.scale(self.scale, self.scale)
            case 5:
                self.scale = 0.1 / self.scale #/ 0.1
                self.scale_count = -9
                self.ui.space.scale(self.scale, self.scale)
        print('Scaling')

    def select_scene(self, scene):
        property_vbx = QVBoxLayout()
        type_name = QLabel('', parent=property_vbx)
        scene_name = QLineEdit(scene.name, parent=property_vbx)
        background = QPixmap(scene.width, scene.height, parent=property_vbx)
        background_color = Qt.GlobalColor()
        background_image = None
    
    def select_persona(self, persona):
        property_vbx = QVBoxLayout()
        type_name = QLabel('', parent=property_vbx)
        persona_name = QLineEdit(persona.name, parent=property_vbx)
        skin = QPixmap(parent=property_vbx)

    def select_replica(self):
        pass
    
    def to_welcome(self):
        self.controller.to_welcome()
    
    def update(self):
        pass


    #OnClick() на объект, на поля ... Changed?