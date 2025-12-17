from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Coffee(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    city_name = Column(String(250), comment="Город продажи")
    shop_type_name = Column(String(250), comment="Тип торговой точки")
    network_name = Column(String(250), comment="Название торговой сети")
    brand_owner_name = Column(String(250), comment="Название бренда кофе")
    brand_name = Column(String(250), comment="")
    subbrand_name = Column(String(250), comment="Вкус кофе")
    garbage_name = Column(String(250), comment="Состояние (растворимый, 3в1 и т.д.")
    product_name = Column(String(250), comment="Продукт")
    quantity = Column(Integer, comment="Количество")
    price = Column(Float, comment="Цена")
    cover_name = Column(String(250), comment="Тип упаковки")

    def __repr__(self):
        return f"{self.brand_owner_name} {self.brand_name} - {self.subbrand_name}"
