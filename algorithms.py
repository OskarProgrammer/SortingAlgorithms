import random

class Helper(object):
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        R = [0] * (n2)
        L = [0] * (n1)
 
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
 
        i = 0     
        j = 0    
        k = l    
 
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
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
 

class Sort(Helper):
   
    def quickSort(self, array: list) -> list:
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            greater = [x for x in array if x>pivot ]
            less = [x for x in array if x<pivot ]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)
    
    def bumbleSort(self, array: list) -> list:
        i = 1
        while i != 0:
            i = 0
            for x in range(len(array)):
                try:
                    if array[x] > array[x+1]:
                        mem = array[x]
                        array[x],array[x+1] = array[x+1], mem
                        i += 1
                except IndexError:
                    pass
        return array
    
    def insertSort(self, array: list):
        n = len(array)

        if n<=1:
            return

        for x in range(1, n):
            current = array[x]
            previousIndex = x-1
            while previousIndex >= 0 and current < array[previousIndex]:
                array[previousIndex + 1] = array[previousIndex]
                previousIndex -= 1

            array[previousIndex + 1] = current

    def mergeSort(self, array, l, r):
        if l < r:

            m = l+(r-l)//2

            self.mergeSort(array, l, m)
            self.mergeSort(array, m+1, r)
            self.merge(array, l, m, r)


sort = Sort()

randomList = [random.randrange(-20,100) for x in range(100)]

print(sort.quickSort(randomList))
print(sort.bumbleSort(randomList))

randomList = [random.randrange(-20,100) for x in range(100)]

sort.insertSort(randomList)
print(randomList)

randomList = [random.randrange(-20,100) for x in range(100)]

sort.mergeSort(randomList, 0, len(randomList)-1)
print(randomList)