#Remove all occurrences of a specific element from a list.

def getListFromUser():
    n=int(input("Enter the length of the list: "))
    
    if n<=0:
        print("Enter a positive integer...")
        return []
    
    arr=[]
    
    for i in range(n):
        element=int(input(f"Enter the {i + 1} element: "))
        arr.append(element)
    
    return arr

def removeAllOccurrences(arr,removeItem):
    return [x for x in arr if x!=removeItem]

def main():
    arr=getListFromUser()

    if not arr:
        return

    removeItem=int(input("Enter the number you want to delete: "))
    updatedList=removeAllOccurrences(arr,removeItem)

    print(f'Updated List = {updatedList}')

if __name__=="__main__":
    main()


