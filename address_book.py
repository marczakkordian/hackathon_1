contact_list = [['Olaf', 'Skiba', '123456789'], ['Krzysztof', 'Socha', '123456789'],
                ['Henryka', 'Sobolewska', '123456789'], ['Gabriel', 'Markowski', '123456789'],
                ['Sylwester', 'Urbański', '123456789'], ['Aleks', 'Madej', '123456789'], ]


def show_program_intro():
    print('''Welcome in Address Book v1.0 program! Menu options: 
    \n[1] display all contacts | [2] add new contact | [3] update contact | [4] remove contact | [5] remove all data | [6] command list | [7] quit\n''')


def show_command_list():
    print('''Available commands in the program: 
    \n[1] display all contacts | [2] add new contact | [3] update contact | [4] remove contact | [5] remove all data | [6] command list | [7] quit\n''')


def show_all_contacts() :
    print('---> Show all contacts  is open <----')
    counter = len(contact_list)
    if counter > 0:
        for index in range(counter) :
            print(f'[{index + 1}]', ' || '.join(contact_list[index]))
    else:
        print('Contact list is empty! There is nothing to show...')
    print('---> Show all contacts is closed <----')


def add_contact() :
    print('---> Add contact is open <----')
    name = input('Enter name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone number: ')
    contact_list.append([name, last_name, phone_number])
    print('---> Add contact is closed <----')


def update_contact():
    print('---> Update contact is open <----')
    user_index = int(input('Please type number of row to update: '))
    index = user_index - 1
    # selected row
    print(f'[{index + 1}]', ' || '.join(contact_list[index]))
    user_option = int(input('''Select what you want change: Name[1] | LastName[2] | Phone number[3]: '''))
    user_option = user_option - 1
    if user_option == 0:
        contact_list[index][user_option] = input('Enter new name: ')
        print('Update successful!\n', f'[{index + 1}]', ' || '.join(contact_list[index]))
    elif user_option == 1:
        contact_list[index][user_option] = input('Enter new lastname: ')
        print('Update successful!\n', f'[{index + 1}]', ' || '.join(contact_list[index]))
    elif user_option == 2:
        contact_list[index][user_option] = input('Enter new phone number: ')
        print('Update successful!\n', f'[{index + 1}]', ' || '.join(contact_list[index]))
    else:
        print('Please select correct option[1-3]')
    print('---> Update contact is closed <----')


def remove_contact() :
    print('---> Remove contact is open <----')
    user_index = int(input('Please type number of row to remove: '))
    index = user_index - 1
    print('Row deleted:', contact_list.pop(index))
    print('---> Remove contact is closed <----')


def remove_all() :
    print('---> Remove all contact data is open <----')
    contact_list.clear()
    print('All data has been removed and contact list is empty')
    print('---> Remove all contact data is closed <----')


# main code
show_program_intro()
while True:
    usr_option = int(input('>>> Please enter a number of function which you need: '))
    usr_option > 0 and usr_option <= 7
    if usr_option == 7:
        break
    elif usr_option == 1:
        show_all_contacts()
    elif usr_option == 2:
        add_contact()
    elif usr_option == 3:
        update_contact()
    elif usr_option == 4:
        remove_contact()
    elif usr_option == 5:
        remove_all()
    elif usr_option == 6:
        show_command_list()
    else:
        print('Please select correct option [1-6]: ')
        continue
