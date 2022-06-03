num = input("enter a number: ")
try: 
    ival = int(num)
except: 
    ival = -1
	
if ival > 0 :
    print("number")
else:
    print("not a number")