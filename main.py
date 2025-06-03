import sys
from PyQt6.QtWidgets import QApplication
from model.model import Model
from model.list_model import ListModel
from model.novel_model import NovelModel
from model.scene_model import SceneModel
from model.persona_model import PersonaModel
from model.replica_model import ReplicaModel
#from model.novel_list_model import NovelListModel
from controller.welcome_controller import WelcomeController
from utility.manager import ControllerManager

def main():
    app = QApplication(sys.argv)

    #con = sqlite3.connect('db/database.db')
    #Model.connection = con
    #ListModel.connection = con
    novel_model = NovelModel()
    #list_model = NovelListModel()

    controller_manager = ControllerManager(novel_model, )
    controller_manager.set_controller('welcome')
    #controller = WelcomeController(model)#, list_model)

    app.exec()

if __name__ == '__main__':
    sys.exit(main())