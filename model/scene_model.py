from model.model import Model
from model.scene import Scene



class SceneModel(Model):
    def __init__(self):
        #self.modified_for_insert = {}
        #self.modified_for_update = {}
        self.scenes = []
        self.scene_number = 1

    def get_next_number(self, number):
        is_free = True
        for scene in self.scenes:
            if scene.name == 'Сцена' + number:
                is_free = False
        if is_free:
            self.scene_number = number+1
            return number
        else:
            self.get_next_number(number+1)
    
    def create(self, width, height):
        scene_name = 'Сцена' + str(self.get_next_number(self.scene_number))
        return Scene(None, scene_name, None, width, height, None)

    def insert(self, scene):
        cur = self.connection.cursor()
        cur.execute('''
                    INSERT INTO scene (scene_name, scene_background, novel)
                    VALUES (?, ?, ?)''',
                    (scene.name, scene.blob_background, scene.novel))
        self.connection.commit()

    def update(self, scene):
        cur = self.connection.cursor()
        cur.execute('''
                    UPDATE scene 
                    SET scene_name = ?, scene_background = ?
                    WHERE scene_id = ?''',
                    (scene.name, scene.blob_background, scene.id))
        self.connection.commit()

    def select_all(self):
        self.scenes = set()
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM scene''')
        results = cur.fetchall()
        for result in results:
            scene = Scene(str(result[0]), result[1], result[2], result[3])
            self.scenes.add(scene)
        self.connection.commit()
        return self.scenes
    
    def select_by_id(self, id):
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM scene
                    WHERE scene_id = ?''',
                    (id))
        result = cur.fetchone()
        scene = Scene(str(result[0]), result[1], result[2], result[3])
        self.connection.commit()
        return scene

    def delete(self, scene):
        cur = self.connection.cursor()
        cur.execute('''
                    DELETE 
                    FROM scene
                    WHERE scene_id = ?''',
                    (scene.id))
        self.connection.commit()