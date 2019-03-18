from core_conversion.hex16 import htd,dth
def dtb(num):  #dtb
   num=int(num)
   const=32768
   output=''
   for i in range(1,17):
      if(num&const):
         output+='1'
      else:
         output+='0'
      const=const>>1
   return output

'''
def btd(bin):
   binary=str(bin)
   sum=0
   l=len(bin)
   for i in range((len(bin)-1),-1,-1):
       sum+=(int(bin[i]))*(2**(l-i-1))
   return sum
'''

def btd(bin): #btd
   sum=0
   l=len(bin)
   for i in range(l):
      sum+=(int(bin[i]))*(2**(l-i-1))
   return sum
      
def bth(num): #bth
   return dth(btd(num))

def htb(num): #htb
   return dtb(htd(num))
