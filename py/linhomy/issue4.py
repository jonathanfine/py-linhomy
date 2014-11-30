from .issue4tools import non_zero_entries
from .issue4tools import print_entries
from .issue4tools import C_G, D_G

if __name__ == '__main__':

    N = 6                           # Was 12.

    for n in range(2, N-1):

        print('C in the g basis.')
        print_entries(non_zero_entries(C_G[n]))
        print()

    for n in range(2, N-2):

        print('''D in the g basis - n = ''' + str(n))
        print_entries(non_zero_entries(D_G[n]))
        print()
