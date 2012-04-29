.. _python_intro:

==========
Python简介
==========



安装
====


很多现代的Linux发行版默认安装的程序中就已经包括了Python。先检查一下
Python的版本，现在Django开发还需要Python2，推荐使用Python 2.7。


.. code-block:: console

    $ python --version
    Python 2.7.2


假如你看到的是3，比如像下面这样，请尝试用\ ``python2``\ 替换\ ``python``\ 。


.. code-block:: console

    $ python --version
    Python 3.2.1




Hello, world!
=============

**Hello world**\ 一般是指在学习的时候，写的第一个程序。这个程序只做一件
事，那就是显示\ ``Hello world``\ 。第一个程序是\ **Hello world**\ 的传
统可以追溯1974年\ [#history-of-hello-world]_\ 。


首先，输入\ ``python``\ 命令进入Python交互式命令行。

.. code-block:: text

    $ python
    Python 2.7.2 (default, Oct 27 2011, 01:40:22) 
    [GCC 4.6.1 20111003 (Red Hat 4.6.1-10)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 


输入\ ``print "Hello, world!"``\ 。

.. code-block:: pycon

    >>> print "Hello, world!"
    Hello, world!


.. [#history-of-hello-world]
    http://en.wikipedia.org/wiki/Hello_world_program#History


