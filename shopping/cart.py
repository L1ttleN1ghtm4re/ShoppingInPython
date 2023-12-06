from shopping.cartItem import CartItem


class Cart:
    # region private attributes
    __cartItems = []
    # endregion private attributes

    def __init__(self):
        self.__cartItems = []

    def add(self, cartitems_to_add):
        self.__cartItems.extend(cartitems_to_add)

    def remove(self):
        raise NotImplementedError

    @property
    def cartitems(self) -> [CartItem]:
        return self.__cartItems

    def price(self, average: bool = False):
        self.currentcartprice = 0.00
        self.currentcartiemlen = len(self.__cartItems)
        for self.cartItem in self.__cartItems:
            self.currentcartprice = self.__cartItems[0].article.price

        if average:
            return self.currentcartprice / self.currentcartiemlen

        return self.currentcartprice

    def doesexist(self, articleid):
        raise NotImplementedError

    def cheapest(self):
        raise NotImplementedError

    def mostexpensive(self):
        raise NotImplementedError


class CartException(Exception):
    pass


class ArticleNotFoundException(CartException):
    pass
