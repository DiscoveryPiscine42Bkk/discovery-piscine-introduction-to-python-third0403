x= int(input("Please tell me your age :"))
print(f"You are currently {x} years old")
y = 0
for i in range(3):
  y += 10
  print(f"In {y} years, you'll be {x + y} years old")
