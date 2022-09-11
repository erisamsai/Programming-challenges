from tabulate import tabulate
import numpy as np
import array as arr

richter = [1.0, 5.0, 9.1, 9.2, 9.5]
richter = np.asarray(richter)

def richter_to_energy(richter):
    return 10**((1.5*richter[0:1]) + 4.8)

def energy_to_tnt(energy):
    return richter_to_energy(energy) / (4.184*10**9)

energy = richter_to_energy(richter[0:1])
tnt = energy_to_tnt(energy)


data = [[richter[0:1], richter_to_energy(richter[0:1]), energy_to_tnt(richter[0:1])],
        [richter[1:2], richter_to_energy(richter[1:2]), energy_to_tnt(richter[1:2])],
        [richter[2:3], richter_to_energy(richter[2:3]), energy_to_tnt(richter[2:3])],
        [richter[3:4], richter_to_energy(richter[3:4]), energy_to_tnt(richter[3:4])],
        [richter[4:5], richter_to_energy(richter[4:5]), energy_to_tnt(richter[4:5])],
        ]

col_names = ['Richter', 'Joules', 'TNT']
print(tabulate(data, headers=col_names))

richter_value = float(input('Please enter a Richter value:'))

def richter_to_energy(richter_value):
    return 10**((1.5*richter_value) + 4.8)

print(f'Richter value: {richter_value}', '\n')
print(f'Equivalent in joules: {richter_to_energy(richter_value)}', '\n',
      f'Equivalent in tons of TNT: {energy_to_tnt(richter_to_energy(richter_value))}')