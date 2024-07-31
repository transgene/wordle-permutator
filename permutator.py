import itertools


available_letters = 'qwetyiopasdfghjkzcvb'
exclusions = {'e': (5,), 'i': (3,), 'o': (1, 2, 3), 'd': (1, 4, 5)}


vowels = 'aeiou'.upper()
available_letters = sorted(available_letters.upper())
exclusions = {k.upper(): v for k, v in exclusions.items()}
combinations = itertools.product(available_letters, repeat=5)

filtered_combs = []
for c in combinations:
    if not(exclusions.keys() <= set(c)):
        continue
    if c[0] == c[1] and c[0] not in vowels:
        continue
    for i in range(0, 5):
        excl_positions = exclusions.get(c[i], ())
        if i+1 in excl_positions:
            break
    else:
        filtered_combs.append(c)


for c in filtered_combs:
    print(' '.join(c))
    
print(len(filtered_combs))