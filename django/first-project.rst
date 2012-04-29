.. first_django_project:


================
第一个Django项目
================

新建一个名叫\ ``myfirstproject``\ 的项目。

.. code-block:: console

    $ django-admin startproject myfirstproject


开发服务器
----------

切换到\ :file:`myfirstproject`\ 目录，运行命令\ ``python manage.py
runserver``\ ，你会在命令行中看到以下输出::

    Validating models...

    0 errors found
    Django version 1.3.1, using settings 'myfirstproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


现在开发服务器已经启动了。将浏览器指向\ http://127.0.0.1:8000/\ ，你会看到一个标
题是 "Welcome to Django" 的页面。


