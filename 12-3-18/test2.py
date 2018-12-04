# Test

def mergeSort(arr):

    if len(arr) > 1:
        n = len(arr)
        arrL = arr[:n // 2]
        arrR = arr[n // 2:]
        mergeSort(arrL)
        mergeSort(arrR)
        i = j = k = 0

        while i < len(arrL) and j < len(arrR):
            if arrL[i] < arrR[j]:
                arr[k] = arrL[i]
                i += 1
            else:
                arr[k] = arrR[j]
                j += 1
            k += 1

        while i < len(arrL):
            arr[k] = arrL[i]
            i += 1
            k += 1
        
        while j < len(arrR):
            arr[k] = arrR[j]
            j += 1
            k += 1
        
        return arr

    else:
        return arr

test = [12, 6, 13, 5, 11, 7]
print(mergeSort(test))

###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###
###

def mergeSort2(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort2(L)
        mergeSort2(R)