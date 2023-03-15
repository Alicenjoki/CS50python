people = [
    {"name":"Alice", "Reside":"Narok"},
    {"name":"Collins", "Reside":"Nairobi"},
    {"name":"Mike", "Reside":"Kisumu"}
]

people.sort (key=lambda person:person["name"])
print(people)