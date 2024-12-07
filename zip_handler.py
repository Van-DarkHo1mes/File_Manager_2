import os
import zipfile

class ZipHandler:
    _file_extension = 'zip'
    _mount_point = 'D:/files'

    def __init__(self, name):
        self._zip_path = os.path.join(self._mount_point, f"{name}.{self._file_extension}")
        self._is_closed = False
        self._encoder = zipfile.ZipFile(self._zip_path, 'w', zipfile.ZIP_DEFLATED)
        print(f"Создан zip-файл: {self._zip_path}")

    def add_to_zip(self, file_path):
        if self._is_closed:
            print('Ошибка! Создайте сначала zip-файл.')
            return

        if not os.path.exists(file_path):
            print('Ошибка! Файл для добавления не существует.')
            return

        try:
            self._encoder.write(file_path, arcname=os.path.basename(file_path))
            print(f'Файл успешно добавлен в архив: {file_path}')
        except Exception as e:
            print(f'Ошибка при добавлении файла в архив: {e}')

    def close_zip(self):
        if not self._is_closed:
            self._encoder.close()
            self._is_closed = True
            print(f"Zip-файл {self._zip_path} закрыт")

    def print_file_content(self):
        if not os.path.exists(self._zip_path):
            print('Ошибка! Создайте сначала zip-файл.')
            return

        self.close_zip()
        try:
            with zipfile.ZipFile(self._zip_path, 'r') as archive:
                for file_info in archive.infolist():
                    print(f'Файл в архиве: {file_info.filename}')
                    print(f'Размер файла: {file_info.file_size} байт')

                    extracted_path = os.path.join(self._mount_point, f"extracted_{file_info.filename}")
                    archive.extract(file_info.filename, path=self._mount_point)
                    os.rename(os.path.join(self._mount_point, file_info.filename), extracted_path)
                    print(f'Файл {file_info.filename} успешно извлечён и сохранён как {extracted_path}')
        except Exception as e:
            print(f'Ошибка при чтении содержимого zip-файла: {e}')

    def remove_file(self):
        if not os.path.exists(self._zip_path):
            print('Ошибка! Создайте сначала zip-файл.')
            return

        try:
            self.close_zip()
            os.remove(self._zip_path)
            print(f'Zip-файл {self._zip_path} удален!')
        except Exception as e:
            print(f'Ошибка при удалении zip-файла: {e}')
