from concurrent.futures import process
import time
# print(time.time())
def send_emails():
    for i in range(1000000000):
        pass
    
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)