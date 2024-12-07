import os
import xml.etree.ElementTree as ET
from file_handler import FileHandler

class XmlHandler(FileHandler):
    file_extension = 'xml'

    def __init__(self, name):
        super().__init__(name)
    
    def create_file(self):
        if os.path.exists(self._file_path):
            print('Ошибка! Такой файл уже есть.')
            return

        try:
            os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
            root = ET.Element("root")
            tree = ET.ElementTree(root)
            tree.write(self._file_path, encoding="utf-8", xml_declaration=True)
            print('Файл успешно создан!')
        except Exception as e:
            print(f'Ошибка: {e}')

    def write_to_file(self, content):
        if not isinstance(content, tuple) or len(content) != 2:
            raise ValueError("Content must be a tuple with two string elements")

        element_name, element_content = content
        try:
            tree = ET.parse(self._file_path)
            root = tree.getroot()

            new_element = ET.Element(element_name)
            new_element.text = element_content
            root.append(new_element)

            tree.write(self._file_path, encoding="utf-8", xml_declaration=True)
            print("Запись в файл успешно произведена!")
        except Exception as e:
            print(f'Ошибка: {e}')
