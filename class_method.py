
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    @classmethod
    def import_data(cls, data):

        students = []
        for row in data:
            # Create the Student object taking data from data list
            student = cls(row['name'], row['id'])
            #append the data to the list
            students.append(student)

        return students



data = [
    {
        'name': 'Akkas',
        'id': 12
    },
    {
        'name': 'Timmy',
        'id': 23
    }
]

stu = Student.import_data(data)
print(stu)
print(stu[0].name)
        