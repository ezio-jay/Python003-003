# MTV框架
Model 负责和数据库进行交互，进行数据处理
View  负责业务逻辑，调用Model和Template
Template 负责将页面内容展示给用户
#Django
采用MTV的框架
##Django的安装
$pip install --upgrade django==version
##创建Django项目
$ django-admin startproject MyDjango
$ python manage.py startapp index
##运行Django项目
$ python manage.py runserver
##settings.py主要配置文件
INSTALL_AAPS加载自己所设置的APP

