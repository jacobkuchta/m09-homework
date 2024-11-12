import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("War of the Worlds", 4)
        self.assertTrue("War of the Worlds" in lover.book_list['book_name'].values)

    def test_2_add_book(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("War of the Worlds", 4)
        lover.add_book("War of the Worlds", 4)
        self.assertEqual(len(lover.book_list[lover.book_list['book_name'] == "War of the Worlds"]), 1)
                
    def test_3_has_read(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("War of the Worlds", 4)
        self.assertTrue(lover.has_read("War of the Worlds"))
        
    def test_4_has_read(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(lover.has_read("Harry Potter"))
        
    def test_5_num_books_read(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("War of the Worlds", 4)
        lover.add_book("Harry Potter", 5)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("War of the Worlds", 4)
        lover.add_book("Harry Potter", 2)
        lover.add_book("Fahrenheit 451", 5)
        fav_books = lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
