# 11.2.1 population

from population_function import city_country

def test_city_country():
    formatted_name = city_country('stockholm', 'sweden')
    assert formatted_name == 'Stockholm, Sweden'

def test_city_country_population():
    formatted_name = city_country(
        'stockholm', 'sweden', population=999200
    )
    assert formatted_name == 'Stockholm, Sweden - population 999200'

