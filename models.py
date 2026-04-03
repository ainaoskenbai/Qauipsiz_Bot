from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class CheckedItem(Base):
    __tablename__ = "checked_items"

    id = Column(Integer, primary_key=True)
    type = Column(String)       # url / phone / sms
    value = Column(String)      # сама ссылка или номер
    result = Column(String)     # результат проверки