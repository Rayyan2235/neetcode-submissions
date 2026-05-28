class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)

        return (self.arr[n//2] if (n & 1) # n & 1 checks if the n value has a 1 in the LSB indicating that it is an odd number
        else (self.arr[n//2] + self.arr[(n//2) -1]) / 2)
            

        
        
        