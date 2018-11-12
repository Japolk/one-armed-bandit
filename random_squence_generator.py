import datetime


def get_r8_seeds():
    """Get seed triplet based on microseconds system time"""

    microseconds = datetime.datetime.now().microsecond

    seeds = str(microseconds)[-7:]
    seeds = "0" * (7 - len(seeds)) + seeds

    return [int(seeds[idx:(idx + 5)]) for idx in [0, 1, 2]]


def r8_random(s1, s2, s3):
    """R8 algo"""

    s1 = ((171 * s1) % 30269)
    s2 = ((172 * s2) % 30307)
    s3 = ((170 * s3) % 30323)

    value = float(s1) / 30269.0 + float(s2) / 30307.0 + float(s3) / 30323.0
    value = (value % 1.0)

    return value, s1, s2, s3


def get_random_sequence(random_range):
    """Return list with elements between (0; 1) of length"""

    s1, s2, s3 = get_r8_seeds()

    seq = []
    for idx in range(3):
        val, s1, s2, s3 = r8_random(s1, s2, s3)
        seq.append(int(val * (random_range-1) + 1))
    return seq