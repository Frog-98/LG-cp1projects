#Lincoln Girot, Crew Shares

import random

number_of_pirates = int(input("How many pirates are there?"))

units = random.randint(500, 5000)

yondu_share = round(units*0.13,2)
remaining_units = units - yondu_share

peter_share = round(remaining_units*0.11,2)
remaining_units -= peter_share

divided_units = round(remaining_units / number_of_pirates,2)

"""
yondu's share is 13% (times by 0.13)
peter gets 11% of what's remaining (times 0.11)
divide rest among the total crew
add quotient to peter and yondu
"""

print(f"Total stolen units = {units}")
print(f"Yondu's share is {yondu_share + divided_units}")
print(f"Peters share is {peter_share + divided_units}")
print(f"Crews share is {divided_units}")
