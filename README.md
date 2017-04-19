# overwatch-daily
Daily statistics gathering for Overwatch


## Installation
Running under Ubuntu 12.04 or 14.04, might run into this error:

```
requests.exceptions.SSLError: [Errno 1] _ssl.c:504: error:14077438:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert internal error
```

There are several crappy ways to fix this, but upgrading urllib3 seems to be the sane solution.

http://urllib3.readthedocs.io/en/latest/user-guide.html#ssl-py2

```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
$ pip install urllib3[secure]
```
