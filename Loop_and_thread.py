import time, threading

def disp_msg(msg, limit):
    count=0
    while count < limit:
        #time.sleep(3)
        print(msg)
        count += 1

thread1 = threading.Thread(target=disp_msg, args=("Loop1",3))
thread2 = threading.Thread(target=disp_msg, args=("Loop2",5))

thread1.start()
thread2.start()

thread1.join()
print("Completed 1")
thread2.join()
print("Completed 2")


for i in range(5):
    if i == 3:
        break
    print(i)

print("Break is tested")

for i in range(5):
    if i == 3:
        continue
    print(i)

print("Continue is tested")

lst=[]
# Fine prime number
def prime_number(start, end):
    for i in range(start,end):
        if i < 2:
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            lst.append(i)


prime_number(1,20)
print(lst)

# Fibonacci Series
first,second=0,1
for i in range(10):
    print(first,end=' ')
    first,second=second,first+second

names = ["Karthik","GR","Jith"]
city = ["Vanavasi","Salem","Chennai"]

zipped = list(zip(names, city))
print(zipped)

