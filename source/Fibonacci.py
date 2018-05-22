

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(50))

# fib(10): 89
# fib(20): 10946
# fib(30): 1346269
# fib(40): 165580141
# runnning time goes up
