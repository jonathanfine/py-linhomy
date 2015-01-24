from linhomy.issue26 import compose_3

list(compose_3(-1)) == []

list(compose_3(0)) == [
    (0, 0, 0),
    ]

list(compose_3(1)) == [
    (0, 0, 1), (0, 1, 0),
    (1, 0, 0),
    ]

list(compose_3(2)) == [
    (0, 0, 2), (0, 1, 1), (0, 2, 0),
    (1, 0, 1), (1, 1, 0),
    (2, 0, 0),
    ]

list(compose_3(3)) == [
    (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0),
    (1, 0, 2), (1, 1, 1), (1, 2, 0),
    (2, 0, 1), (2, 1, 0),
    (3, 0, 0),
]