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
