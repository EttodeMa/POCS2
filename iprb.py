def dom_prob(k, m, n):
    tot_pop = k + m + n
    dom = (
        1 - (n * (n - 1) + n * m + 0.25 * m * (m - 1)) / (tot_pop * (tot_pop - 1))
    )
    return dom


with open("C:/Users/ettod/Downloads/rosalind_iprb.txt") as population:
    P = population.readlines()
k = P[0].strip()
m = P[1].strip()
n = P[2].strip()

prob = dom_prob(k, m, n)
print(prob)
