def mwc(seed, a=4294957665, m=2**32):
    c = 12345  # Initial carry value
    while True:
        seed = (a * seed + c) % m
        c = (a * seed + c) // m
        yield seed
