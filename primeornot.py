n=int(input('enter a number'))
def prime():
    if n==1:
        print(n,"is not prime")
    for i in range(2,n):
        if n% i==0:
            print(n,"is not prime")
        else:
            print(n,"is prime")
            break
    else:
        print(n,"is prime")
prime()


