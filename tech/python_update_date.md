# Python 自动更新文件夹内文件的信息



代码功能主要是：遍历获取根目录下的所有文件，更新被创建和被修改的文件的`created time` 和 `updated time`。



主要知识点：

- `for i in range (len(file)-1, -1, -1)` 倒序遍历
- `filemt = time.localtime(os.stat(path).st_mtime)` 查看文件的修改时间
- open file 的时候，mode 非常重要。
- `os.listdir(path)` 获取文件夹下所有的文件。
- `os.path.isdir(cur_path)` 判断文件是否是文件夹




```python
import os
import time
import datetime

# 一些忽略的路径
ignore_path = ['.git', 'scripts', 'style.txt', '_config.yml', 'pics']
# 想要修改信息的文件类型
relavant_file_type = ['txt', 'md']

# 实现方式比较简单，是倒序遍历文件名，获得点号后面的字符串。
def getFileType(file):
    for i in range (len(file)-1, -1, -1):
        if file[i] == '.':
            return file[i+1:]
    return "unknown"


# 核心逻辑是
# 1. 检查文件是否是 today 更新：是则2，不是则结束。
# 2. 检查文件是否是 today 创建：是则3，不是则4.
# 3. 同时添加 "created" 和 "updated"
# 4. 添加 "updated"

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
    
    getFiles(root_path, "")
    
```

> 创建于 2022-06-02


> 更新于 2022-06-02