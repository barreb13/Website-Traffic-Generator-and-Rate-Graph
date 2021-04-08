#!/usr/bin/python3
import sys
import random
import requests
import time

def main():    
    urlArg = sys.argv[1]
    rps = int(sys.argv[2])
    jitter = float(sys.argv[3])
    jitterMin = rps * (1.0 - jitter)
    jitterMax = rps * (1.0 + jitter)
    jitterRequestRate = int(random.uniform(jitterMin, jitterMax))
    print("Enter ctrl-c to quit")

    while True:
        jitterRequestRate = int(random.uniform(jitterMin, jitterMax))
        for _ in range(jitterRequestRate):
            r = requests.get(urlArg)   
        time.sleep(1 - time.time() % 1)        

if __name__ == "__main__":
    main()
