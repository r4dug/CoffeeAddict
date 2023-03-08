import unittest
from src.locate_coffee_shop import ProximateCoffeeShop, locate_closest_coffee_shops


class TestLocateCoffeeShop(unittest.TestCase):

    # test with a wrong file path
    def test_locate_coffee_shop_no_file(self):
        file_path = 'fake_file.csv'
        user_x = 47.5809
        user_y = -122.3160
        try:
            locate_closest_coffee_shops(user_x, user_y, file_path)
        except Exception as ex:
            assert "Input file does not exist." in str(ex)

    def test_locate_coffee_shop(self):
        user_location = [0, 0]
        coffee_shops = [['Loc 1', 1, 1],
                        ['Loc 2', 2, 2],
                        ['Loc 3', 3, 3],
                        ['Loc 4', 4, 4],
                        ['Loc 5', 5, 5],
                        ['Loc 6', 6, 6]]
        expected_response = [ProximateCoffeeShop(name='Loc 1', distance=1.4142),
                             ProximateCoffeeShop(name='Loc 2', distance=2.8284),
                             ProximateCoffeeShop(name='Loc 3', distance=4.2426)]
        self.assertEqual(locate_closest_coffee_shops(user_location[0], user_location[1], coffee_shops),
                         expected_response)

    def test_locate_coffee_shop_fail(self):
        user_location = [0, 0]
        coffee_shops = [['Loc 1', 1, 1],
                        ['Loc 2', 2, 2],
                        ['Loc 3', '3', 'string'],
                        ['Loc 4', 4],
                        [],
                        ['Loc 5', 5, 5]]
        expected_response = [ProximateCoffeeShop(name='Loc 1', distance=1.4142),
                             ProximateCoffeeShop(name='Loc 2', distance=2.8284),
                             ProximateCoffeeShop(name='Loc 5', distance=7.0711)]
        '''Expected issues: - Could not convert string to float: 'string' ,
                            - Not enough values to unpack (expected 3, got 2) ,
                            - Not enough values to unpack (expected 3, got 0) ,
        '''
        self.assertEqual(locate_closest_coffee_shops(user_location[0], user_location[1], coffee_shops),
                         expected_response)


if __name__ == '__main__':
    unittest.main()
