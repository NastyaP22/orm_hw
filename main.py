import os
import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from models import create_tables, Publisher, Book, Shop, Stock, Sale

load_dotenv()

# conn = psycopg2.connect(database='bookshop', user='postgres', password='avebilly1906')

user = os.getenv('user')
password = os.getenv('password')
database_name = os.getenv('database_name')

DSN = f'postgresql://{user}:{password}@localhost:5432/{database_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Достоевский')
book1 = Book(title='Капитанская дочка', publisher_id=1)
book2 = Book(title='Руслан и Людмила', publisher_id=1)
book3 = Book(title='Евгений Онегин', publisher_id=1)
book4 = Book(title='Преступление и наказание', publisher_id=2)
book5 = Book(title='Идиот', publisher_id=2)
shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Книжный дом')
stock1 = Stock(book_id=1, shop_id=1, count=19)
stock2 = Stock(book_id=1, shop_id=2, count=16)
stock3 = Stock(book_id=1, shop_id=3, count=9)
stock4 = Stock(book_id=2, shop_id=1, count=22)
stock5 = Stock(book_id=2, shop_id=2, count=7)
stock6 = Stock(book_id=2, shop_id=3, count=16)
stock7 = Stock(book_id=3, shop_id=1, count=19)
stock8 = Stock(book_id=3, shop_id=2, count=10)
stock9 = Stock(book_id=3, shop_id=3, count=11)
stock10 = Stock(book_id=4, shop_id=1, count=15)
stock11 = Stock(book_id=4, shop_id=2, count=14)
stock12 = Stock(book_id=4, shop_id=3, count=10)
stock13 = Stock(book_id=5, shop_id=1, count=4)
stock14 = Stock(book_id=5, shop_id=2, count=20)
stock15 = Stock(book_id=5, shop_id=3, count=13)
sale1 = Sale(price=600, date_sale='09-11-2022', stock_id=1, count=1)
sale2 = Sale(price=500, date_sale='08-11-2022', stock_id=4, count=1)
sale3 = Sale(price=580, date_sale='05-11-2022', stock_id=2, count=1)
sale4 = Sale(price=490, date_sale='02-11-2022', stock_id=9, count=1)
sale5 = Sale(price=600, date_sale='26-10-2022', stock_id=1, count=1)
sale6 = Sale(price=570, date_sale='12-11-2022', stock_id=11, count=1)
sale7 = Sale(price=720, date_sale='13-11-2022', stock_id=15, count=1)

session.add_all([publisher1, publisher2, book1, book2, book3, book4, book5, shop1, shop2, shop3, stock1, stock2, stock3, stock4,
                 stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13, stock14, stock15, sale1, sale2, sale3, sale4, sale5, sale6, sale7])
session.commit()

publisher = input('Введите id издателя: ')

for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).filter(Book.publisher_id == publisher, Shop.shop_id == Stock.shop_id, Stock.book_id == Book.book_id, Sale.stock_id == Stock.stock_id).join(Stock, Sale.stock_id == Stock.stock_id).all():
    sales_list = []
    for e in c:
      sales_list.append(str(e))
    print((' | ').join(sales_list))

session.close()




