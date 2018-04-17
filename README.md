[Packt]Django 1.0 Website Development.pdf

# 建立一个社会化书签应用
前一节，我们学了如果去创建一个空的项目，数据库设置，以及启动开发服务器。接下来，我们将写一个书签分享应用，同时在这个过程中学习views, models, templates。

你可以认为这一节是一个django主要组建的延生学习，将会学到如何用views去创建一个动态页面，用models在数据库里面存储和管理数据，以及用templates简化页面的生成。在学习这些特性的过程中，你会建立起django组件的工作及相互交互的原理。后面的章节中，我们会通过开发更多的特性来进一步探索这些组件，并把他们加入到我们的应用中。

本章节会覆盖以下内容
- URLs和Views： 创建主页
- Models： 设计和初始化数据库schema
- Templates：给主页创建模板
- 把以上这些整合起来：生成用户页面

## Django术语简介

Django是MVC框架。但是，这儿的controller叫做“view”，view是“template"。Django中的view是接收和处理数据的组件，模板是将数据呈现给用户的组件。因为这个原因，有时候Django也被叫做MTV框架（这儿 MTV指的是model，template和view）。术语名字的差别不会改变Django是一个MVC框架的事实，也不会影响应用的开发方式。但是如果你之前也用过其他的MVC的框架的话，还是要记住这个术语以免搞混了。

## URL和Views：创建主页
看到开发服务器欢迎页面之后，第一个出现的想法是：我们怎么去修改它？要创建自己的欢迎页面，我们需要定义一个应用入口，这个入口是URL形式，并且告诉Django当有人访问这个URL时去调用一个特定的python函数。我们会自己实现这个python函数，并让它显示我们的欢迎消息。

### 创建主页视图
Django术语中的view是一个普通python函数，它通过生成响应页面来响应页面请求。去写主页的第一个Django view，我们首先需要在我们的项目的创建一个Django应用application。你可以把这个应用想象成视图和数据模型的容器。

在django_bookmarks文件夹下面执行下面命令创建bookmarks应用。  
> $ python manage.py startapp bookmarks

创建用于的语法和创建项目的非常相似。```startapp```是```python manage.py```的 第一个参数， bookmarks是应用的名字。

运行这个命令之后，Django就会在项目文件夹下面创建一个bookmarks的文件夹，他包含下面文件：
- \_\_iniit\_\_.py: 这个文件告诉python，bookmarks是一个python包
- views.py: 包含视图
- models.py 包含数据模型

现在，我们开始创建主页试图。打开文件bookmarks/views.py，并输入下面代码
``` python
from django.http import HttpResponsedef main_page(request): output = u''' <html> <head><title>%s</title></head> <body> <h1>%s</h1><p>%s</p> </body> </html> ''' % (  u'Django Bookmarks',  u'Welcome to Django Bookmarks',  u'Where you can store and share bookmarks!'  ) return HttpResponse(output)
```

代码很短，我们一行一行来看一下：
- 首先，我们从django.http import了HttpResponse类，该类用于生成响应页面
- 我们定义了一个Python函数main_page, 它有一个参数request这个参数包含了用户输入和其他信息。例如request.GET, request.POST和request.COOKIES，这些都是字典，分别包含了get,post和cookie数据。
- 我们构建了响应页面的Html代码，并且把它封装在HttpResponse对象里，然后将它返回。Django用Unicode去存储和显示谁。因为这个原因，我们在字符前面添加了字符u来将它们转为unicode字符串。

Django view只是一个普通的Python函数。它把用户输入作为入参并返回页面输出。但是要看到这个视图输出，我们还需要将它关联到URL。
因为各种原因，通常我们并不推荐这种内嵌的HTML代码片段方式。这儿只是为了演示简单。后面的章节中，我们会学习如果将HTML代码放到独立的文件中。

