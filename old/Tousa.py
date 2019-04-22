def tousa(initPageVal, r, N):
    an=initPageVal
    for num in range(N-1):
        an+=r
    print(an)

if __name__ == "__main__":
    N=999
    tousa(316, 52, N)