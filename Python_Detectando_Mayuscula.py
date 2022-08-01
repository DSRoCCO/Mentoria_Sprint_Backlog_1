"""Ejemplo de resultado"""
def find_upper(person1, person2):
    persons = [person1, person2]
    for person in persons:
        if person['last_name'][0] == person['last_name'][0].upper():
            result = {person['last_name'][0]: person['last_name']}
    return result

#person1 = {"name": "candy", "last_name": "Feder", "age": 34}
#person2 = {"name": "Manuel", "last_name": "martínes", "age": 21}

#print(find_upper(person1, person2))
#>> {'F': 'Feder'}
