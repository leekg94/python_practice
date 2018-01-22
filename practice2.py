import random

lotto=[]

for i in range(1,46):
  lotto.append(i)

num = random.sample(lotto, 6)

print(num)
