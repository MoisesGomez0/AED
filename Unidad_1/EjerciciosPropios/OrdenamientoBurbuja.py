class BubbleSort():
    def __init__(self):
        self.array = []
    def CollectingData(self):
        print("Escriba los valores, cuando termine escriba -s")
        value = input(":")
        while value != "-s":
            try:
                self.array.append(int(value))
                value = input(":")
            except:
                print("Parece que ese valor es invalido, dale otra vez")
                value = input(":")
    def Sort(self):
        for j in range(len(self.array)):
            for i in range(len(self.array)):
                if self.array[j] < self.array[i]:
                    temp = self.array[i]
                    self.array[i] = self.array[j]
                    self.array[j] = temp
    def Show(self):
        for i in self.array:
            print(i)

a = BubbleSort()
a.CollectingData()
a.Show()
print()
a.Sort()
a.Show()