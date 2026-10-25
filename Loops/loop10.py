import time

wait_time = 1
max_retry = 5
attems = 0

otp = 5465
while attems < max_retry:
    print("attems",attems+1, "wait times", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attems +=1

