import sys
import resource

def main():
    #  The first argument will always be the script name, so the actual arguments for the program start at argv[1]...
    searchType = sys.argv[1]
    listSort = sys.argv[2]
    print(searchType)
    print(listSort)
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2))

main()