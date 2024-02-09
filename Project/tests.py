import unittest
from unittest.mock import patch
import os
import json
from hotel_functions import load_hotels, save_hotels, add_hotel, delete_hotel

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        print(f"Passed {test}")

    def addError(self, test, err):
        test_name = self.getDescription(test)
        print(f"Failed {test_name}")

    def addFailure(self, test, err):
        # Customizing failure message format
        test_name = self.getDescription(test)
        print(f"Failed {test_name}")

    def getDescription(self, test):
        """Overrides the default getDescription to remove 'E' or 'F' prefix."""
        return str(test)

class TestHotelFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=["Metro", "Test Location", "4.5"])
    def test_add_hotel(self, mock_input):
        FILENAME = 'hotels.json'
        
        # Load existing hotels from JSON file
        hotels = load_hotels(FILENAME)
        
        # Add a hotel with input from user
        add_hotel(hotels)
        
        # Save hotels to JSON file
        save_hotels(hotels, FILENAME)
        
        # Load hotels from JSON file again
        updated_hotels = load_hotels(FILENAME)
        
        # Check if the hotel with the specified name, location, and rating exists in the updated hotel list
        hotel_added = {'name': "Metro", 'location': "Test Location", 'rating': 4.5}
        self.assertTrue(hotel_added in updated_hotels)
        
    def test_delete_hotel(self):
        FILENAME = 'hotels.json'
        
        # Prepare test data
        test_hotel = {'name': 'Metro', 'location': 'Test Location', 'rating': 4.5}
        
        # Create a temporary file for testing
        with open(FILENAME, 'w') as file:
            json.dump([test_hotel], file)
        
        # Load existing hotels from JSON file
        hotels = load_hotels(FILENAME)
        
        # Mock user input
        mock_input = ["Metro"]
        
        # Patch the input function to return predefined values
        with patch('builtins.input', side_effect=mock_input):
            # Call the delete_hotel function
            delete_hotel(hotels)
        
        # Save hotels to JSON file
        save_hotels(hotels, FILENAME)
        
        # Load hotels from JSON file again
        updated_hotels = load_hotels(FILENAME)
        
        # Check if the hotel with the specified name, location, and rating exists in the updated hotel list
        hotel_deleted = {'name': "Metro", 'location': "Test Location", 'rating': 4.5}
        self.assertTrue(hotel_deleted not in updated_hotels)

    # Additional test case for loading and saving hotels

    def test_create_hotels_json(self):
        # Path to the hotels.json file
        filename = 'hotels.json'

        # Check if hotels.json file exists
        if os.path.exists(filename):
            try:
                # Load hotels from existing file
                loaded_hotels = load_hotels(filename)
            except Exception as e:
                self.fail(f"Failed to load {filename}: {e}")

            # Test data
            test_data = [
                {'name': 'Hotel A', 'location': 'Location A', 'rating': 4.5},
                {'name': 'Hotel B', 'location': 'Location B', 'rating': 3.8}
            ]

            try:
                # Save test data to hotels.json file
                save_hotels(test_data, filename)
            except Exception as e:
                self.fail(f"Failed to save data to {filename}: {e}")

            # Check if hotels.json file exists after saving
            self.assertTrue(os.path.exists(filename), f"{filename} should exist after saving")

            try:
                # Load hotels from the saved JSON file
                loaded_hotels = load_hotels(filename)

                # Check if loaded data matches the test data
                self.assertEqual(loaded_hotels, test_data)
            except Exception as e:
                self.fail(f"Failed to load data from {filename}: {e}")
        else:
            self.fail(f"{filename} does not exist. Unable to test load and save features.")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHotelFunctions)
    runner = unittest.TextTestRunner(resultclass=CustomTextTestResult)
    result = runner.run(suite)
