coins = []
n = int(input())
score_1 = 0
score_2 = 0
empty = []

def main():
    if 1 < n <= 30 and n % 2 != 0:
        exit()

    for i in range(1, n+1):
        coins.append(i)

    print(coins)

def p1_selectable():
    global coins
    global score_1
    select = max(coins)
    score_1 += select
    coins.remove(select)

def p2_selectable():
    global coins
    global score_2
    select = max(coins)
    score_2 += select
    coins.remove(select)


main()
while coins != empty:
    p1_selectable()
    p2_selectable()

print(score_1)
