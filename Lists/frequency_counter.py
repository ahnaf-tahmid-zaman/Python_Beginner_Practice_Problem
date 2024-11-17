#Count the frequency of each element in a list.


def frequencyCounter (lst):
    countedItem=[]
    frequncies=[]

    for i in range(len(lst)):
        if lst[i] not in countedItem:
            count=0
            for j in range(len(lst)):
                if lst[i]==lst[j]:
                    count+=1
            countedItem.append(lst[i])
            frequncies.append((lst[i], count))
    
    for element, freq in frequncies:
        print(f'{element}:{freq}')


if __name__=="__main__":
    lst=input("Enter elements of the list separated by spaces: ").split()
    print("Frequencies of elements:")
    frequencyCounter(lst)
