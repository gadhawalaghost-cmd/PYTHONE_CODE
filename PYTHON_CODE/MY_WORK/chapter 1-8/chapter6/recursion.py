# when a function call itself repeatadly,its called recursion

def show (n):
    if n == 0:
        return 
    print(n)
    show (n-1)

show (6)