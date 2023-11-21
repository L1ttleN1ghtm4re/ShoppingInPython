import unittest
from shopping.article import *


class TestArticle(unittest.TestCase):

    # region private attributes
    __article = None
    __id = 0
    __description = ""
    __price = 0.0
    # endregion private attributes

    def setUp(self):
        # Private attributes
        self.__id = 1
        self.__description = "product description"
        self.__price = 20.45
        self.__article = Article(self.__id, self.__description, self.__price)

    def test_all_properties_after_instantiation_success(self):
        # given
        # then
        self.assertEqual(self.__id, self.__article.id)
        self.assertEqual(self.__description, self.__article.description)
        self.assertEqual(self.__price, self.__article.price)

    def test_description_short_description_return_new_value(self):
        # given
        self.expected_description = "After Shave"
        # when
        self.__article.description = self.expected_description
        # then
        self.assertEqual(self.__article.description, self.expected_description)

    def test_description_long_description_return_new_value(self):
        # given
        self.expected_description = "A very long long long long long long descriptionn"
        # when
        self.__article.description = self.expected_description
        # then
        self.assertEqual(self.__article.description, self.expected_description)

    def test_description_single_word_description_throw_exception(self):
        # given

        # when
        with self.assertRaises(TooShortDescriptionException):
            check_description("TooShort")
        # then
        # throw exception

    def test_description_descriptioncontainingspecialchars_throwexception(self):
        # given

        # when
        with self.assertRaises(SpecialCharInDescriptionException):
            check_description("Jacques+Daniel")
        # then
        # throw exception

    def test_description_toolongdescription_throwexception(self):
        # given
        # when
        with self.assertRaises(TooLongDescriptionException):
            check_description("A very very very very very looonnng descriptioooooon")
        # then
        # throw exception


if __name__ == '__main__':
    unittest.main()
