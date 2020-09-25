A = 0  # Geocache
B = 0  # Multicache
C = 0  # Fragezeichen
D = 0  # Weltkugel
E = 0  # Geist
F = 0  # Briefumschlag
G = 0  # Kamera
H = 0  # Mega
I = 0  # Coin
J = 0  # Blauer Pfeil

for A in range(1, 10):
    for B in range(1, 10):
        for C in range(1, 10):
            for D in range(1, 10):
                for E in range(0, 10):
                    for F in range(0, 10):
                        for G in range(1, 10):
                            for H in range(1, 10):
                                for I in range(0, 10):
                                    for J in range(0, 10):
                                        if (A+B+C+D+E+F+G+H+I+J) == 0:
                                            continue
                                        #print('%s - %s - %s - %s - %s - %s - %s - %s - %s' % (
                                        #    int(f'{A}{B}{C}'),
                                        #    int(f'{D}{E}{F}'),
                                        #    int(f'{B}{G}{I}'),
                                        #    int(f'{D}{J}{A}'),
                                        #    int(f'{G}{D}{F}'),
                                        #    int(f'{H}{C}{C}'),
                                        #    int(f'{G}{A}{D}'),
                                        #    int(f'{H}{A}{G}'),
                                        #    int(f'{C}{G}{H}')
                                        #))
                                        if int(f'{A}{B}{C}') + int(f'{D}{E}{F}') != int(f'{B}{G}{I}'):
                                            continue
                                        if int(f'{D}{J}{A}') + int(f'{G}{D}{F}') != int(f'{H}{C}{C}'):
                                            continue
                                        if int(f'{G}{A}{D}') + int(f'{H}{A}{G}') != int(f'{C}{G}{H}'):
                                            continue
                                        if int(f'{A}{B}{C}') + int(f'{D}{J}{A}') != int(f'{G}{A}{D}'):
                                            continue
                                        if int(f'{D}{E}{F}') + int(f'{G}{D}{F}') != int(f'{H}{A}{G}'):
                                            continue
                                        if int(f'{B}{G}{I}') + int(f'{H}{C}{C}') != int(f'{C}{G}{H}'):
                                            continue
                                        print(f'N 51° 53.{A}{F}{J} E 012° 39.{E}{J}{C}')
