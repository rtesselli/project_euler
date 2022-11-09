import utils.number_theory as nt


def problem50():
    limit = 1000000
    primes = nt.sieve_of_atkin(limit)
    primes_set = set(primes)
    max_terms = 0
    best_value = 0
    for idx, start in enumerate(primes):
        odd = start % 2 == 1
        cumsum = start
        terms = 1
        for next_prime in primes[idx + 1:]:
            cumsum += next_prime
            terms += 1
            odd = not odd
            if odd and cumsum in primes_set:
                if terms > max_terms:
                    best_value = cumsum
                    max_terms = terms
            if cumsum > limit:
                break
    return best_value
