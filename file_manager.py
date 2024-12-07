import re
from file_handler import FileHandler
from json_handler import JsonHandler
from xml_handler import XmlHandler
from zip_handler import ZipHandler
from person import Person

class FileManager:
    def __init__(self):
        self.file_handler = None
        self.json_handler = None
        self.xml_handler = None
        self.zip_handler = None

    @staticmethod
    def get_file_parameter():
        while True:
            name = input('Введите название файла (только буквы): ').strip()
            if re.match(r'^[a-zA-Zа-яА-Я]+$', name):
                return name
            else:
                print('Ошибка: название должно содержать только буквы.')

    @staticmethod
    def get_file_content(condition):
        if condition == 0:
            while True:
                data = input('Введите данные для записи в файл (только буквы): ').strip()
                if re.match(r'^[a-zA-Zа-яА-Я]+$', data):
                    return data
                else:
                    print('Ошибка: данные должны содержать только буквы.')

        elif condition == 1:
            while True:
                first_name = input('Введите имя (только буквы): ').strip()
                if re.match(r'^[a-zA-Zа-яА-Я]+$', first_name):
                    break
                else:
                    print('Ошибка: имя должно содержать только буквы.')

            while True:
                second_name = input('Введите фамилию (только буквы): ').strip()
                if re.match(r'^[a-zA-Zа-яА-Я]+$', second_name):
                    break
                else:
                    print('Ошибка: фамилия должна содержать только буквы.')

            age = int(input('Введите возраст: ').strip() or 0)
            return Person(first_name, second_name, age)

        elif condition == 2:
            element_name = input('Введите имя элемента (только буквы): ').strip()
            element_content = input('Введите содержание элемента: ').strip()
            return (element_name, element_content)

    def choose_action(self):
        print('''Выберите действие с файлом:
    1 - Создать файл;
    2 - Записать в файл;
    3 - Прочитать файл;
    4 - Удалить файл;
    5 - Добавить файл в архив;
    6 - Назад;''')
        return int(input('Введите число: ').strip() or 6)

    def create_file(self):
        file_name = self.get_file_parameter()
        self.file_handler = FileHandler(file_name)
        self.file_handler.create_file()

    def create_json_file(self):
        file_name = self.get_file_parameter()
        self.json_handler = JsonHandler(file_name)
        self.json_handler.create_file()

    def create_xml_file(self):
        file_name = self.get_file_parameter()
        self.xml_handler = XmlHandler(file_name)
        self.xml_handler.create_file()

    def write_to_file(self, handler):
        if not handler or not handler.file_exists():
            print("Создайте сначала файл!")
            return

        condition = 0
        if isinstance(handler, JsonHandler):
            condition = 1
        elif isinstance(handler, XmlHandler):
            condition = 2

        content = self.get_file_content(condition)
        handler.write_to_file(content)

    def print_content(self, handler):
        if not handler or not handler.file_exists():
            print("Создайте сначала файл!")
            return
        handler.print_file_content()

    def remove_file(self, handler):
        if not handler or not handler.file_exists():
            print("Создайте сначала файл!")
            return
        handler.remove_file()

    def create_zip_file(self):
        if self.zip_handler and self.zip_handler.file_exists():
            self.close_zip()

        file_name = self.get_file_parameter()
        self.zip_handler = ZipHandler(file_name)

    def write_to_zip_file(self, handler):
        if not handler or not handler.file_exists():
            print("Создайте сначала файл!")
            return

        if not self.zip_handler or not self.zip_handler.file_exists():
            print("Создайте сначала zip-файл!")
            return

        self.zip_handler.add_to_zip(handler.file_path)

    def close_zip(self):
        if self.zip_handler and self.zip_handler.file_exists():
            self.zip_handler.close_zip()

    def print_zip_file(self):
        if not self.zip_handler or not self.zip_handler.file_exists():
            print("Создайте сначала zip-файл!")
            return
        self.zip_handler.print_file_content()

    def remove_zip_file(self):
        if not self.zip_handler or not self.zip_handler.file_exists():
            print("Создайте сначала zip-файл!")
            return
        self.zip_handler.remove_file()

    def work_with_file(self):
        action = 0
        while action != 6:
            action = self.choose_action()
            if action == 1:
                self.create_file()
            elif action == 2:
                self.write_to_file(self.file_handler)
            elif action == 3:
                self.print_content(self.file_handler)
            elif action == 4:
                self.remove_file(self.file_handler)
            elif action == 5:
                self.write_to_zip_file(self.file_handler)

    def work_with_json(self):
        action = 0
        while action != 6:
            action = self.choose_action()
            if action == 1:
                self.create_json_file()
            elif action == 2:
                self.write_to_file(self.json_handler)
            elif action == 3:
                self.print_content(self.json_handler)
            elif action == 4:
                self.remove_file(self.json_handler)
            elif action == 5:
                self.write_to_zip_file(self.json_handler)

    def work_with_xml(self):
        action = 0
        while action != 6:
            action = self.choose_action()
            if action == 1:
                self.create_xml_file()
            elif action == 2:
                self.write_to_file(self.xml_handler)
            elif action == 3:
                self.print_content(self.xml_handler)
            elif action == 4:
                self.remove_file(self.xml_handler)
            elif action == 5:
                self.write_to_zip_file(self.xml_handler)

    def work_with_zip(self):
        action = 0
        while action != 4:
            print('''Выберите действие с zip-файлом:
    1 - Создать файл;
    2 - Разархивировать файл;
    3 - Удалить файл;
    4 - Назад;''')
            action = int(input('Введите число: ').strip() or 4)
            if action == 1:
                self.create_zip_file()
            elif action == 2:
                self.print_zip_file()
            elif action == 3:
                self.remove_zip_file()
