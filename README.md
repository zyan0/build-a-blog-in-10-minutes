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

## [1 min] 基础设施

### 创建 Project 和 App

### 设置数据库

### 运行服务器

## [1 min] Model - 如何存储你的文章

### MVC 简介

### 关于 Model：文章都有什么属性？
* 标题
* 时间
* 内容
* ...
* 关于 id

## [1 min] URL - 如何访问到各个页面
* 首页
* 管理页面
* 添加文章
* 编辑文章
* ...

## [4 min] 添加、编辑

### View
View 部分是和 Controller 完全独立的。

模版？变量？

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