import unittest

def booksearch():
    return{}

class BookSearchTest(unittest.TestCase):
    def test_booksearch(self):
        self.assertEquals({}, booksearch())