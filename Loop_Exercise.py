# a=int(input("Enter value:"))
# num=1
# count=0
# sum=0
# if a==0:
#     print("exist")
#     exit()
# while(a>0):
#     sum +=num
#     count +=1
# avg = (sum/(count-1))
# print("Average:")

# print("|-------------------------------|")
# print("|     celsius \t| Farenheits    |")
# print("|-------------------------------|")
# for i in range(101):
#     if(i%10==0):
#         f=(i*(9/5)+32)
# print("|\t",i,"\t|",f,"\t""|")
# print("|-------------------------------|")

a=int(input("Enter a string: "))
palindrome=True
for i in range(0,len(line) //2):
if line[i]!=line[len(line)-i-1]:
    palindrome=False
if palindrome:
    print(line,"is a palindrome")
else:
    print(line,"is not a palindrome")
       



