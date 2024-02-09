import unittest
from unittest.mock import patch
from hotel_functions import *

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


 

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHotelFunctions)
    runner = unittest.TextTestRunner(resultclass=CustomTextTestResult)
    result = runner.run(suite)
