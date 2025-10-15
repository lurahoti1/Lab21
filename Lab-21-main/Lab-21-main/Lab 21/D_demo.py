from A_models import Book, Member
from B_methods import Book as BookMethods, Member as MemberMethods
from C_factories import Book as BookFactory, Member as MemberFactory

b1 = BookFactory("97899943", "Python Bazë", "A. Hoxha", 1200.0)
b2 = BookFactory("97888888", "OOP në Python", "E. Dema", 800.0)

b3 = BookFactory.from_string("97811111;Algoritme;B. Dervishi;900")
try:
    b4 = BookFactory.from_string("gabim;pa;format")  
except ValueError as e:
    print("Gabim:", e)

m1 = MemberFactory(12, "Arta Kola", "arta.kola@shkolla.al")
m2 = MemberFactory(15, "Bledi Hysa", "b.hysa@shkolla.al")
m3 = MemberFactory.anonymous()

books = [b1, b2, b3]
members = [m1, m2, m3]

print("LIBRAT:")
count_over_1000 = 0
for book in books:
    base = book._format_money(book.price)
    discounted = book._format_money(book.apply_discount(20))
    print(f'- {book} | Bazë: {base} | -20%: {discounted}')
    if book.price > 1000:
        count_over_1000 += 1

print("\nANËTARËT:")
for member in members:
    print(f'- {member}')

print(f"\nTot > 1000 L: {count_over_1000}")
