K = 400

while K != 0:
    K -= 1
    if K % 2 != 1:
        continue
    if K % 3 != 1:
        continue
    if K % 4 != 1:
        continue
    if K % 5 != 1:
        continue
    if K % 6 != 1:
        continue
    if K % 7 == 0:
        print(f'K: {K}')
        print(f'N 51°52.{K+140} E 012°38.{3*K-40}')
        continue
