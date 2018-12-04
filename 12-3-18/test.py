# Test

arr = [6, 5, 1, 8, 7, 2, 4, 3]

def mergeSort(arr):
    
    minimum = 4
    n = len(arr)

    if n < minimum:
        return arr
    else:
        subArr1 = sorted([arr[i] for i in range(n // 2)])
        subArr2 = sorted([arr[j] for j in range(n // 2, n)])
        finalArr = []
        i = 0
        j = 0

        for k in range(n):
            if i == n // 2:
                finalArr.append(subArr2[n // 2 - 1])
            elif j == n // 2:
                finalArr.append(subArr1[n // 2 - 1])
            else:
                if subArr1[i] < subArr2[j]:
                    finalArr.append(subArr1[i])
                    i += 1
                elif subArr1[i] > subArr2[j]:
                    finalArr.append(subArr2[j])
                    j += 1
        
        return finalArr

arr = [6, 5, 1, 8, 7, 2, 4, 3]
print(mergeSort(arr))