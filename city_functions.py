

def city_country(city, country, population=0):
        """Return a string representing a city-country pair."""
        output_string = city.title() + ", " + country.title()
        if population:
            output_string += ' - population ' + str(population)
        return output_string

#describe_city("Moscow", "Russia")
#describe_city("San Diego")
#describe_city("Johanisburg", "Africa")
