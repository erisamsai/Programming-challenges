
temperature = [10, 0, -10]
speed = [15, 25, 35]

for value in temperature:
 print(f'Temperature of  and speed of {value}:')

 def wind_chill_temp():
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

air_temp = float(input('Temperature: '))
air_speed = float(input('Speed : '))
wind_chill_temp = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

print(f'Windchill: {wind_chill_temp}')

