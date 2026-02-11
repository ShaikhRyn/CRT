from typing import List

def Collatz_Sequence(n: int) -> List:
   lis = [n]
   
   while n!=1:
      if n%2 == 0:
            n = n//2
      else:
         n = 3*n+1
      lis.append(n)
   return lis

if __name__ == '__main__':
   n = int(input())
   print(Collatz_Sequence(n))
