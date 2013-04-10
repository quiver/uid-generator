# unique-identifier-generator

Simple 8-character unique identifier generator

## Algorithm

1. Make 4 buckets(b1, b2, b3, b4) of 4000 2-character unique keys(eg. 3z, 2d, ...)
2. For each bucket, select a prime number(p1, p2, p3, p4) around 3800(less than 4000)
3. Let N be an auto-incremented number.
   For each bucket, pick up a key such that k1 = b1[N mod p1].
4. Concatenate each key, then you'll get a new unique identifier :
     new-id = k1 + k2 + k3 + k4

## Programs

This library consists of following programs:

### uid.py

8-character unique identifier generator.

Algorithm is described here:
http://debiancdn.wordpress.com/2013/04/07/%E5%8A%A0%E7%95%91%E3%81%95%E3%82%93%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%93%E3%83%A5%E3%83%BC%EF%BC%9A%E8%A1%9D%E7%AA%81%E3%81%97%E3%81%AA%E3%81%84%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E4%BD%9C%E3%82%8B/
http://www.youtube.com/watch?feature=player_detailpage&v=-nfEjkc0CBo#t=6120s

Cycle is 3793 x 3797 x 3803 x 3821 = 200 trillion

### server.py

XML-RPC Server wrapper for uid.py. default port is 8000.

Allowed methods are :
- id(retrieve next id)
- counter(retrieve current counter)
- reset(reset counter and random characters)

```
$ python server.py --help
usage: server.py [-h] [--port [PORT]] [--db [DB]]

optional arguments:
  -h, --help     show this help message and exit
  --port [PORT]
  --db [DB]

$ python server.py --port 8080
```


### client.py

Sample XML-RPC Client program to communicate with uid server.

### shell.py

Shell interface to communicate with uid server.

```
$ python shell.py
localhost:8000> help

Undocumented commands:
======================
EOF  counter  help  id  reset

localhost:8000> counter
None
localhost:8000> reset
localhost:8000> counter
0
localhost:8000> id
4de0u7gm
localhost:8000> id
k3d70nw7
localhost:8000> counter
2
```


