list=[2,3,4,5,2,6,7,8,9,0,5,4,3,2,3,6,7,6,5,8,5,3,4,2]
even=[]
odd=[]
for num in list:
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)
print("original list",list)
print("even number",even)
print("odd number",odd)
