segunda = {'Bruno': 1, 'pedro': 0, 'Luiz': 0}
plant_seg = []

for i in segunda:
    if segunda[i] == 1:
        plant_seg.append(i)

print(plant_seg)

#### NOVA SEMANA ####

terca = {'Bruno': 0, 'pedro': 1, 'Luiz': 1}
plant_terca = []

for j in terca:
    if j in plant_seg and terca[j] == 1:
        plant_terca.append(j)


print(plant_terca)