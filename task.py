from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise ValueError(f"Phone number {value} was not added. It must be 10 digits")
        else:
            super().__init__(value)


class Record:
    def __init__(self, contact_name):
        self.name = Name(contact_name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, contact_number):
        self.phones.append(Phone(contact_number))

    def edit_phone(self, old_number: str, new_number: str):
        matches = [phone for phone in self.phones if phone.value == old_number]

        if matches:
            matches[0].value = new_number
        else:
            print(f"Phone {old_number} not found")

    def find_phone(self, contact_number: str):
        found_phones = [phone for phone in self.phones if phone.value == contact_number]
        return found_phones[0].value


class AddressBook(UserDict):

    def __str__(self):
        return "\n".join(f"{value}" for key, value in self.data.items())

    def add_record(self, record_to_add):
        self[record_to_add.name.value] = record_to_add

    def find(self, contact_name: str):
        if contact_name in self.data:
            return self[contact_name]
        else:
            print(f"Contact {contact_name} not found in Address Book")

    def delete(self, contact_name: str):
        if contact_name in self.data:
            del self[contact_name]
            print(f"Contact {contact_name} deleted")
        else:
            print(f"Contact {contact_name} not found")
