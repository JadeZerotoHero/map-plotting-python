"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
from city import City, get_city_by_id, get_cities_by_name
from csv_parsing import create_cities_countries_from_csv
from country import Country
from vehicles import Vehicle, create_example_vehicles
from itinerary import Itinerary
from path_finding import find_shortest_path
from map_plotting import plot_itinerary

import matplotlib.pyplot as plt

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("=============== Main Menu ===============")
    print("Welcome to Onboard Navigation!")
    print("1. View available vehicles")
    print("2. Select a vehicle and start navigation \n (find shortest path and plot the itinerary)")
    print("3. View world cities")
    print("4. Exit")
    print("=========================================")

def view_world_cities():
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following options")

def view_available_vehicles(vehicles_dict):
    print("Available vehicles:")
    print("1. CrappyCrepeCar (200 km/h)\n"
          "2. DiplomacyDonutDinghy (100 km/h | 500 km/h)\n"
          "3. TeleportingTarteTrolley (3 h | 2000 km)")

def start_navigation(vehicles_dict):
    # Get user input for vehicle selection
    view_available_vehicles(vehicles_dict)
    vehicle_choices = {"1": "CrappyCrepeCar", "2": "DiplomacyDonutDinghy", "3": "TeleportingTarteTrolley"}
    vehicle_choice = validate_input("Select a vehicle (1, 2, or 3): ", vehicle_choices.keys())
    vehicle_name = vehicle_choices[vehicle_choice]
    vehicle = vehicle_name

    # Call main() function with the selected vehicle
    main(vehicle)

def menu():
    # List available vehicles
    vehicles_dict = create_example_vehicles()

    while True:
        clear_screen()
        print_menu()

        choice = validate_input("Please choose an option (1-3): ", ["1", "2", "3"])

        if choice == "1":
            clear_screen()
            view_available_vehicles(vehicles_dict)
            input("Press Enter to return to the main menu.")

        elif choice == "2":
            clear_screen()
            start_navigation(vehicles_dict)

        elif choice == "3":
            # Clear the screen and display world cities
            clear_screen()
            view_world_cities()
            input("Press Enter to continue...")

        elif choice == "4":
            print("Thanks for using Onboard Navigation! Goodbye!")
            break

def main(vehicle):
    # Get user input for origin city
    origin_city_name = input("Enter origin city name: ")
    origin_cities = get_cities_by_name(origin_city_name)
    if not origin_cities:
        print(f"Origin city '{origin_city_name}' not found.")
        return
    elif len(origin_cities) > 1:
        print("Multiple cities found with the same name. Please choose by entering the ID:")
        for city in origin_cities:
            print(f"{city} - {city.city_id}")
        origin_city_id = int(input("Enter origin city ID: "))
        origin_city = get_city_by_id(origin_city_id)
    else:
        origin_city = origin_cities[0]

    # Get user input for destination city
    dest_city_name = input("Enter destination city name: ")
    dest_cities = get_cities_by_name(dest_city_name)
    if not dest_cities:
        print(f"Destination city '{dest_city_name}' not found.")
        return
    elif len(dest_cities) > 1:
        print("Multiple cities found with the same name. Please choose by entering the ID:")
        for city in dest_cities:
            print(f"{city} - {city.city_id}")
        dest_city_id = int(input("Enter destination city ID: "))
        dest_city = get_city_by_id(dest_city_id)
    else:
        dest_city = dest_cities[0]

    # Find shortest path and plot the itinerary if a path exists
    itinerary = find_shortest_path(vehicle, origin_city, dest_city)
    if itinerary:
        print(f"Shortest path found: {itinerary}")
        plot_itinerary(itinerary)
        plt.savefig(f"map_{origin_city.name}_{dest_city.name}.png")
        plt.show()
    else:
        print("No path found between the two cities for the selected vehicle.")

if __name__ == "__main__":
    menu()
