#
#   No.784 「,（カンマ）」
#   https://yukicoder.me/problems/no/784
#

def comma(N):
    i=int(len(N))
    N_list=list(N)
    while i > 0:
        N_list.insert(i,',')
        i-=3
    result="".join(N_list)
    return result.rstrip(',')


if __name__ == "__main__":
    N=input('N: ')
    print(comma(N))