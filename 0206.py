length1=int(input('Enter the first length: '))
length2=int(input('Enter the second length: '))
length3=int(input('Enter the third length: '))
if length1+length2>length3 and length1+length3>length2 and length2+length3>length1:
    print('Yes')
else:
    print('No')