from shopping.cartItem import CartItem


class Cart:
    # region private attributes
    __cartItems = []
    # endregion private attributes

    def add(self, addcartitems):
        self.__cartItems = addcartitems

    def remove(self):
        raise NotImplementedError

    @property
    def cartitems(self) -> [CartItem]:
        return self.__cartItems

    def doesexist(self):
        raise NotImplementedError

    def cheapest(self):
        raise NotImplementedError

    def mostexpensive(self):
        raise NotImplementedError
