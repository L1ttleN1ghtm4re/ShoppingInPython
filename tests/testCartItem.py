import unittest

from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import *


class TestCartItem(unittest.TestCase):

    # region private attributes
    __cartItem: CartItem = CartItem
    __price: float = 0.00
    __quantity: int = 0
    # endregion private attributes

    # region public methods
    def setUp(self):
        self.__quantity: int = 1
        self.__articles: [Article] = ArticleGenerator.generate(1)
        self.__cartItem: CartItem = CartItem(self.__articles[0],
                                             self.__quantity)

    def test_allProperties_afterInstantiation_success(self):
        # given
        # refer to Setup
        self.__price: float = 2.00
        # when
        # Event will be triggered by constructor

        # then
        self.assertEqual(self.__cartItem.article.price, self.__price)
        self.assertEqual(self.__cartItem.quantity, self.__quantity)
        self.assertFalse(self.__cartItem.for_adult_only)

    def test_AllProperties_AfterInstantiationWithForAdultOnlyOption_GetTrue(self):
        # given
        # refer to Setup
        self.__price: float = 2.00
        self.__cartItem.for_adult_only = True
        # when
        # Event will be triggered by constructor

        # then
        self.assertEqual(self.__cartItem.article.price, self.__price)
        self.assertEqual(self.__cartItem.quantity, self.__quantity)
        self.assertTrue(self.__cartItem.for_adult_only)

    # region quantity
    def test_quantity_correctValue_getNewValue(self):
        # given
        self.expected_quantity: int = 2
        # when
        self.__cartItem._quantity = self.expected_quantity
        # then
        self.assertEqual(self.__cartItem._quantity,
                         self.expected_quantity)

    def test_quantity_wrongValue_throwException(self):
        # given
        self.expected_quantity: int = -2
        # when
        self.assertRaises(WrongQuantityException)
        # then
        # throw exception
    # endregion quantity
    # endregion public methods


if __name__ == '__main__':
    unittest.main()
