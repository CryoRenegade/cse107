# @file winds.py
# @author Jacob Ledbetter, Jareth Tipton
# @description Describes wind on the Beaufort scale

wind = int(input("Please enter the speed of the wind (in knots): "))

if wind == 0:
    print("There is a Calm in your area")
elif wind >= 1 and wind <= 3:
    print("There is a Light Air in your area")
elif wind >= 4 and wind <= 27:
    print("There is a Breeze in your area")
elif wind >= 28 and wind <= 47:
    print("There is a Gale in your area")
elif wind >= 48 and wind <= 63:
    print("There is a Storm in your area")
elif wind > 63:
    print("There is a Hurricane in your area... SHELTER IN PLACE!!!")
else:
    print("Error:", wind, " is not a valid wind speed.")
