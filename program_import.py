import os

def save_data(data):
    path = os.path.join(os.getcwd(), "log.txt")
    with open(path, 'w') as fp:  
        fp.write(str(data))