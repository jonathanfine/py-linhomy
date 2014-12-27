from linhomy.matrices import F_from_IC

def lists_from_matrix(matrix):

    return [
        list(map(int, row))
        for row in matrix
    ]

lists_from_matrix(F_from_IC[4]) == [
    [1, 5, 10, 10, 30],
    [1, 6, 13, 13, 40],
    [1, 7, 15, 14, 45],
    [1, 8, 16, 14, 48],
    [1, 10, 21, 18, 64],
]


from linhomy.matrices import IC_from_CD_helper

list(IC_from_CD_helper(b'')) == [
    b'',
]

list(IC_from_CD_helper(b'\x01')) == [
    b'\x01',
]

list(IC_from_CD_helper(b'\x02')) == [
    b'\x01\x01',
    b'\x02',
]

list(IC_from_CD_helper(b'\x02\x01\x02\x02')) == [
    b'\x01\x01\x01\x01\x01\x01\x01',
    b'\x01\x01\x01\x01\x01\x02',
    b'\x01\x01\x01\x02\x01\x01',
    b'\x01\x01\x01\x02\x02',
    b'\x02\x01\x01\x01\x01\x01',
    b'\x02\x01\x01\x01\x02',
    b'\x02\x01\x02\x01\x01',
    b'\x02\x01\x02\x02',
]


from linhomy.matrices import IC_from_CD

lists_from_matrix(IC_from_CD[4]) == [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
]
