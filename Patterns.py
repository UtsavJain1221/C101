num = int(input   ("Enter the number of Rows"))

for i in range(0, num):   
        for j in range(0, i + 1):              
            print("*", end=" ")
        print() 

0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 


for i in range(0, num):   
        for j in range(0, i + 1):              
            print(j, end=" ")
        print()   

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5       

for i in range(1,num):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

* * * * * 
* * * * 
* * * 
* * 
* 

for i in range(0,num):
    for j in range(num, i, - 1):
        print("*", end="")
       print() 