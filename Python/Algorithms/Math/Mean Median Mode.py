"""
● Anisha is learning statistics and she is unable to find the values of central tendency ( Mean, Median,
and Mode) correctly. To help her write a python program. Create a class ct ( central tendency ) that will
store the list of values. Then create 5 methods:
● addValue()
● removeValue()
● mean()
● median()
● mode()
● Note:
● To find mean: Add all the elements and divide it by the length of list.
● To find median: sort the list in ascending order then return the middle value of the list.
● To find mode: return the element occurring most number of times.
"""


class ct:
    def __init__(self, List):
        self.l = List

    def addValue(self):
        a = int(input("Please enter how many numbers you want to add:"))
        for b in range(a):
            i = int(input("Please enter a new number: "))
            List.append(i)
        print(self.l)

    def removeValue(self):
        a = int(input("Please enter how many numbers you want to remove:"))
        for b in range(a):
            print(self.l)
            i = int(input("Please enter a existing number for removal: "))
            self.l.remove(i)
        print(self.l)

    def mean(self):
        temp2 = self.l
        temp = len(self.l)
        self.l = sum(self.l)
        self.l = self.l/temp
        print(int(self.l))
        self.l = temp2

    def median(self):
        length = len(self.l)
        temp = self.l
        hl = int(length/2)
        self.l.sort()
        if length % 2 == 0:
            m = (self.l[hl-1]+self.l[hl])/2
            print(m)
        else:
            term = int((length+1)/2)
            m = self.l[term-1]
            print(m)
        self.l = temp

    def mode(self):
        print(max(set(self.l), key=self.l.count))


List = [51, 61, 12, 15, 201, 15]
new = ct(List)
new.mode()
