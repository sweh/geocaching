import sys


def increase():
    global A, B, C, e, f, d

    if A + B + C + e + f + d < 200:
        A += 1
    elif B > 1:
        A = 19
        B -= 1
    elif C < 200:
        A = 19
        B = 1
        C += 1
    else:
        return True


for e in range(1, 20):
    for f in range(1, 20):
        for d in range(1, 20):
            if e <= f:
                continue
            if f <= d:
                continue
            A = 19
            B = 9
            C = 1
            while True:
                if A + B != d*d:
                    if increase():
                        break
                    continue

                if B + C != f*f:
                    if increase():
                        break
                    continue

                if A + C != e*e:
                    if increase():
                        break
                    continue

                if A + B + C + e + f + d >= 200:
                    if increase():
                        break
                    continue

                qs = sum([int(i) for i in str(A + B + C + e + f + d)])
                if qs != 11:
                    if increase():
                        break
                    continue

                if A <= 18 or B >= 10 or e >= 20 or e <= f or f <= d:
                    if increase():
                        break
                    continue

                print(f'A: {A} B: {B} C: {C} d: {d} e: {e} f: {f}')
                print(f'N51°53.{A+(C*7)+d-e-f} E012°39.{A+C+e+f}')
                sys.exit()
