import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publishers"

    publisher_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

    def __str__(self):
        return f'{self.publisher_id}: {self.name}'

class Book(Base):
    __tablename__ = "books"

    book_id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=80), nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publishers.publisher_id"), nullable=False)

    publishers = relationship(Publisher, backref="publishers")

    def __str__(self):
        return f'{self.book_id}: {self.title}. Автор: {self.publisher_id}'

class Shop(Base):
    __tablename__ = "shops"

    shop_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False)

    def __str__(self):
        return f'{self.shop_id}: {self.name}'

class Stock(Base):
    __tablename__ = "stocks"

    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("books.book_id"), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shops.shop_id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship(Book, backref="books")
    shops = relationship(Shop, backref="shops")

    def __str__(self):
        return f'{self.stock_id}: книга - {self.book_id}, магазин - {self.shop_id}, кол-во - {self.count}'

class Sale(Base):
    __tablename__ = "sales"

    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.String(length=10), nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey("stocks.stock_id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship(Stock, backref="stocks")

    def __str__(self):
        return f'{self.sale_id}: цена - {self.price}, дата - {self.date_sale}, сток - {self.stock_id}, кол-во - {self.count}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)