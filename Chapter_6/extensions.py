# 6.12 Extensions

cities = {
    "Stockholm": {
        "country": "Sweden",
        "population": "975,000",
        "fact": "It is built on many islands.",
        "language": "Swedish"
    },

    "Halmstad": {
        "country": "Sweden",
        "population": "70,000",
        "fact": "It is famous for its beaches and summer tourism.",
        "language": "Swedish"
    },

    "Övertorneå": {
        "country": "Sweden",
        "population": "4,000",
        "fact": "It is located near the Finnish border.",
        "language": "Swedish and Finnish"
    },

    "Umeå": {
        "country": "Sweden",
        "population": "130,000",
        "fact": "It is known as the City of Birches.",
        "language": "Swedish"
    },

    "Göteborg": {
        "country": "Sweden",
        "population": "600,000",
        "fact": "It is Sweden’s second-largest city and has a famous harbor.",
        "language": "Swedish"
    },

    "Malmö": {
        "country": "Sweden",
        "population": "350,000",
        "fact": "It is connected to Denmark by the Öresund Bridge.",
        "language": "Swedish"
    },

    "Kiruna": {
        "country": "Sweden",
        "population": "23,000",
        "fact": "It is known for the Icehotel and the northern lights.",
        "language": "Swedish"
    }
}

print("\n--- City Information ---")

for city, info in cities.items():
    print(f"\n{city}")

    for key, value in info.items():
        print(f"  {key.title()}: {value}")