# main函数是如何执行的
main 函数的原型为：
```
int main(int argc, char *argv[])
```
argc是命令行参数的数量，argv是命令行参数数组的指针

内核通过`exec`函数执行`C`程序，这个函数会从内核中获取参数传给`main`函数
