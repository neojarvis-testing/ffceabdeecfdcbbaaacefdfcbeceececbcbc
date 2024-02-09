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
    def test_load_save_hotels(self):
        # Test data
        test_data = [
            {'name': 'Hotel A', 'location': 'Location A', 'rating': 4.5},
            {'name': 'Hotel B', 'location': 'Location B', 'rating': 3.8}
        ]

        # Path to the test hotels.json file
        filename = 'test_hotels.json'

        # Write test data to hotels.json file
        with open(filename, 'w') as file:
            json.dump(test_data, file)

        # Load hotels from the test JSON file
        loaded_hotels = load_hotels(filename)

        # Check if loaded data matches the test data
        self.assertEqual(loaded_hotels, test_data)

        # Additional hotel data to save
        additional_hotel = {'name': 'Hotel C', 'location': 'Location C', 'rating': 4.2}

        # Add additional hotel to the test data
        test_data.append(additional_hotel)

        # Save test data to hotels.json file
        save_hotels(test_data, filename)

        # Load the saved data from the file
        with open(filename, 'r') as file:
            saved_data = json.load(file)

        # Check if the saved data matches the updated test data
        self.assertEqual(saved_data, test_data)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHotelFunctions)
    runner = unittest.TextTestRunner(resultclass=CustomTextTestResult)
    result = runner.run(suite)
