'''lst = list(map(int, input("Enter numbers : ").split(',')))
print("Your list:", lst)

def s_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum = lst[i]+sum
    return sum
print(s_list(lst))'''

lst = list(map(int, input("Enter numbers : ").split(',')))
def sum_lst(lst):
    sum=0
    if not lst:
        return 0
    else:
        sum = lst[0] + sum_lst(lst[1:])
    return sum
print("sum of the elements in the list are: ",sum_lst(lst))



    

    