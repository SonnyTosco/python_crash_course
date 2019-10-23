def build_person(first_name, last_name, age=28):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
musician2 = build_person('jimi', 'hendrix')
print(musician)
print(musician2)
