# Question 1.2
def make_keeper (n):
    def f(cond):
        i, count = 1, 0
        while i <= n:
            if cond(i):
                print (i)
            i = i + 1
    return lambda cond:f(cond)

# Question 1.7
def print_delayed(x):
    def delay_print(y):
        print (x)
        return print_delayed
    return delay_print

# Questions 1.8
def print_n (n):
    def inner_print (x):
        if n <= 0:
            print ("done")
        else:
            print (x)
        return print_n (n-1)
    return inner_print