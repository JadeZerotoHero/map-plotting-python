"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country, add_city_to_country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    #city,city_ascii,lat,lng,country,iso2,iso3,admin_name,capital,population,id
    #city,city_ascii,lng,admin_name,iso3,lat,population,id,capital,country
    #Table: city_ascii (as city give weird symbols like kōbe rather than kobe)
    #       , lat, lng (coordinates), city_type, population, city_id

    with open(path_to_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            city_name = row["city_ascii"]
            latitude = float(row["lat"])
            longitude = float(row["lng"])
            country_name = row["country"]
            iso3 = row["iso3"]
            city_type = row["capital"]
            population = int(row["population"]) if row["population"] else 0
            city_id = int(row["id"])
            table = City(city_name, (latitude, longitude), city_type, population, city_id)
            add_city_to_country(table, country_name, iso3)
        csv_file.close

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
