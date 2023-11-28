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
        raise NotImplementedError

    def doesexist(self):
        raise NotImplementedError

    def cheapest(self):
        raise NotImplementedError

    def mostexpensive(self):
        raise NotImplementedError
