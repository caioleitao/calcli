n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
operations = input("To run operations \n Enter 1 to sum \n Enter 2 to subtract \n Enter 3 to split \n Enter 4 to Multiply \n (1/2/3/4): ")

if(operations == 1):
    operations1 = n1 + n2
    print("result: {}".format(operations1))
elif(operations == 2):
    operations2 = n1 - n2
    print("result: {}".format(operations2))
elif(operations == 3):
    operations3 = n1 / n2
    print("result: {}".format(operations3))
elif(operations == 4):
    operations4 = n1 * n2
    print("result: {}".format(operations4))
else:
    print("Error")