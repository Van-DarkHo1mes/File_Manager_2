import subprocess
import re

class DriveInfoManager:
    @staticmethod
    def show_system_info():
        drives_info = DriveInfoManager.get_drives_on_windows()
        for drive in drives_info:
            print(drive)

    @staticmethod
    def get_drives_on_windows():
        try:
            result = subprocess.run(
                ['wmic', 'logicaldisk', 'get', 'caption,filesystem,freespace,size,volumename'],
                capture_output=True,
                text=True,
                shell=True
            )
            output = result.stdout

            lines = [line.strip() for line in output.splitlines() if line.strip()]
            if len(lines) < 2:
                return ['No logical disks found']

            headers = re.split(r'\s+', lines[0].strip())
            drives_data = []

            for line in lines[1:]:
                drive_info = re.split(r'\s+', line.strip())
                drive_map = {}

                for i in range(min(len(headers), len(drive_info))):
                    drive_map[headers[i]] = drive_info[i]

                drives_data.append(DriveInfoManager.format_drive_info(drive_map))

            return drives_data
        except Exception as e:
            return [f"Error retrieving drive information: {e}"]

    @staticmethod
    def format_drive_info(drive_info):
        caption = drive_info.get('Caption', 'Unknown')
        volume_name = drive_info.get('VolumeName', 'Unknown')
        file_system = drive_info.get('FileSystem', 'Unknown')
        free_space = drive_info.get('FreeSpace', 'Unknown')
        size = drive_info.get('Size', 'Unknown')

        return f'''
Диск: {caption}
Метка тома: {volume_name}
Файловая система: {file_system}
Свободное место: {DriveInfoManager.format_bytes(free_space)}
Общий размер: {DriveInfoManager.format_bytes(size)}
'''

    @staticmethod
    def format_bytes(bytes_str):
        if not bytes_str or bytes_str == 'Unknown':
            return 'Unknown'
        size = int(bytes_str)

        suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        i = 0
        adjusted_size = float(size)

        while adjusted_size >= 1024 and i < len(suffixes) - 1:
            adjusted_size /= 1024
            i += 1
        return f"{adjusted_size:.2f} {suffixes[i]}"
