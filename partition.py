import sys
import heapq
import random
import math

FLAG = int(sys.argv[1])
ALG = int(sys.argv[2])
FILE = sys.argv[3]
IS_PRE = ALG > 3
MAX_ITER = 1000

with open(FILE) as file:
    A = []
    for num in file:
        A.append(int(num))
    N = len(A)

def get_rand_solution():
    if IS_PRE:
        return random.choices(range(N), k = N)
    else:
        return random.choices([-1, 1], k = N)

def get_rand_neighbor(S):
    S = S.copy()
    n_range = range(len(S))
    if IS_PRE:
        i = random.choice(n_range)
        j = S[i]
        while j == S[i]:
            j = random.choice(n_range)
        S[i] = j
    else:
        [i, j] = random.sample(n_range, 2)
        S[i] = -S[i]
        if random.random() < 0.5:
            S[j] = -S[j]
    return S

def residue(S):
    if IS_PRE:
        grouped_A = [0] * N
        for i in range(N):
            grouped_A[S[i]] += A[i]
        return KK(grouped_A)
    else:
        r = 0
        for i in range(N):
            r += A[i] * S[i]
        return abs(r)

def KK(A):
    H = [-x for x in A]
    heapq.heapify(H)
    while(len(H) > 1):
        x = heapq.heappop(H)
        y = heapq.heappop(H)
        heapq.heappush(H, x - y)
    return -heapq.heappop(H)

def RR():
    S = get_rand_solution()
    for _ in range(MAX_ITER):
        S_p = get_rand_solution()
        if residue(S_p) < residue(S):
            S = S_p.copy()
    return residue(S)

def HC():
    S = get_rand_solution()
    for _ in range(MAX_ITER):
        S_p = get_rand_neighbor(S)
        if residue(S_p) < residue(S):
            S = S_p.copy()
    return residue(S)

def T(iter):
    return pow(10, 10) * pow(.8, iter // 300)

def SA():
    S = get_rand_solution()
    S_pp = S.copy()
    for i in range(MAX_ITER):
        S_p = get_rand_neighbor(S)
        if residue(S_p) < residue(S):
            S = S_p.copy()
        else:
            if random.random() < pow(math.e, -(residue(S_p) - residue(S))/T(i)):
                S = S_p.copy()
        if residue(S) < residue(S_pp):
            S_pp = S.copy()
    return residue(S_pp)

if ALG == 0:
    print(KK(A))
elif ALG in [1, 11]:
    print(RR())
elif ALG in [2, 12]:
    print(HC())
elif ALG in [3, 13]:
    print(SA())


# N = 5
# A = [10, 1, 1, 1, 20]
# S = get_rand_solution()
# print(S)
# print(residue(S))

# print(KK(A))
# print(RR())
# print(HC())
# print(SA())