import os
from hotel_functions import load_hotels, save_hotels, add_hotel, delete_hotel, update_rating, view_hotels

# Define the filename for storing hotel data
FILENAME = 'hotels.json'

# Main function
def main():
    # Load hotel data from the JSON file
    hotels = load_hotels(FILENAME)

    while True:
        print("\n1. Add a hotel\n2. Delete a hotel\n3. Update hotel rating\n4. View all hotels\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_hotel(hotels)
        elif choice == '2':
            delete_hotel(hotels)
        elif choice == '3':
            update_rating(hotels)
        elif choice == '4':
            view_hotels(hotels)
        elif choice == '5':
            # Save hotel data to the JSON file before exiting
            save_hotels(hotels, FILENAME)
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
