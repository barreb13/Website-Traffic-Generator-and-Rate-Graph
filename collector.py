#!/usr/bin/python3
import requests
import time
import urllib
import argparse
import time

#stats page --> http://localhost:8080/stats
parser = argparse.ArgumentParser()
parser.add_argument("webPage")
parser.add_argument("outputTextFile")
parser.add_argument("--interval")
args = parser.parse_args()

def main():
    print("Enter ctrl-c to quit")
    url = args.webPage
    outputFile = args.outputTextFile
    interval = int(args.interval)
    while True:
        page = requests.get(url)
        pageString = page.text
        lines = pageString.split("\n")
        pairs = (line.split(": ") for line in lines[:-1])
        newDict = dict(pairs)
        dictList = []
        for key in newDict:
            dictList.append(newDict[key])
        newString = "\t".join(str(x) for x in dictList)

        with open(outputFile, "a") as out:
            out.write(newString)
            out.write("\n")
        
        time.sleep(interval - time.time() % interval)   

if __name__ == "__main__":
    main()