

#this is counter function using if-statement

def counter1():
   a=x=0 #a-->old(present) state x-->new state
   for i in  range(32):
          print(x)  
          if a&1==1:  
                x=a^2  
          if a&3==3:  
                x=x^4  
          if a&7==7:  
                x=x^8  
          if a&15==15:  
                x=x^16
          if a&31==31:  
                x=x&1  
          x=x^1  
          a=x 


#this is counter function-using for loop 


def mask_gen(k):      #suppose to use bitwise operator
     return 2**(k+1)-1


def counter2():
   old_state=new_state=0 #a-->old(present) state x-->new state
   count_enable=1
   for i in range(32):
     print(new_state)
     for k in range(5):
         mask=mask_gen(k)  #should use a mask generator!
         if (old_state&mask)==mask:
             new_state=new_state^(2<<k)
         if old_state&31==31:  
                   new_state=new_state&1  
     new_state=new_state^count_enable
     old_state=new_state

#counting--
counter1()
counter2()
