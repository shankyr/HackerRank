

n, hit, t = map(int, raw_input().strip().split(' '))

monsters = map(int, raw_input().strip().split(' '))

monsters.sort()

jason_energy = hit * t
max_monsters_killed = 0

for m in monsters:
    hit_counter = 0
    if m <= jason_energy:
        max_monsters_killed += 1

        hit_counter = m / hit
        if m % hit != 0:
            hit_counter += 1

        jason_energy -= hit * hit_counter

    else:
        break

print max_monsters_killed
