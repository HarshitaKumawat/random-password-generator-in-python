import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol= "!@#$%^&*_[]{}.,/?"
number = "1234567890"
all = lower + upper + symbol + number
length = 9
password = "".join(random.sample(all,length))
print("the password you generated is:",password)