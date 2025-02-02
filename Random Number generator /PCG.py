def pcg(seed, multiplier=6364136223846793005, increment=1442695040888963407):
    while True:
        seed = seed * multiplier + increment
        yield seed
