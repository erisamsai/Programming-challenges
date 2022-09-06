x = float(input('Input rods:'))
print('You input', x ,'rods.')

meters = x*5.0292
feet = meters/0.3048
furlongs = x/40
miles = meters/1609.34
time = miles/3.1*60

print('Meters:', meters,
      'Feet:', feet,
      'Miles:', miles,
      'Furlongs:', furlongs,
      'Minutes to walk', x, 'rods:', time)
