import os as _os

PROJECT_PATH = r"C:\Users\User\PycharmProjects\your_bets"

def clear_db():
    remove_migrations()
    delete_db_file()

def remove_migrations():
    for path in specific_filepaths_recursive(PROJECT_PATH, "py"):
        if ("\\env\\" not in path) and ("migrations" in path) and ("__init__.py" not in path):
            _os.remove(path)

def delete_db_file():
    _os.remove(PROJECT_PATH + "\\db.sqlite3")

def filepaths_recursive(dir_path):
    return sum(([p+ "\\" + d for d in f] for p,b,f in _os.walk(dir_path)),[])

def specific_filepaths_recursive(dir_path, ext):
    return (fs for fs in filepaths_recursive(dir_path) if fs.endswith(ext))

clear_db()