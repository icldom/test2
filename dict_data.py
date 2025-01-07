data = {
    "Albus": "Brumbál",
    "Alice": {
        "age": 29,
        "hobbies": ["reading", "cycling", "gardening"],
        "contacts": {
            "email": "alice@example.com",
            "phone": "555-1234"
        }
    },
    "Bob": {
        "age": 34,
        "hobbies": ["hiking", "chess", "coding"],
        "contacts": {
            "email": "bob@example.com",
            "phone": "555-5678"
        }
    },
    "Charlie": {
        "age": 25,
        "hobbies": ["photography", "traveling", "music"],
        "contacts": {
            "email": "charlie@example.com",
            "phone": "555-9101"
        }
    },
}

print(f"Získejte hodnotu 25: {data['Charlie']['age']}")
print(f"Získejte hodnotu Brumbál: {data['Albus']}")
print(f"Získejte hodnotu 555-1234: {data['Bob']['contacts']['phone']}")
print(f"Získejte hodnotu reading: {data['Alice']['hobbies'][0]}")
print(f"Získejte hodnotu traveling: {''}")
print(f"Získejte hodnotu bob@example.com: {''}")
print(f"Získejte hodnotu 29: {''}")