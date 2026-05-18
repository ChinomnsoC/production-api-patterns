from sqlalchemy import UUID, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column
from app.db.base import Base

import uuid


class Post(Base):
    __tablename__ = "post"
    
    
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = mapped_column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    deleted_at = mapped_column(DateTime, nullable=True)
    created_at = mapped_column(DateTime, nullable=False)
    content = mapped_column(String)