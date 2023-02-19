import os


def import_folder(path: str):
    surface_list = []

    full_path = os.path.join(os.getcwd(), path)
    print(full_path)

    for folder in os.walk(full_path):
        print(folder)

    return surface_list
