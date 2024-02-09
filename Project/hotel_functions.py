import json

# Function to load hotel data from a JSON file
def load_hotels(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save hotel data to a JSON file
def save_hotels(hot, filename):
    with open(filename, 'w') as file:
        json.dump(hot, file, indent=4)

# Function to add a hotel to the list


# Modify the add_hotel function in hotel_functions.py
def add_hotel(hotels):
    name = input("Enter the hotel name: ")
    location = input("Enter the hotel location: ")
    rating = float(input("Enter the hotel rating (out of 5): "))
    hotel = {'name': name, 'location': location, 'rating': rating}
    hotels.append(hotel)

# Function to delete a hotel from the list
def delete_hotel(hotels):
    name = input("Enter the name of the hotel to delete: ")
    for hotel in hotels:
        if hotel['name'] == name:
            hotels.remove(hotel)
            return
    print(f"Hotel {name} not found.")


# Function to update the rating of a hotel
def update_rating(hotels):
    name = input("Enter the name of the hotel to update rating: ")
    for hotel in hotels:
        if hotel['name'] == name:
            new_rating = float(input("Enter the new rating for the hotel: "))
            hotel['rating'] = new_rating
            print(f"Rating for {name} updated successfully!")
            return
    print(f"Hotel {name} not found.")
# Function to view all hotels
def view_hotels(hotels):
    print("All hotels:")
    for hotel in hotels:
        print(f"Name: {hotel['name']}, Location: {hotel['location']}, Rating: {hotel['rating']}")

