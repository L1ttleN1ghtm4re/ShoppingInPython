import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import *


class TestCartItem(unittest.TestCase):

    # region private attributes
    __cartItem = CartItem
    __price = 0.00
    __quantity = 0
    # endregion private attributes

    def setUp(self):
        self.__quantity = 1
        self.__articles = ArticleGenerator.generate(1)
        self.__cartItem = CartItem(self.__articles[0], self.__quantity)

    def test_allProperties_afterInstantiation_success(self):
        # given
        # refer to Setup
        self.__price = float(2.00)
        # when
        # Event will be triggered by constructor

        # then
        self.assertEqual(self.__cartItem.article.price, self.__price)
        self.assertEqual(self.__cartItem.quantity, self.__quantity)

    def test_quantity_correctValue_getNewValue(self):
        # given
        self.expected_quantity = 2
        # when
        self.__cartItem._quantity = self.expected_quantity
        # then
        self.assertEqual(self.__cartItem._quantity, self.expected_quantity)

    def test_quantity_wrongValue_throwException(self):
        # given
        self.expected_quantity = -2
        # when
        self.assertRaises(WrongQuantityException)
        # then
        # throw exception
