# 程序员必知必会命令

### linux

- [screen](https://linuxize.com/post/how-to-use-linux-screen/)
  - 新建并进入：`screen`
  - 进入已经建好的 screen：`screen -r session_name`
  - 查看：`screen -ls`
  - 新建、命名并进入：`screen -S session_name`
    - `Ctrl+a` `c` Create a new window (with shell).
    - `Ctrl+a` `"` List all windows.
    - `Ctrl+a` `0` Switch to window 0 (by number).
    - `Ctrl+a` `A` Rename the current window.
    - `Ctrl+a` `S` Split current region horizontally into two regions.
    - `Ctrl+a` `|` Split current region vertically into two regions.
    - `Ctrl+a` `tab` Switch the input focus to the next region.
    - `Ctrl+a` `Ctrl+a` Toggle between the current and previous windows
    - `Ctrl+a` `Q` Close all regions but the current one.
    - `Ctrl+a` `X` Close the current region.
  - 退出：`Ctrl+a` `d`
  - 删除：`screen -X -S id quit`


- 强制删除文件夹：`rm -rf [文件夹名称]`

- 下载文件：`wget [文件URL]`

- 修改单个文件名：`mv [旧文件名] [新文件名]`

- 当前目录下文件夹的大小：`du -h -d 1`

- 软链接：`ln -s [文件夹真实地址] [文件夹软链接地址]`

  ​

### pip

conda 可以代替 pip 进行 Python 库的管理。

- 将 txt 文件中的环境进行安装：`pip install -r requirements.txt` 
- 重装库：`pip uninstall [库名称]` 

### conda

- 查看 conda 环境：`conda list -e`
- 新建 conda 环境：`conda create --name [环境名称] python=3.7` 
- 启动 conda 环境：`conda activate [环境名称]`
- 删除 conda 环境：`conda remove -n [环境名称] --all`
- 删除虚拟环境中的包：`conda remove --name [环境名称] [包的名称] `

### sql



### neo4j 

 Cypher

- 删除所有数据：match (n) detach delete n




### Notebook

Windows: 安装 Anaconda. 










