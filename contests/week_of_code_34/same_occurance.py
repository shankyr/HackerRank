# 25/30 tests passed
# https://www.hackerrank.com/contests/w34/challenges/same-occurrence

#!/bin/python3

import sys

if __name__ == "__main__":
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = list(map(int, input().strip().split(' ')))
    postn = {}
    arr_elements, key_set = set([]), set([])
    ans_history = {}
    for i in range(0,n):
        try:
            postn[arr[i]].append(i)
        except KeyError:
            postn[arr[i]] = [i]
        if arr[i] not in arr_elements:
            arr_elements.add(arr[i])
    #print (postn)
    #print (arr_elements)
    
    for a0 in range(q):
        p, q = input().strip().split(' ')
        y, x = max(int(p), int(q)), min(int(p), int(q))
        key = str(x) + '-' + str(y)
        # Write Your Code Here
        if key in key_set:
            ans = ans_history[key]
        elif ((x == y) or ((x not in arr_elements) and (y not in arr_elements))):
            ans = int (n * (n+1)/2)
            key_set.add(key)
        elif ((x in arr_elements) and (y not in arr_elements)):
            arr_temp = sorted(list(set(postn[x])))
            tt = len(arr_temp)
            if tt == 1:
                k = arr_temp[0]
                ans = int(k * (k+1)/2) + int((n-k-1)*(n-k)/2)
            else:
                k = arr_temp[0]
                ans = int(k * (k+1)/2)
                for i in range(1,tt):
                    k = arr_temp[i] - arr_temp[i-1]
                    ans += int(k*(k-1)/2)
                k = n - arr_temp[tt - 1]
                ans += int(k*(k-1)/2)
            key_set.add(key)
        elif ((y in arr_elements) and (x not in arr_elements)):
            arr_temp = sorted(list(set(postn[y])))
            tt = len(arr_temp)
            #print (arr_temp)
            if tt == 1:
                k = arr_temp[0]
                ans = int(k * (k+1)/2) + int((n-k-1)*(n-k)/2)
            else:
                k = arr_temp[0]
                ans = int(k * (k+1)/2)
                for i in range(1,tt):
                    #print (i)
                    k = arr_temp[i] - arr_temp[i-1]
                    ans += int(k*(k-1)/2)
                k = n - arr_temp[tt - 1]
                ans += int(k*(k-1)/2)
            key_set.add(key)
        else:
            sum_ref = {}
            set_x, set_y = set([]), set([])
            if x in arr_elements:
                for i in postn[x]:
                    sum_ref[i] = 1
                set_x = set(postn[x])
            if y in arr_elements:
                for i in postn[y]:
                    sum_ref[i] = -1
                set_y = set(postn[y])
            arr_temp = sorted(list(set_x) + list(set_y))
            #print(sum_ref)
            sum_arr = {}
            sum_elements = set([])
            sum_temp,ans = 0, 0
            sum_arr[0] = arr_temp[0] 
            sum_elements.add(sum_temp)
            tt = len(arr_temp)
            for i in range(1,tt):
                sum_temp += sum_ref[arr_temp[i-1]]
                if sum_temp not in sum_elements:
                    sum_elements.add(sum_temp)
                    sum_arr[sum_temp] = arr_temp[i] - arr_temp[i-1]
                else:
                    sum_arr[sum_temp] += arr_temp[i] - arr_temp[i-1] 
                
            sum_temp += sum_ref[arr_temp[tt - 1]]
            if sum_temp not in sum_elements:
                sum_elements.add(sum_temp)
                sum_arr[sum_temp] = n - arr_temp[tt - 1] 
            else:
                sum_arr[sum_temp] += n - arr_temp[tt - 1] 
            #print (sum_arr)
            for i in sum_elements:
                #print (i)
                if i == 0:
                    ans += int(sum_arr[i] * (sum_arr[i] + 1)/2)
                else:
                    ans += int(sum_arr[i] * (sum_arr[i] - 1)/2)
            key_set.add(key)
        print (ans)
        ans_history[key] = ans