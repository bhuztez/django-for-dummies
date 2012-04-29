.. _hyper_text:

==========
HTML和HTTP
==========


.. literalinclude:: /_src/python/hyper-text/hello.html
   :language: html


.. code-block:: console

    $ python -m SimpleHTTPServer
    Serving HTTP on 0.0.0.0 port 8000 ...


.. code-block:: console

    $ python -m urllib 'http://localhost:8000/hello.html'
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">
    <HTML>
       <HEAD>
          <TITLE>Hello, world!</TITLE>
       </HEAD>
       <BODY>
          <H1>Hello, world!</H1>
       </BODY>
    </HTML>
    $



.. code-block:: console

    $ python -m telnetlib localhost 8000
    GET /hello.html HTTP/1.0
    Content-Length: 0

    HTTP/1.0 200 OK
    Server: SimpleHTTP/0.6 Python/2.7.2
    Date: Mon, 30 Apr 2012 11:28:26 GMT
    Content-type: text/html
    Content-Length: 215
    Last-Modified: Mon, 30 Apr 2012 11:28:11 GMT

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">
    <HTML>
       <HEAD>
          <TITLE>Hello, world!</TITLE>
       </HEAD>
       <BODY>
          <H1>Hello, world!</H1>
       </BODY>
    </HTML>
    *** Connection closed by remote host ***
    $




