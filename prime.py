def prime_number():
    print('Enter the number to be checked: ')
    p=int(input())
    count=1
    for i in range(2,p):
        if p%i==0:
            count=2

    if(count>1):
        print('The number is not prime')
    else:
        print('The number is prime')

prime_number()
