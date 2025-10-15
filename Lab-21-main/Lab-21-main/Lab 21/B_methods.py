class Book:

    def apply_discount(self, percent):
        if not (0 <= percent <= 50):
            raise ValueError("Zbritja duhet të jetë midis 0–50%.")
        discounted_price = self.price * (1 - percent / 100)
        return round(discounted_price, 2)

    def _format_money(self, value):
        return f"{value:.2f} L"


class Member:

    def change_email(self, new_email):
        if "@" not in new_email or "." not in new_email:
            raise ValueError("Email i ri i pavlefshëm.")
        self.email = new_email
