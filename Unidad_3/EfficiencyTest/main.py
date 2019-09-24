from Performance import (TestPerformance,ExecutionTime,ArrayGenerator)
from Algorithms import (QuickSort,SelectionSort,BubbleSort,InsertionSort)

test = TestPerformance()
execution = ExecutionTime()
arrayGenerator = ArrayGenerator()
result = []
array = arrayGenerator.generate(10000)
bubbleSort = BubbleSort()
insertionSort = InsertionSort()
selectionSort = SelectionSort()
quickSort = QuickSort()

bubble = test.test("Bubble",bubbleSort,execution,array.copy())
insertion = test.test("Insert",insertionSort,execution,array.copy())
selection = test.test("Select",selectionSort,execution,array.copy())
quick = test.test("Quick",quickSort,execution,array)
result.append(bubble)
result.append(insertion)
result.append(selection)
result.append(quick)

print("\n\n")
print("-"*80)
print("\tName\t\t|\t\tsize\t\t|\t\ttime")
print("-"*80)
for name,size,time in result:
    print("\t%s\t\t|\t\t%s\t\t|\t\t%s" %(name,size,time))
print("-"*80)