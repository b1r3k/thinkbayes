# -*- coding: utf-8 -*-
import thinkbayes2 as thinkbayes

print('\nCookie problem')
print('-' * 25)


def solve_bayes(priori, update):
    pmf = thinkbayes.Pmf()
    for hypo, prob in priori.items():
        pmf.Set(hypo, prob)

    for hypo, prob in update.items():
        pmf.Mult(hypo, prob)
    pmf.Normalize()
    return pmf


priori = {
    'Bowl 1': 0.5,
    'Bowl 2': 0.5
}
update = {
    'Bowl 1': 0.75,
    'Bowl 2': 0.5
}

print(solve_bayes(priori, update).Prob('Bowl 1'))

print('\nMonty Hall problem 1')
print('-' * 25)

pmf = thinkbayes.Pmf()

# X - probability that car is behind X
# H - car is behind Y
# D - In this case D consists of two parts: Monty chooses Door B and there is no car there.

pmf.Set('A', 1 / 3)
pmf.Set('B', 1 / 3)
pmf.Set('C', 1 / 3)

pmf.Mult('A', 0.5)  # P(D|H)
pmf.Mult('B', 0)
pmf.Mult('C', 1)

# inaczej mowiac, Prawd. że D (wybierze B a środku nie ma samochodu) jeśli samochód jest w A. Skoro samochód jest w A, wybiera między B i C

pmf.Normalize()
print(pmf.Prob('A'))

print('\nMonty Hall problem 2')
print('-' * 25)

pmf = thinkbayes.Pmf()

# X - probability that car is behind X
# H - car is behind Y
# D - Monty always chooses B if he can, and only chooses C if he has to (because the car is behind B)

pmf.Set('A', 1 / 3)
pmf.Set('B', 1 / 3)
pmf.Set('C', 1 / 3)

pmf.Mult('A', 1)  # P(D|H)
pmf.Mult('B', 0)
pmf.Mult('C', 1)

pmf.Normalize()
print(pmf.Prob('A'))

print('\nExercise: iterative cookie problem')
print('-' * 25)

# But in the more likely scenario where we eat the cookies we draw,
# the likelihood of each draw depends on the previous draws.
# Modify the solution in this chapter to handle selection without replacement

bowl1_count = [30, 10]
bowl2_count = [20, 20]

# P(B1|V) - Vanilla cookie from Bowl 1
# P(V|B1) - Vanilla cookie given Bowl 1

priori = [0.5, 0.5]
for i in range(0, 3):
    update = [bowl1_count[0] / sum(bowl1_count), bowl2_count[0] / sum(bowl2_count)]
    pmf = solve_bayes(dict(A=priori[0], B=priori[1]), dict(A=update[0], B=update[1]))
    print('Bowl state#%s: %s' % (i, update))
    print('Cookie iteration#%s: %s' % (i, pmf.Prob('A')))
    bowl1_count = [bowl1_count[0] - 1, bowl1_count[1]]


print('\nExercise: mammography problem')
print('-' * 25)

# 1% of women at age forty who participate in routine screening have breast cancer.
# 80% of women with breast cancer will get positive mammographies.
# 9.6% of women without breast cancer will also get positive mammographies.
# A woman in this age group had a positive mammography in a routine screening.
# What is the probability that she actually has breast cancer?


# probability that has cancer given positive mammography

pmf = solve_bayes(dict(Cancer=0.01, NoCancer=0.99), dict(Cancer=0.8, NoCancer=0.096))
print('Probability that women has cancer %s %.4f' % (pmf.Prob('Cancer'), (1 / 826.)*100))
