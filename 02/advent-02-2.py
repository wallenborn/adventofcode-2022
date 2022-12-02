import sys

# Rock, Paper, Scissors scores
# Player 1: A=Rock, B=Paper, C=Scissors
# Player 2 chooses such that: X=lose, Y=draw, Z=win
# 6 points for a win, 3 for a draw, 0 for a loss
# plus 3 points fo Z, 2 for Y, 1 for X
pts = {'A X': 3, 'A Y': 4, 'A Z': 8,
       'B X': 1, 'B Y': 5, 'B Z': 9,
       'C X': 2, 'C Y': 6, 'C Z': 7}

def main():
    if len(sys.argv) < 2:
        print("Usage: advent-02-1.py <inptfile>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename) as file:
        score = 0
        for line in file:
            key = line.rstrip()
            d = pts[key]
            score += d
    print(score)


if __name__ == '__main__':
    main()
