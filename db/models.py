__all__ = [
    "User",
    "Base",
]

# Про ORM-паттерн асинхронного sqlalchemy и модели
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-orm

# декларативная модель базы данных python
# https://metanit.com/python/database/3.2.php
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DATE, Integer, VARCHAR
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"

    user_id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(32), unique=False, nullable=False)
    reg_data = Column(DATE, default=datetime.now())
