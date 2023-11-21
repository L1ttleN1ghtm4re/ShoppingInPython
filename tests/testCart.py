import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import CartItem
from shopping.cart import Cart
from shopping.article import Article


class TestCart(unittest.TestCase):
    # region private attributes
    _cart = None
    # endregion private attributes

    def setUp(self):
        self._cart = Cart

    def test_add_firstsinglecartitem_success(self):
        # given
        # refer to setup
        self.expectedarticlesquantity = 1
        self.expectedarticles = Article, ArticleGenerator.generate(self.expectedarticlesquantity)
        self.expectedarticleincartitem = 1

        self.expectedCartItem = CartItem(self.expectedarticles[0], self.expectedarticleincartitem)
        self.expectedCartItems = CartItem(self.expectedCartItem)
        self.assertEqual(self._cart, 0)

        # when
        self._cart.add(self.expectedCartItem)
        # then

        self.assertEqual(self._cart.Count(), self.expectedArticlesquantity)

