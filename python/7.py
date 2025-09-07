# write apython program to print index at which a perticular value
#  exists if the value at multiple location location then print all the 
# indices also count the of time that values is repeat in the list

a=[2,3,4,5,3,4,4,9,8,4,7,3,4,5,4,7,6,4,1,5,6]
b=int(input("enter the elementyou want to check :-"))
count=0
for i in range(0,len(a)):
    if (a[i]==b):
        print("the no is exist at index -",i )
        count +=1
print("the no is repeated ",count)