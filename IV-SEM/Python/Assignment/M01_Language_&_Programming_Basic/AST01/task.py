def Ticket_Pricing(n: int) -> int:
   pass
   if(n<5):
      print("Free")
   elif(n>=5 and n<=17):
      return 10
   elif(n>=18 and n<=64):
      return 20
   else:
      return 15


if __name__ == '__main__':
   n = int(input())
   print(Ticket_Pricing(n))
