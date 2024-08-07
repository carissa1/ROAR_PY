
f = open('../../ROAR_Competition/track_boundaries.txt')
f2 = open('new_bounds.txt', 'w')
for line in f.readlines():
    f2.write(line[1:(len(line)-2)])
    f2.write('\n')
