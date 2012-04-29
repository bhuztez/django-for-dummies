.. _cgi:

===
CGI
===

.. code-block:: python

    #!/usr/bin/env python2

    import cgitb
    cgitb.enable()

    import cgi

    print "Content-Type: text/html"
    print

    cgi.print_environ()



.. code-block:: console

    $ env -i - PATH="${PATH}" python -m CGIHTTPServer
    Serving HTTP on 0.0.0.0 port 8000 ...



表单处理
========

