def factorial(n):
    '"Finds factorial(n)"'
    if n==1: return 1
    else: return n*factorial(n-1)

n=int(input('Enter number: '))
print('Factorial of ',n,'=',factorial(n))
