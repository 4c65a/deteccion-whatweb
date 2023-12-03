import subprocess
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target",help="Agrega una URL \n ( https:// o http:// )")
parser = parser.parse_args()



def main():
    
    if parser.target:
        subprocess.call("whatweb " + parser.target + "> whatweb.txt", shell=True)
        whatweb = open("whatweb.txt", "r")
        whatweb = whatweb.read()
        print(whatweb)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

