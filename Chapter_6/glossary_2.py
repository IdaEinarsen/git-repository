# 6.4 glossary 2

glossary2 = {
    "list": "A collection of items",
    "loop": "Repeats a block of code multiple times",
    "if statement": "A conditional test that runs code if a condition is true.",
    "dictionary": " A collection of key-value's",
    "string": "A sequence of characters inside quotes.",
    "integer": "A whole number",
    "float": "A number with decimals",
    "comment": "Ignored notes in code",
    "variable": "A name that stores a value",
    "tuple": "An immutable collection of items"
}

for term, meaning in glossary2.items():
    print(f"\n{term.title()}:")
    print(f"  {meaning}")



