def countINVpairs(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    count = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            count += n1 - i
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return count


def countinv(arr, l, r):
    if l < r:
        m = (l + r) // 2

        linv = countinv(arr, l, m)
        rinv = countinv(arr, m + 1, r)
        invs = countINVpairs(arr, l, m, r)

        return linv + rinv + invs
    else:
        return 0


lst = []
array_string = input("Enter the array elements separated by spaces: ")
array_strings = array_string.split()

for num_str in array_strings:
    try:
        ele = int(num_str)
        lst.append(ele)
    except ValueError:
        print(f"Error: '{num_str}' is not a valid integer.")

n = len(lst)

invPair = countinv(lst, 0, n - 1)
print("Total number of inversions:", invPair)
