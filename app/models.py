from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    wallet_address = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    credentials = relationship("Credential", back_populates="owner")


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    issuer = Column(String)
    issue_date = Column(DateTime, default=datetime.utcnow)
    verification_hash = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="credentials")
