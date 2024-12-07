import json
import os
from file_handler import FileHandler
from person import Person

class JsonHandler(FileHandler):
    file_extension = 'json'

    def __init__(self, name):
        super().__init__(name)
    
    def write_to_file(self, content):
        if not isinstance(content, Person):
            raise ValueError("Content must be of type Person")

        json_string = json.dumps(content.to_dict()) + "\n"
        super().write_to_file(json_string)
    
    def print_file_content(self):
        if not os.path.exists(self._file_path):
            print('Ошибка! Создайте сначала файл.')
            return

        try:
            with open(self._file_path, 'r') as file:
                content = file.read().strip()
            list_string = content.split('\n')

            list_persons = [Person.from_dict(json.loads(element)) for element in list_string if element]

            print('Данные файла:\n')
            for person in list_persons:
                print(person)
        except Exception as e:
            print(f'Ошибка: {e}')
