from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() 
class Customer(Base):
   __tablename__ = 'customers'

   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

class Invoice(Base):
   __tablename__ = 'invoices'
   
   id = Column(Integer, primary_key = True)
   cusid=Column(Integer,ForeignKey('customers.id'))
   invno = Column(Integer)
   amount = Column(Integer)
   customer = relationship("Customer", back_populates = "invoices")

# Customer.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "customer")
# Base.metadata.create_all(engine)