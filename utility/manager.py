from controller.welcome_controller import WelcomeController
from controller.editor_controller import EditorController



class ControllerManager():
    def __init__(self, novel_model):
        self.novel_model = novel_model

    def set_controller(self, controller_name, novel=None, width=None, height=None):
        match controller_name:
            case 'welcome':
                self.active_controller = WelcomeController(self, self.novel_model)
            case 'editor':
                self.active_controller = EditorController(self, novel, self.novel_model, width, height)
            case _:
                Exception
            