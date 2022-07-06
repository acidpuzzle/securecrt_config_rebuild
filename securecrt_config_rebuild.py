import re
import os

path_f = [] 
for d, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ini') and file != '__FolderData__.ini' and f[-3:] != '.py':
            path = os.path.join(d,file) # формирование адреса 
            path_f.append(path) # добавление адреса в список 
            
def replace_in_file(file, username = None, password = None):
    try:
        with open(file) as file_in:
            text = file_in.read()
            text = re.sub(r'S:\"Username\"\S+', 'S:\"Username\"={}'.format(username), text)
            text = re.sub(r'S:\"Password V2\"\S+', 'S:\"Password V2\"={}'.format(password), text)
            text = re.sub(r'S:\"Color Scheme\"\S+', 'S:\"Color Scheme\"=Birds of Paradise', text)
            text = re.sub(r'S:\"Keyword Set\"\S+', 'S:\"Keyword Set\"=<None>', text)
        with open(file, "w") as file_out:
            file_out.write(text)
    except:
        pass


if __name__ == "__main__":
    username = ''
    password = ''

    i = len(path_f) - 1
    while i >= 0:
        file = path_f[i]
        replace_in_file(file)
        #os.rename(file, file[:-4]+"_"+ re.search(r'[а-яА-ЯёЁ]+', file).group(0) + '.ini') # МФЦ только. переименует файл конфигурации, добавит имя папки в конце имени файла.
        print(i, file)
        i = i - 1