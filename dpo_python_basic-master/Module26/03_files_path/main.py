import os


def search_path(home: str, search: str):
    for dir_path, dir_names, filenames in os.walk(home):
        for cur_dir in dir_names:
            if cur_dir == search:
                return os.path.join(dir_path, cur_dir)
    return False


def gen_files_path(home: str, search: str):
    result = search_path(home, search)
    file_list = []
    if isinstance(result, str):
        with os.scandir(result) as files:
            for file_name in files:
                if not file_name.name.startswith('.') and file_name.is_file():
                    file_list.append(os.path.join(result, file_name.name))
    return file_list


print('\n'.join(gen_files_path('/skill/', 'Module26')))