class Book:
    def __init__(self, isbn, title, author, price):
        if price < 0:
            raise ValueError("Çmimi nuk mund të jetë negativ.")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'Book[{self.isbn}] "{self.title}" — {self.author} | {self.price:.2f} L'


class Member:
    def __init__(self, member_id, full_name, email):
        if member_id <= 0:
            raise ValueError("ID duhet të jetë > 0.")
        if not full_name.strip():
            raise ValueError("Emri nuk mund të jetë bosh.")
        if "@" not in email or "." not in email:
            raise ValueError("Email i pavlefshëm.")
        self.member_id = member_id
        self.full_name = full_name
        self.email = email

    def __str__(self):
        return f'Member[{self.member_id}] {self.full_name} <{self.email}>'
