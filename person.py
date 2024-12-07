class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get('firstName'),
            second_name=data.get('secondName'),
            age=data.get('age')
        )

    def to_dict(self):
        return {
            'firstName': self.first_name,
            'secondName': self.second_name,
            'age': self.age
        }

    def __str__(self):
        return f"Person:\n имя: {self.first_name}\n фамилия: {self.second_name}\n возраст: {self.age}\n"
