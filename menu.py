from hex16 import dth,htd
from binary import btd,dtb,bth,htb

def menu():
  doc="\n    This is a python program to convert a number from one number system to another. The operations are listed in the menu.\n\n  Here, a number in binary system is converted using only 16 bits. \n\n---The greatest number in DEC that can be represented into binary is 65535 i.e. FFFF in HEX\n---The greatest number in DEC that can be converted into HEX is 65535.\n "
  print(doc)
  print('\n')
  print('[code]','\t\t','[conversion]','\n')
  ops=['dec to bin',
    'dec to hex',
    'bin to dec',
    'bin to hex',
    'hex to dec',
    'hex to bin',
    'exit ',
    ]
  codes=[1,2,3,4,5,6,0]
  for i,j in zip(ops,codes) :
    print('  ',j,'\t\t',i,)
    print('\r')
  print('\r')

menu()
while True:
  code=int(input('enter the option:'))
  if code==0:
     break
  elif code==1: #dec to bin
     print('\n---DEC TO BIN ---')
     operand=input("enter the decimal number :")
     print('result:',dtb(operand),'\n')
     
  elif code==2: #dec to hex
     print('\n ---DEC TO HEX--- :')
     operand=input("enter the decimal number :")
     print('result:',dth(operand),'\n')
  elif code==3:
     print('\n---BIN TO DEC---')#bin to dec
     operand=input("enter the binary number :")
     print('result:',btd(operand),'\n')
  elif code==4:
     print('---BIN TO HEX---')#bin to hex
     operand=input("enter the binary number :")
     print('result:',bth(operand),'\n')
  elif code==5:
     print('\n---HEX TO DEC---')#hex to dec
     operand=input("enter the hexadecimal number :")
     print('result:',htd(operand),'\n')
  elif code==6:
     print('\n---HEX TO DEC---')#hex to bin
     operand=input("enter the hexadecimal number :")
     print('result:',htb(operand),'\n')
  else:
     print('===Invalid code! Try again===')
     print('\r')
     continue
