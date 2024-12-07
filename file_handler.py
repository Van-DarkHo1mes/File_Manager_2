import os

class FileHandler:
    def __init__(self, name):
        self.file_path = f"{name}.txt"

    def create_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write("")
            print(f"Файл {self.file_path} успешно создан!")
        else:
            print(f"Файл {self.file_path} уже существует.")

    def file_exists(self):
        return os.path.exists(self.file_path)

    def write_to_file(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)
        print(f"Данные записаны в файл {self.file_path}.")

    def print_file_content(self):
        if self.file_exists():
            with open(self.file_path, 'r') as file:
                print(file.read())
        else:
            print("Файл не найден.")

    def remove_file(self):
        if self.file_exists():
            os.remove(self.file_path)
            print(f"Файл {self.file_path} удален.")
        else:
            print("Файл не найден.")
