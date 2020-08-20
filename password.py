import random
chars = 'ajdbqorbZl164938#@'

number = input("enter the number of passwoed")
number = int(number)
length = input("enter th length of password")

length = int(length)
for pwd in range(number):
  password = ''
  for c in range(length):
    password+= random.choice(chars)
  print(password)