import os
import shutil

def create_item(path, is_file=True):
    try:
        if is_file:
            open(path, 'a').close()
            print(f"Файл '{path}' успешно создан.")
        else:
            os.makedirs(path)
            print(f"Папка '{path}' успешно создана.")
    except Exception as e:
        print(f"Ошибка при создании { 'файла' if is_file else 'папки' } '{path}': {e}")

def delete_item(path, is_file=True):
    try:
        if is_file:
            os.remove(path)
            print(f"Файл '{path}' успешно удален.")
        else:
            shutil.rmtree(path)
            print(f"Папка '{path}' успешно удалена.")
    except Exception as e:
        print(f"Ошибка при удалении { 'файла' if is_file else 'папки' } '{path}': {e}")

def move_item(source, destination):
    try:
        shutil.move(source, destination)
        print(f"{ 'Файл' if os.path.isfile(source) else 'Папка' } '{source}' успешно перемещен в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при перемещении { 'файла' if os.path.isfile(source) else 'папки' } '{source}': {e}")

def copy_item(source, destination):
    try:
        if os.path.isfile(source):
            shutil.copy2(source, destination)
            print(f"Файл '{source}' успешно скопирован в '{destination}'.")
        else:
            shutil.copytree(source, destination)
            print(f"Папка '{source}' успешно скопирована в '{destination}'.")
    except Exception as e:
        print(f"Ошибка при копировании { 'файла' if os.path.isfile(source) else 'папки' } '{source}': {e}")
