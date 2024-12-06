from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.users.infrastructure.repositories.user_postgres_repository import PostgresUserRepository

from app.core.config import settings
from app.core.database.postgresql.connection import get_db

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
async def read_root(db: Session = Depends(get_db)):
    db_session = db
    
    user_repository = PostgresUserRepository(db_session)
    
    user = None
    
    if user is None:
        return {"Hello": "World"}
    
    print(user)
    
    return {"Hello": settings}
  
