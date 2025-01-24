from database.db_config import SessionLocal
from database.models import Memory

class LongTermMemory:
    def __init__(self, project_id):
        self.project_id = project_id  
    
    def save_context(self, text):
        db = SessionLocal()
        try:
            memory = Memory(context=text, project_id=self.project_id)
            db.add(memory)
            db.commit()
        finally:
            db.close()

    def get_all_contexts(self):
        db = SessionLocal()
        try:
            memories = db.query(Memory).filter_by(project_id=self.project_id).all()  
            return [memory.context for memory in memories]
        finally:
            db.close()
