from linhomy.issue4tools import CD_G
from linhomy.issue4tools import G_CD

def aaa(matrix):
    return list(map(list, matrix))

aaa(CD_G[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]

aaa(G_CD[4]) == [
    [1, 0, 0, 0, 0],
    [0, 1, -1, 0, 0],
    [0, 0, 1, -1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
