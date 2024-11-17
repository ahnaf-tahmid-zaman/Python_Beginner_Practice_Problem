def getListFromUser():
    lst = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    
    if len(lst) < 2:
        raise ValueError("List must have at least two distinct numbers.")
    return lst

def removeDuplicates(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def sorting(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def main():
    try:
        lst = getListFromUser()
        unique_list = removeDuplicates(lst)
        if len(unique_list) < 2:
            raise ValueError("List must have at least two distinct numbers.")
        sorted_list = sorting(unique_list)
        print(f"Second largest number from {lst} is: {sorted_list[1]}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
