import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import *
from shopping.article import Article


class TestCartItem(unittest.TestCase):

    # region private attributes
    __cartItem = CartItem
    __price = float(0.00)
    __quantity = 0
    # endregion private attributes

    def setUp(self):
        self.__quantity = 1
        self.__articles = ArticleGenerator.generate(1)
        self.__cartItem = CartItem(self.__articles[0], self.__quantity)

    def test_AllProperties_AfterInstantiation_Success(self):
        # given
        # refer to Setup
        self.__price = float(2.00)
        # when
        # Event will be triggered by constructor
        self.__cartItem.article.price = self.__price
        # then
        self.assertEqual(self.__cartItem.article.price, self.__price)
        self.assertEqual(self.__cartItem.quantity, self.__quantity)

    def test_SetQuantity_CorrectValue_GetNewValue(self):
        # given
        self.expected_quantity = 2
        # when
        self.__cartItem._quantity = self.expected_quantity
        # then
        self.assertEqual(self.__cartItem._quantity, self.expected_quantity)

    def test_SetQuantity_WrongValue_ThrowException(self):
        # given
        self.expected_quantity = -2
        # when
        self.assertRaises(WrongQuantityException)
        # then
        # throw exception
