with open('contacts.csv', 'r') as person:
    rows = person.read().split('\n')

headers = rows[0]
header_list = headers.split(',')


person_list = []
for person in rows[1:]:
    row_list = person.split(',')
    person_dict = {}
    for i in range(len(row_list)):
        person_dict[header_list[i]] = row_list[i]
    
    person_list.append(person_dict)

print(f"person_list {person_list}")


user_name = input("Enter a name: ")
user_color = input("Enter color: ")
user_fruit = input("Enter fruit: ")


user_list = [user_name, user_color, user_fruit]
user_dict = {}
for i in range(len(user_list)):
    user_dict[header_list[i]] = user_list[i]
person_list.append(user_dict)

print(f"Updated list:\n{person_list}")


user_retrieve = input("Enter a name you would like to retrieve: ")
for person_dict in person_list:
    if person_dict['Name'] == user_retrieve:
        break

print(person_dict: {'person_dict'})


user_update_person = input("Which name would you like to update? ")
user_update_attribute = input("Which attribute would you like to update? ")
user_update_new_attribute = input("And what would you like to change it to? ")
for person_dict in person_list:
    if person_dict['person'] == user_update_person:
        break
person_dict[user_update_attribute] = user_update_new_attribute

print(person_list)

#delete a record
user_remove_person = input("Which person would you like to remove? ")
for person_dict in person_list:
    if person_dict['person'] == user_remove_person:
        break
person_list.remove(person_dict)

print(person_list)