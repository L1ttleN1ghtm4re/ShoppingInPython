import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import CartItem
from shopping.cart import Cart


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
        self.expectedarticles = []
        self.expectedarticles = ArticleGenerator.generate(self.expectedarticlesquantity)

        self.expectedarticleincartitem = 1
        self.expectedcartitem = CartItem(self.expectedarticles[0], self.expectedarticleincartitem)
        self.expectedcartitems = [self.expectedcartitem]
        self.assertEqual(0, len(self._cart.cartitems))

        # when

        # then

        # self.assertEqual(self._cart.Count(1), self.expectedarticlesquantity)

    # def test_add_multiplesinglecartitems_success(self):

    # def test_add_onemultiplecartitems_success(self):

    # def test_price_emptycart_getprice(self):
    #    expectedprice = 0.00

    # def test_price_notemptycart_getprice(self):

    # def test_priceaverage_uniquevalue_getaverage(self):

    # def test_doesexist_byid_true(self):

    # def test_doesexist_byid_false(self):

    # def test_cheapest_uniquevalue_getarticleid(self):

    # def test_mostexpensive_uniquevalue_getarticleid(self):
