# djcelery-example
django-celery 使用方法demo(官方demo不完全)，支持celery 调用ansible api。

### feature
- 支持django admin页面查看日志
- 支持页面配置crotab任务
- 支持celery 调用ansible api接口

### Install
```bash
# 安装并启动redis
$ sudo yum intall redis supervisor -y && sudo service redis start

# 下载项目
$ git clone https://github.com/dengshaochun/djcelery-example.git && cd proj

# 安装依赖包(需先安装pipenv)
$ pipenv install . && pipenv install -r requirements.txt

# 初始化数据库
$ pipenv run python manage.py migrate

# 创建super user
$ pipenv run python manage.py createsuperuser

# 启动superviosr
$ supervisord -c djcelery.ini && supervisorctl -c djcelery.ini status

# 启动django web(浏览器地址 http://localhost:9009)
$ pipenv run python manage.py runserver 0.0.0.0:9009
```

### Python shell 提交任务
```bash
$ pipenv run python manage.py shell
Python 2.7.5 (default, Aug  4 2017, 00:39:18)
Type "copyright", "credits" or "license" for more information.

IPython 5.6.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from demo.tasks import mul

In [2]: p = mul.delay(5, 6)

In [3]: p.status
Out[3]: u'SUCCESS'

In [4]: p.result
Out[4]: 30

In [5]: exit
```

> Blog doc
