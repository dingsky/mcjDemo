from function import myTime
import time

if __name__=="__main__":
    print(myTime.getLocalTime())

    while True:
        print('test for usleep', flush = True)
        time.sleep(0.01)