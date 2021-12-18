class Contact:
    def __init__(self, id, name, surname, birth, profession):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth = birth
        self.profession = profession

    def __str__(self):
        return f'ID:{self.id} - {self.name} {self.surname}\n birth: {self.birth}, profession: {self.profession}'


contact1 = Contact('033', 'Alfredo', 'Hugecoco', '1990.03.03', 'Fashion')
print(contact1)

contact2 = Contact('228', 'Marry', 'Jane', '1996.04.20', 'Rap Artist')
print(contact2)