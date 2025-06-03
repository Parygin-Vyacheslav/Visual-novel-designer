from model.model import Model
from model.replica import Replica

class ReplicaModel(Model):
    def __init__(self):
        self.modified_for_insert = {}
        self.modified_for_update = {}
        
    def create(self, replica):
        cur = self.connection.cursor()
        cur.execute('''
                    INSERT INTO replica (replica_text, replica_number, persona)
                    VALUES (?, ?, ?)''',
                    (replica.text, replica.number, replica.persona))
        self.connection.commit()

    def update(self, replica):
        cur = self.connection.cursor()
        cur.execute('''
                    UPDATE replica 
                    SET replica_text = ?, replica_number = ?
                    WHERE replica_id = ?''',
                    (replica.text, replica.number, replica.id))
        self.connection.commit()

    def select_all(self):
        replicas = set()
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM replica''')
        results = cur.fetchall()
        for result in results:
            replica = Replica(str(result[0]), result[1], result[2], result[3])
            replicas.add(replica)
        self.connection.commit()
        return replicas
    
    def select_by_id(self, id):
        cur = self.connection.cursor()
        cur.execute('''
                    SELECT * 
                    FROM replica
                    WHERE replica_id = ?''',
                    (id))
        result = cur.fetchone()
        replica = Replica(str(result[0]), result[1], result[2], result[3])
        self.connection.commit()
        return replica

    def delete(self, replica):
        cur = self.connection.cursor()
        cur.execute('''
                    DELETE 
                    FROM replica
                    WHERE replica_id = ?''',
                    (replica.id))
        self.connection.commit()