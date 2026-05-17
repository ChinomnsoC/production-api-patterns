from sqlalchemy import UUID, String, DateTime
from sqlalchemy.orm import mapped_column
from app.db.base import Base

import uuid



class User(Base):
    __tablename__ = "user"
    
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = mapped_column(String(30), nullable=False, unique=True)
    email = mapped_column(String, unique=True)
    first_name = mapped_column(String)
    last_name = mapped_column(String)
    deleted_at = mapped_column(DateTime, nullable=True)
    password_hash = mapped_column(String)

    
    
#     users table:
#   id (UUID, primary key)        ← internal database identifier
#   username (String, unique)     ← human-readable identifier


    
    
    # users: id, username, email, first_name, 
    # last_name, password_hash, last_login, created_at, updated_at, deleted_at