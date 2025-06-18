x = 0
while x <= 10:
  print(f"Table de {x} :", end=" ")
  y = 0
  while y <= 10:
    print(x * y, end=" ")
    y += 1

  print()
  x += 1
