Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fib(num):
    f = 0
    s = 1
    if num == 1:
        print(f)
    else:
        print(f)
        print(s)
        for i in range(1, num):
            c = f + s
            f = s
            s = c
            print(c)

            
fib(10)
0
1
1
2
3
5
8
13
21
34
55
