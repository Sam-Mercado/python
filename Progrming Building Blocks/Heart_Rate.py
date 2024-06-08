#When you physically exercise to strengthen your heart, you should maintain
#your heart rate within a range for at least 20 minutes. To find that range,
#subtract your age from 220. This difference is your maximum heart rate '
#per minute. Your heart simply will not beat faster than this maximum (220 − age).
#When exercising to strengthen your heart, you should keep your heart rate 
#between 65% and 85% of your heart’s maximum rate.

age = int(input('Please enter your age:'))
heart_rate = 220 - age
max_HRxmin = heart_rate
minHR_percentage = int(max_HRxmin * 65 / 100) 
maxHR_percentage = int(max_HRxmin * 85 / 100)

print('When you exercise to strengthen your heart, you should keep your heart rate between {} and {} beats per minute.'.format(minHR_percentage , maxHR_percentage))

