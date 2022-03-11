import unittest
from car import Car

class TestCar(unittest.TestCase):

    def test_instantiated(self):
        car = Car('Volkswagen', 'Kever', 'Red')
        self.assertIsInstance(car, Car)

    def test_mileage_is_0(self):
        car = Car('Volkswagen', 'Kever', 'Red')
        self.assertEqual(car._mileage, 0)

    def test_mileage_is_set(self):
        car = Car('Volkswagen', 'Kever', 'Red', 100000)
        self.assertEqual(car._mileage, 100000)

    def test_mileage_after_drive(self):
        # Arange
        initial_mileage = 100000
        distance = 1234
        car = Car('Volkswagen', 'Kever', 'Red', initial_mileage)

        # Act
        car.drive(distance)

        # Assert
        actual = car._mileage
        expected = initial_mileage + distance
        self.assertEqual(expected, actual)

    def test_mileage_after_drive_negative_distance_raises_exception(self):

        initial_mileage = 100000
        distance = -1234
        car = Car('Volkswagen', 'Kever', 'Red', initial_mileage)

        # drive with a negative distance raise an exception
        with self.assertRaises(Exception):
            car.drive(distance)

if __name__ == '__main__':
    unittest.main()
