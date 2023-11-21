from shopping.article import Article


class CartItem:

    def __init__(self, article_, quantity_):
        self._article = Article
        self._quantity = quantity_

    @property
    def article(self):
        return self._article

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


class CartItemException(Exception):
    pass


class WrongQuantityException(CartItemException):
    pass
