def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i = j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list

lst1=[]
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
   
    lst1.append(ele)   # adding the element

lst2=[]
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
   
    lst2.append(ele)   # adding the element

print(merge_sorted_lists(lst1, lst2)) 
