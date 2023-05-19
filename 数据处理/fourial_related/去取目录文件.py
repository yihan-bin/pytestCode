import os
file_dir='d:/'
file_name=os.listdir(file_dir)
with open('../数据/11.txt', 'a') as f:
    for name in file_name:
        if '.' in name:
            f.writelines(name+'\n')
            print(name)
    f.close()

