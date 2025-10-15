class Book:

    @classmethod
    def from_string(cls, data_str):
        try:
            isbn, title, author, price = data_str.split(";")
            return cls(isbn, title, author, float(price))
        except Exception:
            raise ValueError("Formati i të dhënave është i gabuar.")


class Member:

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @classmethod
    def anonymous(cls):
        return cls(0, "Anonim", "anonim@shkolla.al")
