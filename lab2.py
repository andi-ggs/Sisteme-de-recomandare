import random
import re
import string
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import (
    AddUser,
    AddUserProperty,
    SetUserValues
)

client = RecombeeClient(
    'andiggs-dev',
    '9evxv2Jw8v7w0IgafnKu86B3DOJMym32qZgbDeaAPFRNXksZWNeWiFxEme0mTSVz',
    region=Region.EU_WEST
)

properties = {
    'firstName': 'string',
    'lastName': 'string',
    'email': 'string',
    'homeCountry': 'string',
    'occupation': 'string',
    'travelPreference': 'string',  # preferință: exotic, cultural, urban, etc.
    'budget': 'double'             # buget mediu pentru o vacanță
}

from recombee_api_client.api_requests import AddUserProperty
for prop, prop_type in properties.items():
    try:
        client.send(AddUserProperty(prop, prop_type))
    except Exception as e:
        print(f"Proprietatea '{prop}' există deja sau a apărut o eroare: {e}")

first_names = ["Andrei", "Maria", "Ioana", "Vlad", "Elena", "Mihai", "Raluca", "Cristian", "Oana", "Gabriel"]
last_names = ["Popescu", "Ionescu", "Georgescu", "Marin", "Stan", "Dumitrescu", "Petrescu", "Tudor", "Radu", "Ilie"]
occupations = ["Student", "Profesor", "Programator", "Medic", "Antreprenor", "Fotograf", "Jurnalist", "Designer"]
countries = ["Romania", "Franta", "Germania", "Italia", "Spania", "Grecia", "Portugalia", "Olanda", "Polonia", "Suedia"]
travel_preferences = ["exotic", "cultural", "urban", "mountain", "beach", "historic", "gastronomic"]

user_count = 30
from recombee_api_client.api_requests import AddUser, SetUserValues

for i in range(1, user_count + 1):
    user_id = f"user_{i}"

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    country = random.choice(countries)
    occupation = random.choice(occupations)
    preference = random.choice(travel_preferences)
    budget = round(random.uniform(500, 5000), 2)

    client.send(AddUser(user_id))
    client.send(SetUserValues(user_id, {
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'homeCountry': country,
        'occupation': occupation,
        'travelPreference': preference,
        'budget': budget
    }, cascade_create=True))

print(f"{user_count} utilizatori generați și adăugați în Recombee cu succes!")