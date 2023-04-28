print("Generation Type")
generationType = int(input("Please enter the year that were born: "))
if generationType >= 1925 and generationType<=1946:
  print("You are Traditonalists.")
elif generationType >= 1947 and generationType<=1964:
  print("You are Baby Boomers")
elif generationType >= 1965 and generationType<=1981:
  print("You are Generation X")
elif generationType >= 1982 and generationType<=1995:
  print("You are Millenials")
elif generationType >= 1996 and generationType<=2012:
  print("You are Generation Z")
elif generationType >=2013:
  print("You are Gen Alpha")
else:
  print("You don't exist!")