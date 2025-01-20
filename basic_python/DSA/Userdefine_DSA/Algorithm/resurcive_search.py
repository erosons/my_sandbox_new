mylist=[1,2,3,4,5,6,7]

def serachList(list_to_serach,value,index):
    
    if list_to_serach[index]==value:
        return print(f' Value {value} found ')
    else:
        serachList(list_to_serach,value,index+1)



serachList(mylist,5,0)

        