def element_of(arr, i):
    for c in arr[1:]:
        if i == c:
            return True
    return element_of(arr[1], i)

def filter_by_depth(arr):
    None

def main():
    arr = []
    temp_arr=[]
    n = int(input("Enter number of elements : "))
# iterating till the range
    for i in range(0, n):
        l = int(input())
        arr.append(l) # adding the element
    i = arr[0]
    print(element_of(arr, i))
    m = input("What depth do you want to dive to? ")
    print(filter_by_depth(arr))
if __name__ == "__main__":
    main()