x=  [2,8,9,48,8,22,-12,2]
y= []


for i in range(len(x)):
  
  if x[i] > 5:
    if x[i] + 2 not in y:
       y.append(x[i] + 2)
    
  
print(x)
print(y)
