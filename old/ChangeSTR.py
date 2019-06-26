#
#   No.ABC126-A 「Changing a Character」
#   https://atcoder.jp/contests/abc126/tasks/abc126_a
#

import random, string

def randomname(n):
   return ''.join(random.choices('ABC', k=n))

def changeSTR(N, K):
    S=randomname(N)
    S_list=list(S)
    S_list[K-1] = S[K-1].lower()
    result="".join(S_list)
    return result

if __name__ == "__main__":
    N=input('N: ')
    K=input('K: ')
    S=changeSTR(int(N), int(K))
    print('S:', S)