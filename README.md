# unique-identifier-generator

Simple 8-character unique identifier generator

## Algorithm


## Programs

This library consists of following programs:

### uid.py

8-character unique identifier generator.

Algorithm is described here:
http://debiancdn.wordpress.com/2013/04/07/%E5%8A%A0%E7%95%91%E3%81%95%E3%82%93%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%93%E3%83%A5%E3%83%BC%EF%BC%9A%E8%A1%9D%E7%AA%81%E3%81%97%E3%81%AA%E3%81%84%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E4%BD%9C%E3%82%8B/

Cycle is 4000 ^ 4 = 256000000000000

### server.py

Thin XML-RPC Server wrapper for uid.py.

Allowed methods are :
- id(retrieve next id)
- counter(retrieve current counter)
- reset(reset counter and random characters)

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


