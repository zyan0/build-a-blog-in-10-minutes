# 10 分钟搭建你的个人 blog

Python 大神柳开闫教你用 Django！

## 什么是 Python、Django？

## [1 min] 准备环境

安装 Python、Django。

### Linux and OS X
Python 已经默认安装，只需要先安装 pip（是什么？）：

	curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

然后安装 Django：

	pip install Django

以上。好简单！

### Windows
下载 Python 并安装（注意要下载 2.x 的版本）：

	http://python.org/getit/

将 python.exe 加入环境变量 path。

然后下载 Django 并解压：

	https://www.djangoproject.com/download/

最后在相应目录输入并运行：

	python setup.py install

## [2 min] 基础设施

### 创建 Project 和 App

	django-admin startproject yourname
	cd yourname
	django-admin startapp blog

### 设置数据库

在 settings.py 文件中将 DATABASES 设置为如下内容：

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'blog/db/database.db',          # Or path to database file if using sqlite3.
	    }
	}

### 启用 Admin 并将 Blog 加入已安装应用

	INSTALLED_APPS = (
	    ...
	    'django.contrib.admin',
	    'yourname.blog',
	)

### 运行服务器

	python manage.py runserver

## [2 min] Model - 如何存储你的文章

### MVC 简介

### 关于 Model：文章都有什么属性？
* 标题
* 时间
* 内容
* ...
* 关于 id

### 同步并建立相应数据库

	python manage.py syncdb

### 将相应 Model 注册入 Admin 中

	admin.site.register(YourModel)

## [1 min] URL - 如何访问到各个页面
* 首页
* 管理页面
* ...

## [2 min] 添加、编辑

借用 Admin 实现。

### View
View 部分是和 Controller 完全独立的。

模版？变量？

#### 输出
	{{ variables }}
#### 迭代
	{% for ele in list %}
		do something ...
	{% endfor %}
#### 模块
	{% block name %}
		<div>
			....
		</div>
	{% endblock %}
#### 继承
	{% extends "base.html" %}

### Controller
Controller 用来处理 Model 中的数据，传递给 View。

* 添加和修改文章
* 列出文章

## [2 min] 浏览文章
Simple enough now!

## Done! What's More?
* Category, tag?
* Comment?
* Beautiful template?
* ...
* With group, have a try!