# Dictionaries are Other type of collection
# they store data as a key-value pair, we can use a dictionary as a small local DB
# we can declare a new dictionary with the dict() constructor and we access its data
# using the key names, we can store any python object as a dictionary value

bestWriters = dict()
bestWriters['Mexico'] = ['Rulfo', 'Paz', 'Fuentes']
bestWriters['Argentina'] = ['Lugones', 'Borges', 'Cortázar']
bestWriters['Cuba'] = ['Martí', 'Carpentier', 'Lezama']

print(bestWriters) #{'Mexico': ['Rulfo', 'Paz', 'Fuentes'], 'Argentina': ['Lugones', 'Borges', 'Cortázar'], 'Cuba': ['Martí', 'Carpentier', 'Lezama']}