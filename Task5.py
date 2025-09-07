n=int(input("Enter a number:"))
def fact(n):
    if(n<2):
        return 1
    else:
        return n*fact(n-1)
print(f"Factorial of {n} is:",fact(n))