A1 = "DerWolfunddiesiebenGeisslein"
A2 = "DieHeinzelmaennchen"
A3 = "Rumpelstilzchen"
A4 = "DieBremerStadtmusikanten"
A5 = "HansimGlueck"


def w(letter, split=True):
    result = str(ord(letter.lower()) - 96)
    if len(result) == 1 or not split:
        return int(result)
    return [int(x) for x in result]


A, B = w(A1[3])
C = w(A1[16])
D, E = w(A1[24])
F, G = w(A1[len(A1)-1])

H, I = (int(z) for z in str(sum(
    [int(y) for y in f'{w(A2[3], 0)}{w(A2[7], 0)}{w(A2[14], 0)}{w(A2[len(A2)-1], 0)}'])))

J, K = [int(x) for x in str(len(A3))]

L, M, N = [int(x) for x in str(len(A4) * 5)]

O, P = w(A5[3])
Q = w(A5[6])
R = w(A5[10])

print(
    f'A={A}, B={B}, C={C}, D={D}, E={E}, F={F}, G={G}, H={H}, I={I}, '
    f'J={J}, K={K}, L={L}, M={M}, N={N}, O={O}, P={P}, Q={Q}, R={R}'
)

S = L + I + Q - B - R
T = H * C + A
U = P / B + K
V = Q - D
W = I / H
X = (R + Q + A + B) / R

print(f'S={S}, T={T}, U={U}, V={V}, W={W}, X={X}')
print(f'N 51° 5{G}.{S}{T}{int(U)} E 12° 4{N}.{V}{int(W)}{int(X)}')
