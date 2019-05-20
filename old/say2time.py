#
#   No.739 大事なことなので２度言います
#   https://yukicoder.me/problems/no/739
#

def say2time(S):
    if len(S)%2 ==  0:
        splitNum=int(len(S)/2)
        if S[:splitNum] == S[splitNum:]:
            print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    S='yukicoder'
    say2time(S)