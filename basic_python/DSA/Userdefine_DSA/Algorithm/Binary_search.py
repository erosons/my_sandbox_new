class Binary_search:
    def __init__(self) -> None:
        self.firstvalue=None
        self.lastvalue=None
    
    def binary_Search(self,search_data,target):
        self.firstvalue=0
        self.lastvalue=len(search_data)-1
        Count=0
        while self.firstvalue<=self.lastvalue:
            Count +=1
            midpoint=(self.firstvalue + self.lastvalue)//2
            guess=search_data[midpoint]
            if guess==target:
                return midpoint , Count
            elif guess > target:
                self.lastvalue= midpoint -1

            else:
                 self.firstvalue=midpoint+1
        return None


if __name__=="__main__":
    testCase=Binary_search()
    print(testCase.binary_Search(sorted(["Samson","Tunde","kunle","Aiye","Under","Esther","Bayo","Mayo","Bisi","Titi"]),"Sisi"))