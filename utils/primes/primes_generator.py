"""
Sieve of Eratosthenes
Code by David Eppstein, UC Irvine, 28 Feb 2002
http://code.activestate.com/recipes/117119/
"""


def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    map_primes: dict = {}

    # The running integer that's checked for primeness
    num: int = 2

    while True:
        if num not in map_primes:
            # num is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield num
            map_primes[num * num] = [num]
        else:
            # num is composite. D[num] is the list of primes that
            # divide it. Since we've reached num, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in map_primes[num]:
                map_primes.setdefault(p + num, []).append(p)
            del map_primes[num]

        num += 1
