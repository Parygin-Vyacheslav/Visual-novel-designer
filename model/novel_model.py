from model.model import Model
from model.novel import Novel



class NovelModel(Model):
    def __init__(self):
        self.observers = []
        self.modified_for_insert = {}
        self.modified_for_update = {}
    
    # Методы
    def create(self, novel):
        cur = self.connection.cursor()
        cur.execute('''
                    INSERT INTO novel (novel_name, novel_cover)
                    VALUES (?, ?)''',
                    (novel.name, novel.blob_cover))
        self.connection.commit()
        self.notify_observers()

    def update(self, novel):
        cur = self.connection.cursor()
        cur.execute('''
                    UPDATE novel 
                    SET novel_name = ?, novel_cover = ?
                    WHERE novel_id = ?''',
                    (novel.name, novel.blob_cover, novel.id))
        self.connection.commit()
        self.notify_observers()

    def delete(self, novel):
        cur = self.connection.cursor()
        cur.execute('''
                    DELETE 
                    FROM novel
                    WHERE novel_id = ?''',
                    (novel.id))
        self.connection.commit()
        self.notify_observers()

    def select_all(self):
        novel_list = set()
        cur = self.connection.cursor()
        results = cur.execute('''
                    SELECT * 
                    FROM novel''')
        for result in results:
            novel = Novel(str(result[0]), result[1], result[2])
            print(novel.observers)
            novel_list.add(novel)
        self.connection.commit()
        return novel_list
    
    def select_by_id(self, id):
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM novel
                    WHERE novel_id = ?''',
                    (id))
        result = cur.fetchone()
        novel = Novel(str(result[0]), result[1], result[2])
        self.connection.commit()
        return novel
    
    def select_by_name(self, name):
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM novel
                    WHERE novel_name = ?''',
                    (name,))
        result = cur.fetchone()
        novel = Novel(str(result[0]), result[1], result[2])
        self.connection.commit()
        return novel