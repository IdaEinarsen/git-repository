# 6.11 Cities

cities = {
    "Stockholm":  {
        "country": "Sweden",
        "population": "975,000",
        "fact": "It is built on many islands."
    },

    "Halmstad": {
        "country": "Sweden",
        "population": "70,000",
        "fact": "It is famous for its beaches and summer tourism."
    },

    "Övertorneå": {
        "country": "Sweden",
        "population": "4,000",
        "fact": "It is located near the Finnish border."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")

    for key, value in info.items():
        print(f"{key.title()}; {value}")