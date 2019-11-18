## git
git clone 之后需要配置后push才不用输入密码：git remote set-url origin git@github.com:zhouzhaoxin/linux-example.git
```
vim .git-credentials
输入https://{username}:{password}@github.com
git config --global credential.helper store
此时.gitconfig会多出helper=store
```

#### linux 配置
#### linux 理解
`c`语言程序由内核调用`exec`函数执行，这个函数可以从内核中获取需要执行的`main`函数参数数量以及参数地址列表,`main`函数的原型如下：
```
int main(int argc, char *argv[])
```
有八种方法可以终止进程
1. 从`main`函数中返回
2. 调用`exit`函数
3. 调用`_exit`或者`_Exit`函数
4. 从程序开始后启动的最后一个线程返回
5. 在最后一个线程中调用`pthread_exit`

6. 调用`abort`
7. 接受到终止信号
8. 最后一个线程响应终止请求

执行`_exit`和`_Exit`会从内核直接返回，而`exit`函数则会先清理进程中的资源（比如文件的I/O流）后再返回,这三个方法都有个名为`exit_status`的参数,大多数`linux shell`都提供了查询进程`exit_status`的方法，比如`ubuntu`可以使用`echo $?`获取上一个终止的进程状态码.需要注意的是，若以下三种情况出现，会导致进程终止号为`undefined`
1. 调用以上三种终止进程的函数时选择不传递终止号码参数
2. `main`函数执行后，没有给返回值
3. `main`函数没有声明返回值为`int`
注意：如果`main`函数声明了返回值但是没有正确返回，终止号码为`0`，在`main`方法中调用`exit(0);`和`return(0);`是一样的



