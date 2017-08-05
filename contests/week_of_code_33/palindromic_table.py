# 32/41 tests passed

#!/bin/python3

import sys

def pal_check(len, lst):
    i,condn = 0,0
    #print (lst)
    while (condn < 2 and i<10):
        if(sum(row.count(i) for row in lst) % 2 ==1):
            condn+=1
        #print(str(sum(row.count(i) for row in lst)) + " " + str(i) + "'s")
        i+=1
    if(condn == 2 or sum(row.count(0) for row in lst) == len):
        return False
    else:
        return True

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
table = []
for table_i in range(n):
   table_t = [int(table_temp) for table_temp in input().strip().split(' ')]
   table.append(table_t)

dim_table = []

for i in range(n):
    for j in range(m):
        dim_table.append ([(i+1)*(j+1), i, j]) 
dim_table.sort(reverse=True)
#print(dim_table)
i,j,k,l = 0,0,0,len(dim_table)
result = False
while (result == False):
    #print (dim_table [k])
    i,j = dim_table[k][1],dim_table[k][2]
    for x in range(n-i):
        for y in range(m-j):
            sub_table = [[0] * (j+1) for s in range(i+1)]
            for p in range(x,i+x+1):
                for q in range(y, j+y+1):
                    sub_table[p-x][q-y] = table[p][q]
            result = pal_check(dim_table[k][0],sub_table)
            #print(result)
            if(result == True):
                print(dim_table[k][0])
                print(x, y, i+x, j+y)
                x,y = n-i+1,m-j+1
    k+=1
