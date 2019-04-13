def dth(dec): #dth
   dec=int(dec)
   output=''
   const=61440
   for i,j in zip(range(4),reversed(range(4))):
     k=((const>>i*4)&dec)>>4*j
     if k==10:
        output+='A'
     elif k==11:
     	  output+='B'
     elif k==12:
     	  output+='C'
     elif k==13:
     	  output+='D'
     elif k==14:
     	  output+='E'
     elif k==15:
     	  output+='F'
     else:
     	  output+=str(k)
   return output

def htd(hex):  #htd
   hex=hex.lower()
   sum=0
   n=len(hex)
   for i in range((n-1),-1,-1):
      if hex[i]=='a':
         sum+=(10*(16**(n-i-1)))
      elif hex[i]=='b':
         sum+=(11*(16**(n-i-1)))
      elif hex[i]=='c':
         sum+=(12*(16**(n-i-1)))
      elif hex[i]=='d':
         sum+=(13*(16**(n-i-1)))
      elif hex[i]=='e':
         sum+=(14*(16**(n-i-1)))
      elif hex[i]=='f':
         sum+=(15*(16**(n-i-1)))
      else:
      	  sum+=(int(hex[i])*(16**(n-i-1)))
   return sum
  
'''
2**16=65536
dth(var):
-->converts the parameter var given in dec into 16 bits hexadecimal number.
var<=2**16

htd(hex)
-->vice versa

check: htd(dth(m))==m for m<=2**16
'''
