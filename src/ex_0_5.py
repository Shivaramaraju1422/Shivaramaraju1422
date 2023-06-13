"""
ex_0_5.py
"""


def ground_cover(min_soil_temp):
    return int(min_soil_temp[2])


def depth(min_soil_temp):
    return int(min_soil_temp[3])


min_soil_temp = 'SN05'
print(ground_cover(min_soil_temp))
print(depth(min_soil_temp))

# SN*# = Minimum soil temperature (tenths of degrees C)
# 	          where * corresponds to a code
# 	          for ground cover and # corresponds to a code for soil
# 		  depth.

# 		  Ground cover codes include the following:
# 		  0 = unknown
# 		  1 = grass
# 		  2 = fallow
# 		  3 = bare ground
# 		  4 = brome grass
# 		  5 = sod
# 		  6 = straw multch
# 		  7 = grass muck
# 		  8 = bare muck

# 		  Depth codes include the following:
# 		  1 = 5 cm
# 		  2 = 10 cm
# 		  3 = 20 cm
# 		  4 = 50 cm
# 		  5 = 100 cm
# 		  6 = 150 cm
# 		  7 = 180 cm
