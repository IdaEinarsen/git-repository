# 11.12 Population function


def city_country(city, country, population=""):
    """Return city, country and population neatly"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

    

      
   

