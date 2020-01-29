def operations():
    print('Operations on a List: ')
    print('Creating a list: ')
    mylist = ['India','USA','China','Japan']
    print(mylist)
    print('1. Accessing with index:')
    print(mylist[1])
    print('2. Adding a value to list:')
    mylist.append('Germany')
    print(mylist)
    print('3. Extending a list:')
    mylist.extend(['Mexico','France'])
    print(mylist)
    print('4. Concatenate two lists:')
    mylist2 = ['Russia','Israel','Canada']
    mylist+=mylist2
    print(mylist)
    print('5. Deleting an element from a list')
    del mylist[2]
    print(mylist)
    
    print('___________________________________________')

    print('Operations on a Tuple: ')
    print('Creating a tuple: ')
    mytuple = ['India',1,5.4]
    print(mytuple)
    print('1. Accessing the tuple: ')
    print(mytuple[2])
    print('2. Searching a tuple: ')
    for i in mytuple:
        if(i=='India'):
            print('India exists in this tuple')
    print('3. Printing the index: ')
    print(mytuple.index(1))
    print('4. Printing the number of times a character reapeats:')
    print(mytuple.count('i'))
    print('5. Tuple membership test:')
    print('India' in mytuple)

    print('___________________________________________')

    print('Operations on a Set: ')
    print('Creating a set: ')
    myset = {10,90,87,100,1}
    print(myset)
    print('1. Popping from set: ')
    print(myset.pop())
    print(myset)
    print('2. Discarding an element: ')
    myset.discard(10)
    print(myset)
    print('3. Union')
    A = {1,3,2,8,10}
    B = {4,8,6,10,0}
    print(A|B)
    print('4. Intersection: ')
    A = {1,3,2,8,10}
    B = {4,8,6,10,0}
    print(A&B)
    print('5. Set Difference: ')
    A = {1,3,2,8,10}
    B = {4,8,6,10,0}
    print(A^B)

    print('___________________________________________')

    print('Operations on a Dictionary: ')
    print('Creating a dictionary: ')
    mydict = {'name':'Mahatma Gandhi','age':150}
    print('1. Printing using a key: ')
    print(mydict['name'])
    print(mydict.get('age'))
    print('2. Update: ')
    mydict['age']=27
    print(mydict)
    print('3. Adding a key value pair: ')
    mydict['city'] = 'Porbandar'
    print(mydict)
    print('4. Pop function')
    print(mydict.popitem())
    print('5. Clear: ')
    mydict.clear()
    print(mydict)
    
operations()
