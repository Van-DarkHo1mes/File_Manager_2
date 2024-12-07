import sys
from file_manager import FileManager
from drive_info_manager import DriveInfoManager

def main():
    action = 0
    manager = FileManager()

    while action != 6:
        print('''Выберите действие или тип файла:
    1 - Файл .txt;
    2 - Файл .json;
    3 - Файл .xml;
    4 - Файл .zip;
    5 - Посмотреть данные о дисках;
    6 - Выход;''')
        
        try:
            action = int(input('Введите число: ').strip() or '5')
        except ValueError:
            print('Введите корректное число от 1 до 6!')
            continue

        if action == 1:
            manager.work_with_file()
        elif action == 2:
            manager.work_with_json()
        elif action == 3:
            manager.work_with_xml()
        elif action == 4:
            manager.work_with_zip()
        elif action == 5:
            DriveInfoManager.show_system_info()
        elif action == 6:
            manager.close_zip()
            print("Выход из программы.")
        else:
            print('Введите число от 1 до 6!')

if __name__ == "__main__":
    main()
