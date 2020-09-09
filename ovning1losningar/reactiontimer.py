import time
import random

#Väntar slumpat antal sekunder, mäter reaktionstid och printar reaktionstiden
waitTime = random.randint(1,10)
time.sleep(waitTime)
t_noll = time.time()
a = input("Tryck enter!")
t_final = time.time()
print(t_final-t_noll)