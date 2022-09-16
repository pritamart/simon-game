n = int(input("Enter the number of height\n"))
for i in range(n):
    for i in range(i+1):
        print('* ', end='')
    print()
print('-----------------------------')

for i in range(n):
    for i in range(i,n):
        print('* ', end='')
    print()
print('-----------------------------')

n = 5
k = n*2-2
for i in range(0,n):
    for j in range(0,k):
        print(' ',end='')
    k = k-2   
    for j in range(0,i+1):
        print('* ',end= '')
    print()
print('-----------------------------')

n = n+1
k = n*2-2
for i in range(0,n):
    for j in range(0,i+1):
        print('  ',end='')
        
    for j in range(n-i-1):
        print('* ',end= '')
    print()
print('-----------------------------')
rows = columns =n
k = 2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k =k-2
    for j in range(0, columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
print('--------------------------------')

rows = n
columns = n

for i in range(0,n):
    for j in range(0,i+1):
        print(end=' ')
    
    for j in range(0, columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
print('----------------------------------')

for i in range(n):
    for j in range(n-i-1):
        print('   ',end = '')
    for k in range(2*i+1):
        print(' * ',end= '')
    print()
print('-----------------------------')

for i in range(n):
    print(" " * i , end='')
    print("* "*(n-i))