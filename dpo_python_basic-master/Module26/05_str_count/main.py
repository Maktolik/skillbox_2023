import os



def get_start_directory(home: str = None):
    """
    Если директория не указана или не найдена, то берём текущую.
    Args:
        home: str - Проверка директории
    """
    if home is None:
        return os.getcwd()
    if os.path.isdir(home):
        return home
    else:
        print('Указанная вами папка не найдена.')
        return False


def get_file_list(home: str) -> str:
    """
    Формирование списка файлов
    :home: str - С какой директории начать
    :root: str - путь
    :dir: str - директория
    files: str - файлы
    """
    for root, dir, files in os.walk(home):
        for file in files:
            if file.endswith(".py"):
                yield os.path.join(root, file)

"""расчет количества строк, если пустая - пропуск"""
line_counter = 0
directory = get_start_directory('/skill/Module26/')
if isinstance(directory, str):
    file_list = list(get_file_list(directory))
    if len(file_list) > 0:
        for file in file_list:
            try:
                cur_file = open(file, "r")
                local_count = 0
                for line in cur_file:
                    if line != '\n' or not line.startswith('"') or not line.startswith('#'):
                        local_count += 1
                print(f'{cur_file.name} - {local_count} строки')
                line_counter += local_count
                cur_file.close()
            except:
                continue
        print("Всего строк  - ", line_counter)