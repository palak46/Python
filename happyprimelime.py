class HappyPrime:
    
    def __init__(self,pmin,pmax,hmin,hmax):
        self.pmin=pmin
        self.pmax=pmax
        self.min=hmin
        self.max=hmax
        
    def prime(self):
        list1=[]
        for pnum in range(self.pmin,self.pmax):
            for i in range (2,pnum):
                if (pnum%i)==0:
                    break
            else:
                list1.append(pnum)
        return list1

    def happyNumbers(self):
        list2=[]
        for i in range(self.min,self.max):
            num=i
            while True:
                my_list=[int(x) for x in str(num)]
                num=0
                for j in my_list:
                    num=num+(j)**2
                if num==4 or num==16 or num==20 or num==37 or num==42 or num==58 or num==89 or num==145:
                    break
                elif num==1:
                    list2.append(i)
                    break
        return list2

    def prime_happy_comparison(self):
        comparison=[]
        for i in self.prime():
            if i in self.happyNumbers():
                comparison.append(i)
        return comparison
    def main_process(self):
        L1=self.prime()
        print("prime number series:",L1)
        L2=self.happyNumbers()
        print("happy prime series:",L2)
        L3=self.prime_happy_comparison()
        print("comparison between prime and happy prime:",L3)
        
        
        
        

#pmin = int(input("ENter min val for prime numbers : "))
#pmax = int(input("ENter max val for prime numbers: "))
#L1=prime(self.pmin,self.pmax)
#print("list of prime numbers:")
#print(prime(self.pmin,self.pmax))

#min = int(input("ENter min val for happy numbers: "))
#max = int(input("ENter max val for happy numbers: "))
obj = HappyPrime(5,100,5,100)
obj.main_process()
#l2=obj.happyNumbers()
#l1=obj.prime()
#l3=obj.prime_happy_comparison()
#print(l1)
#print(l2)
#print(l3)




    

#appyNumbers(self.min,self.max)
#print("list of happy numbers")
#print(happyNumbers(self.min,self.max))

#L3=(prime_happy_comparison(L1,L2))
#print("list of comparison between prime and happy number is:")
#print(prime_happy_comparison(L1,L2))




