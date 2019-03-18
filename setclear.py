from core_conversion.binary import dtb,btd
def musk_generator(n):
  musk=2**(n)
  return musk

def main():
    num=int(input("Enter a number in decimal <= 65535 :"))
    if num>65535:
       print("ERROR! Decimal number should be <= 65535.\n\n")
       return 0
    print("The number in 16 bit binary form is:{0}\n".format(dtb(num)))  
    print("\t\t\t===SET and CLEAR===\nSelect a bit for set&clear operation. Numbering is done from 0-15 from right to left---")
    n_bit=int(input()) 
    if n_bit>15:
       print("ERROR! position of bit should be <= 15.\n\n")
       return 0
    #generate the musk register with the given bit:
    musk=musk_generator(n_bit)
   
    print("\n-->enter 1 for set. \n-->enter 2 for clear.\n-->enter 3 for Exit.")
    op=int(input())
    if op==1:
        operation="set"
        result=num|musk
        print("\nAfter {0}, the binary form is:{1}\n".format(operation,dtb(result)))
        return 1  #returning 1 as success
    elif op==2:
        operation="clear"
        result=num&(~musk)
        print("\nAfter {0}, the binary form is:{1}\n".format(operation,dtb(result)))
        return 1  #returning 1 as success
    elif op==3:
        return 3  #returning 3 to exit the loop
        
    else:
        print("\nInvalid operation!")
        return 0  #returning 0 for fail and continue the loop
        
    print("\nAfter {0}, the binary form is:{1}".format(operation,dtb(result)))

if __name__=="__main__":
    while True:
        status=main()
        if status==3:
            break
        elif status==0:
            continue


  

