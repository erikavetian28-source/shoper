from sqlalchemy import Column, Integex, String, Text, DataTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class Product(Base):
    __tablename__ = 'product'


    id = Column(Integex, primary_key = True, index=True)
    name = Column(String, nullable = False, index=True)
    description = Column(Text)
    price = Column(Float, nullable = False)
    category_id = Column(Integex, ForeignKey("categories.id"), nullable = False)''
    image_url = Column(String)
    created_at= Column(DataTime, default = datatime.utcnow)


    category = relationship("Category", back_populates="prodects")
    


    def __repr__(self):
        return f"<Poduct*(id = {self.id}, name= '{self.name}', price={self.price})>
