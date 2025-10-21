import os

def get_unique_filename(path):
    base, ext = os.path.splitext(path)
    counter = 1
    unique_path = path
    
    while os.path.exists(unique_path):
        unique_path = f"{base}({counter}){ext}"
        counter += 1
    return unique_path