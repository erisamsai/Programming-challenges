rods = float(input('Input rods:'))
print(f"You input {rods} rods.")

def rods_to_meters(rods):
      return rods * 5.0292

def meters_to_miles(meters):
      return meters / 1609.34   

meters = rods_to_meters(rods)
miles = meters_to_miles(meters)
feet = meters/0.3048
furlongs = rods / 40
time = miles/3.1*60

print(f"Meters: {meters}", '\n',
      f"Feet: {feet}", '\n',
      f"Miles: {miles}", '\n',
      f"Furlongs: {furlongs}", '\n',
      f"Minutes to walk {rods} rods: {time}")
