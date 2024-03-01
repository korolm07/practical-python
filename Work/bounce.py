# bounce.py
#
# Exercise 1.5
bounce = 3/5
height_start = 100
height = height_start*bounce
number = 1
while number < 11:
  print(number,round(height,4))
  number = number + 1
  height = height * bounce
