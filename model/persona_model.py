from model.model import Model
from model.persona import Persona

class PersonaModel(Model):
    def __init__(self):
        self.modified_for_insert = {}
        self.modified_for_update = {}
        
    def create(self, persona):
        cur = self.connection.cursor()
        cur.execute('''
                    INSERT INTO persona (persona_name, persona_skin, scene)
                    VALUES (?, ?, ?)''',
                    (persona.name, persona.blob_skin, persona.scene))
        self.connection.commit()

    def update(self, persona):
        cur = self.connection.cursor()
        cur.execute('''
                    UPDATE persona 
                    SET persona_name = ?, persona_skin = ?
                    WHERE persona_id = ?''',
                    (persona.name, persona.blob_skin, persona.id))
        self.connection.commit()

    def select_all(self):
        personas = set()
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM persona''')
        results = cur.fetchall()
        for result in results:
            persona = Persona(str(result[0]), result[1], result[2], result[3])
            personas.add(persona)
        self.connection.commit()
        return personas
    
    def select_by_id(self, id):
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM persona
                    WHERE persona_id = ?''',
                    (id))
        result = cur.fetchone()
        persona = Persona(str(result[0]), result[1], result[2], result[3])
        self.connection.commit()
        return persona

    def delete(self, persona):
        cur = self.connection.cursor()
        cur.execute('''
                    DELETE 
                    FROM persona
                    WHERE persona_id = ?''',
                    (persona.id))
        self.connection.commit()