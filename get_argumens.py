import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", dest="range", help="Specify the range you want to scan")
    options = parser.parse_args()
    if options.range:
        return options
    else:
        parser.error("[-] Please Specify the range you want to scan")
        