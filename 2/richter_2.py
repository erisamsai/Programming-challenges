
richter = [1.0, 5.0, 9.1, 9.2, 9.5]

def richter_to_energy(richter):
    return 10**((1.5*richter) + 4.8)

def energy_to_tnt(energy):
    return richter_to_energy(energy) / (4.184*10**9)

if __name__ == '__main__':
    for value in richter:
        print(f"{value:<5}{richter_to_energy(value):<30}{energy_to_tnt(value):<30}")

richter_value = float(input('Please enter a Richter value: '))

print(f' Richter value: {richter_value}', '\n',
      f'Equivalent in joules: {richter_to_energy(richter_value)}', '\n',
      f'Equivalent in tons of TNT: {energy_to_tnt(richter_value)}')