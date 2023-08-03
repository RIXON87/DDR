c=int(input("Enter a number : "))

for i in range(2,c):
    prime=True
    for t in range(2,i):
        if(i%t==0):
            prime=False
            break
    if(prime==True):
        print(i)
    
