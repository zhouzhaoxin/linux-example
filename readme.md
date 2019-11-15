## git
git clone 之后需要配置后push才不用输入密码：git remote set-url origin git@github.com:zhouzhaoxin/linux-example.git
```
vim .git-credentials
输入https://{username}:{password}@github.com
git config --global credential.helper store
此时.gitconfig会多出helper=store
git branch xxx 添加分支
```
linux 配置
linux 理解
