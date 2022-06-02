# git 规范

## commit

分支：master分支，每个任务一个分支（注意.gitignore）

- fix：修复了bug
- docs：只修改了文档
- style：调整代码格式，未修改代码逻辑（比如修改空格、格式化、缺少分号等）
- refactor：代码重构，既没修复bug也没有添加新功能
- perf：性能优化，提高性能的代码更改
- test：添加或修改代码测试
- chore：对构建流程或辅助工具和依赖库（如文档生成等）的更改


## add

```shell
git rm -r --cached [被回收的文件]
```

## branch

```shell
# 切换到旧分支
git checkout oldBranch

# 创建并切换至新分支
git checkout -b luorong 

# 更新分支代码并提交
git add *
git commit -m "init newBranch"
git push origin newBranch

# 查看所有分支
git branch -a

# 查看当前使用分支（结果列表前面*号，代表当前使用的分支)
git branch
```

## 更新 commit 的信息

经常 commit 错误信息。如何修改？分为如下三种情况：

1. 刚刚 commit，还没有 push，使用 git commit --amend;
2. 刚刚push，要修改最近一个push的commit信息，使用git commit --amend；
3. 修改历史push的commit信息，使用git rebase -i HEAD~n【其中的n为记录数】，配合2中的命令





> 创建于 2022-06-02


> 更新于 2022-06-02