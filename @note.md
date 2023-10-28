# 反向生成 sqlalchemy model

安装

```shell
pip install sqlacodegen
pip install pymysql (此前已安装，可以省略)
pip install sqlalchemy (此前已安装，可以省略)
```

使用

```shell
sqlacodegen --tables {表名} --outfile {输出文件名.py} mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8
```


# 在def error(*, code=404)中，*符号的作用是什么？ 

在函数定义中，单个星号（*）被用作一个特殊的语法，称为"参数解包"。在 `def error(*, code=404)` 函数定义中，它指定了一个只接受关键字参数的函数。

具体而言，使用单个星号（*）在函数定义中，可以将所有传递给函数的位置参数捕获到一个元组中，而不限制关键字参数的数量。这意味着在这个函数中，不允许传递任何位置参数，必须使用关键字参数来调用该函数。

在这个例子中，`error()`函数没有任何位置参数，只能使用关键字参数进行调用，并且它接受一个名为`code`的关键字参数，默认值是404。

下面是一些使用`error()`函数的示例：

```python
# 使用默认值404调用函数
error()

# 传递不同的错误代码
error(code=500)

# 不传递参数会引发TypeError
error(404)  # 这样的调用会引发错误
```

通过使用单个星号（*），我们可以明确规定函数只接受关键字参数，从而提高函数的可读性和灵活性。


# 安全漏洞检测工具

https://github.com/PyCQA/bandit

使用

```shell
pip install bandit
bandit -r path/to/your/code
```


# sqlacodegen 用法

```shell
sqlacodegen --noviews --outfile ./model.py mysql://root:root@127.0.0.1:3306/cooyun?charset=utf8
```

# 解决 VScode 的 powershell 中 conda activate xxx 无效的问题

只需要 win+X 打开power shell 然后输入 conda init powershell 回车就能解决