def win_chill_calculated(t,v):
    return 35.74 + 0.6215* t - 35.75 * (v**0.16) + 0.4275 - t * (v ** 0.16) # formula to calculate Windchill

def converts_metric(temperature): 
    return (temperature * 9 / 5) + 32 # C to F Formula

#user inputs temperature and (F/C )
user_input_tem=float(input("What is the temperature?: "))
user_input_metric=input("Fahrenheit or Celsius (F/C)?")

if user_input_metric.upper() == "F":
    user_input_metric= converts_metric(user_input_tem)

wind = 5

for i in range(12):
    wind_chill= win_chill_calculated(user_input_tem, wind)
    print(f"At temperature {user_input_tem}F, and wind speed {wind} mph, the windchill is: {wind_chill:.2f}F")
    wind += 5