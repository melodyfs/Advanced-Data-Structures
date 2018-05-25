


def getWays(n, c):
    memos = [1] + ([0] * n)

    for i in range(len(c)):
        for combination in range(c[i], n+1):
            memos[combination] += memos[combination - c[i]]
    return memos[n]




if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    # print(n,m,c)
    ways = getWays(n, c)
    print(ways)

    # fptr.close()
