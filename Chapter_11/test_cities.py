# 11.1.1 test cities

from city_functions import city_country

def test_city_country():
    """Do city and country names work correctly?"""
    formatted_name = city_country('stockholm', 'sweden')
    assert formatted_name == 'Stockholm, Sweden'