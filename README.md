# 集训队作业提交工具
不是集训队就不用看了= =

这个玩意儿是用来把atcoder上AC的代码提交tuoj的。

依赖：python以及必要的运行库、chromedriver。

配置：在grab.py中填写**atcoder** user_name和pass_word，在submit.py里填写**tuoj**的url、un和ps。

用法：

首先运行grab.py，会抓取下atcoder的代码，形如`arc233_a.cpp`。

然后运行renamer.py，会把代码对应上题目编号，生成`tuoj编号.cpp`之类的代码。

然后运行submit.py，就可以提交了。