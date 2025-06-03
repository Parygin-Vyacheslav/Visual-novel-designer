from view.welcome_view import WelcomeView
from model.novel_model import Novel

class WelcomeController():
    def __init__(self, manager, novel_model):#, list_model):
        self.controller_manager = manager
        self.novel_model = novel_model
        #self.novel_list_model = list_model
        self.welcome_view = WelcomeView(self, self.novel_model)#, self.novel_list_model)

        self.welcome_view.show()

    def create_novel(self, width, height):
        novel = Novel(None, 'Без названия', None)
        self.welcome_view.hide()
        self.controller_manager.set_controller('editor', novel, width, height)

    def delete_novel(self, novel_name):
        novel = self.novel_model.select_by_name(novel_name)
        self.novel_model.delete(novel)
    
    def save_novel(self, novel_name, cover_file):
        blob_cover = open(cover_file[0], 'rb').read()
        novel = Novel(None, novel_name, blob_cover)
        Novel.create(novel)

    '''def get_novels_list(self):
        return self.select_all()

    def create_novel(self, file_name):
        blob_cover = open(file_name[0], 'rb').read()
        novel = Novel(None, 'novel_3', blob_cover)
        self.create(novel)

    def delete_novel(self, novel_name):
        novel = self.select_by_name(novel_name)
        self.delete(novel)
    
    def save_novel(self, novel):
        self.update(novel)'''

    