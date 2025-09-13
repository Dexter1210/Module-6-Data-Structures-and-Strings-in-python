marks_dictionary = {
    'Alice': 95,
    'Bob': 93,
    'Marc': 75,
    'Seth': 38
}

name = input('Enter student name')
if marks_dictionary.get(name) is None:
    print('Student not found')
else:
    print(name+"'s marks: "+str(marks_dictionary[name]))

