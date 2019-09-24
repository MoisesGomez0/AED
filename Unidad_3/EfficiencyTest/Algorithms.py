class QuickSort:
    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to rigth
    # of pivot
    def __init__(self):
        pass
    
    def partition(self,arr,low,high):
        i = (low-1) # index of smaller element
        pivot = arr[high] # pivot
        for j in range(low,high):
            # If current element is smaller than of
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1],arr[high] = arr[high], arr[i+1]
        return i+1
    
    def quitSort(self,arr,low,high):
        if low< high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr,low,high)

            # Separately sor elements before
            # partition and ofter partition
            self.quitSort(arr,low,pi-1)
            self.quitSort(arr,pi+1,high)

    def sort(self,data=[]):
        return self.quitSort(data,0,len(data)-1)

class SelectionSort:
    def __init__(self):
        pass
    def sort(self,data=[]):
        # Traverse through all array elements
        for i in range(len(data)):
            # Find the minimun element in remaining
            # unsorted array
            min_idx = i
            for j in range(i+1,len(data)):
                if data[min_idx]> data[j]:
                    min_idx = j
            # Swap the found minimun element with
            # the first element
            data[i],data[min_idx] = data[min_idx],data[i]
        return data

class InsertionSort:
    def __init__(self):
        pass
    def sort(self,data=[]):
        for i in range(1,len(data)):
            # Element to be compared
            current = data[i]

            # Comparing the current elemenet whit the sorted portion and swapping
            while i>0 and data[i-1]>current:
                data[i] = data[i-1]
                i = i-1
                data[i] = current
        return data

class BubbleSort:
    def __init__(self):
        pass
    def sort(self,data=[]):
        for i in range(len(data)):
            for j in range(len(data)):
                if data[j]<data[i]:
                    temp = data[i]
                    data[i]=data[j]
                    data[j]=temp
        return data