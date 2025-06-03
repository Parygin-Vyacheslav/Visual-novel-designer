from view.editor_view import EditorView
from model.novel_model import NovelModel
from model.scene_model import SceneModel
from model.persona_model import PersonaModel
from model.replica_model import ReplicaModel
from model import novel, scene, persona, replica

class EditorController:
    def __init__(self, manager, novel, novel_model, scene_width, scene_height):#, list_model):
        modified_for_insert = {}
        modified_for_update = {}
        self.controller_manager = manager
        self.novel = novel
        self.novel_model = novel_model
        self.scene_model = SceneModel()
        self.persona_model = PersonaModel()
        self.replica_model = ReplicaModel()

        if novel.id == None:
            self.scene_model.scenes.append(self.scene_model.create(scene_width, scene_height))

        self.editor_view = EditorView(self, self.novel, self.novel_model, self.scene_model, self.persona_model, self.replica_model)#, self.novel_list_model)
        self.editor_view.show()
    
    def to_welcome(self):
        self.editor_view.hide()
        self.controller_manager.set_controller('welcome')
    
    def save_project(self):
        self.elem_changed(self.novel)
        self.elem_changed(self.scene_model.scenes[0])

    def elem_changed(self, elem):
        if elem.id:
            match (elem):
                case type(novel.Novel):
                    self.novel_model.modified_for_update.append(elem)
                case scene.Scene:
                    self.scene_model.modified_for_update.append(elem)
                case persona.Persona:
                    self.persona_model.modified_for_update.append(elem)
                case replica.Replica:
                    self.replica_model.modified_for_update.append(elem)
        else:
            match (elem):
                case type(novel.Novel):
                    self.novel_model.modified_for_insert.append(elem)
                case type(scene.Scene):
                    self.scene_model.modified_for_insert.append(elem)
                case type(persona.Persona):
                    self.persona_model.modified_for_insert.append(elem)
                case type(replica.Replica):
                    self.replica_model.modified_for_insert.append(elem)
        print(self.novel_model.modified_for_insert)
        print(self.scene_model.modified_for_insert)