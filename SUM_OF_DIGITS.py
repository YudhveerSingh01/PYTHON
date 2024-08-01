nums=1245
s=0
dig=0
while(nums!=0):

    dig=nums%10
    s=s+dig
    nums=nums//10



print("Sum of Digits=",s)

