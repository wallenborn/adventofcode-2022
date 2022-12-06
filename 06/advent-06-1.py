import sys


# In an elven communications input stream of characters,
# find the first character such that this and the three
# previous characters are distinct
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-06-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    marker_length = 4
    with open(filename) as file:
        for line in file:
            # slide a 4-character wide window over the input
            for i in range(0, len(line)-(marker_length+1)):
                # size of set is the number of distinct characters
                if marker_length == len(set(list(line[i:marker_length+i]))):
                    print(marker_length+i)
                    break


if __name__ == '__main__':
    main()
