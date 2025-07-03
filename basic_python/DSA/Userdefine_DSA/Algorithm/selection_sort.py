# Finds the minimum in a number

def find_min_elem_index(arr):
    min_num=1000
    for i in range(len(arr)):
        if arr[i]<min_num:
            min_num=arr[i]
            smallest_index=i
    
    return smallest_index


def selectsort(arr):
    newarr=[]
    for elem in range(len(arr)):
        smallest=find_min_elem_index(arr)
        newarr.append(arr.pop(smallest))
    return newarr



if __name__=="__main__":
    test=[13,4,6,34,7,9,15,11]
    selectsort(test)