
newlist = [12, 34, 45, 9, 89, 2, 4, 6, 56, 7, 13, 15, 17]


class Binarysearch:
    firstvalue = None
    lastvalue = None
    midpoint = None

    def bin(self, mylist, target):
        self.firstvalue = 0
        self.lastvalue = len(mylist)-1
        while self.firstvalue <= self.lastvalue:
            self.midpoint = (self.firstvalue + self.lastvalue)//2

            if mylist[self.midpoint] == target:
                return self.midpoint
            elif mylist[self.midpoint] < target:
                self.firstvalue = self.midpoint + 1

            else:
                self.lastvalue = self.midpoint-1
        return None


if __name__ == "__main__":
    test = Binarysearch()
    test.bin(sorted(newlist), 17)
