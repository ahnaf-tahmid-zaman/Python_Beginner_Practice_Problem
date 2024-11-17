#Merge two lists and remove duplicates.

def getListFromUser():
    lst=input("Enter a list separated by space: ").split()

    return lst

def mergeList(lst_1,lst_2):
    return lst_1+lst_2

def removeDuplicates(lst):
    unique_list=[]
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

def main():
    list_1=getListFromUser()
    list_2=getListFromUser()
    merge_list=mergeList(list_1,list_2)
    print(f'Merged List:\n{merge_list}')
    updated_list=removeDuplicates(merge_list)
    print(f'Updated List:\n{updated_list}')

if __name__=="__main__":
    main()