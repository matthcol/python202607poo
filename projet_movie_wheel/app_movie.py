from movie import Mo_vie


# m = Movie()
m1 = Mo_vie(title="La bataille de Gaulle: L'âge de fer", year=2026, duration=160)
m2 = Mo_vie(title='Les Tuche 4', year=2021)

movies = [m1, m2]

for m in movies:
    print(m) # str
    print(str(m))
    print(f"Hier, j'ai vu {m}") # str
    print(repr(m))
    print('title:', m.title)
    print('year:', m.year)
    print('duration:', m.duration if m.duration is not None else 'NA')
    print()

print('Longueur:', len(m2))
m2.duration = 101 # '1h41'
print(m2)
print('Longueur:', len(m2))


for m in movies:
    if 'tuche' in m:
        print('[Found]', m)
    # else:
    #     print('[Skip]', m)

print(2021 in m2)
print(m2 == 'un ventilateur')

h_m = m2.durationHourMinute()
if h_m is not None:
    h, m = h_m
    print(f"{h}h{m}mn")


hm_list = [m.durationHourMinute() for m in movies if m.duration]
print(hm_list)

# movies.duration_hour_minute() # unknown method
