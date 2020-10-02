# -*-coding:utf8;-*-
# qpy:3
# qpy:console
from collections.abc import Iterator,Iterable


def my_ange(end):
    start = 0
    while start < end:
        x = yield start
        print(x)
        start += 1


a = my_ange(2)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
for i in a:
    print(i, end=' ')
print(a.send(None))
print(a.send('python'))
