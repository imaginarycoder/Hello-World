def quadratic():
    print('Enter a, b and c in the equation ax^2+bx+c')
    a=float(input())
    b=float(input())
    c=float(input())
    d=(b**2)-(4*a*c)

    root1=((-1*b)+((b**2)-(4*a*c))**(1/2))/(2*a)
    root2=((-1*b)-((b**2)-(4*a*c))**(1/2))/(2*a)
    
    
    if d<0:
        print('Roots are imaginary')
    elif d==0:
        print('Roots are real and equal:')
        print('The roots are %.3f and %.3f' %(root1,root2))
    elif d>0:
        print('Distinct real roots:')
        print('The roots are %.3f and %.3f' %(root1,root2))

quadratic()            
