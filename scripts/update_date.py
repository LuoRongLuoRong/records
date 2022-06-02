import os
import time
import datetime

ignore_path = ['.git', 'scripts', 'style.txt', '_config.yml', 'pics']
relavant_file_type = ['txt', 'md']

def getFileType(file):
    for i in range (len(file)-1, -1, -1):
        if file[i] == '.':
            return file[i+1:]
    return "unknown"

def updateDate(path):
    today = str(datetime.date.today())
    
    # 查看文档的修改日期
    filemt = time.localtime(os.stat(path).st_mtime)
    hasUpdated = time.strftime("%Y-%m-%d", filemt) == today
    # 没有更新，直接跳过
    if not hasUpdated:
        return
    
    hasCreated = False
    updatedLine = -1    
    lines = []
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(lines)
        for i, line in enumerate(lines):
            # 1. 新创建的文档
            if line.startswith('> CREATED ON') or line.startswith('> 创建于'):
                hasCreated = True
            # 2. 新更新的文档
            if line.startswith('> UPDATED ON') or line.startswith('> 更新于'):
                updatedLine = i
    
    with open(path, "w", encoding="utf-8") as f:
        if not hasCreated:
            lines.append('\n> 创建于 ' + today + '\n\n> 更新于 ' + today) 
        else:
            lines[updatedLine] = '> 更新于 ' + today
            
        print(lines)    
        f.write(''.join(lines))

def getFiles(path, sep):    
    files = os.listdir(path)
    for file in files:
        if file in ignore_path:
            continue
        cur_path = path + os.path.sep + file
        if os.path.isdir(cur_path):
            print(sep, cur_path, True)
            getFiles(cur_path, sep + "  ")
        else:
            print(sep, cur_path, False)
            # 对符合条件的文件进行日期更新
            if getFileType(file) in relavant_file_type:
                updateDate(cur_path)
            

if __name__ == "__main__":
    print('HelloWorld')
    # 获取当前文件路径
    abs_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    par_path = os.path.abspath(os.path.dirname(abs_path) + os.path.sep + ".")
    # 获取项目根目录
    root_path = os.path.abspath(os.path.dirname(par_path) + os.path.sep + ".")
    
    # getFiles(root_path, "")
    # getFileType("a.txt")
    # updateDate(par_path + os.path.sep + "README.md")
    # updateDate(par_path + os.path.sep + "testcreated.txt")
    # updateDate(par_path + os.path.sep + "testupdate.txt")
    updateDate(par_path + os.path.sep + "testupdate2.txt")