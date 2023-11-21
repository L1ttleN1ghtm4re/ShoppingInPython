import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import *


class TestCartItem(unittest.TestCase):

    _cartItem = None
    _price = 0.00
    _quantity = 0

    def setUp(self):
        self._quantity = 1
        self._articles = [], ArticleGenerator.generate(1)
        self._cartItem = CartItem(self._articles[0], self._quantity)

    def test_AllProperties_AfterInstantiation_Success(self):
        # given
        # refer to Setup
        self._price = 2.00
        # when
        # Event will be triggered by constructor
        self._cartItem.article.price = self._price
        # then
        self.assertEqual(self._cartItem.article.price, self._price)
        self.assertEqual(self._cartItem.quantity, self._quantity)

    def test_SetQuantity_CorrectValue_GetNewValue(self):
        # given
        self.expected_quantity = 2
        # when
        self._cartItem._quantity = self.expected_quantity
        # then
        self.assertEqual(self._cartItem._quantity, self.expected_quantity)

    def test_SetQuantity_WrongValue_ThrowException(self):
        # given
        self.expected_quantity = -2
        # when
        self.assertRaises(WrongQuantityException)
        # then
        # throw exception
