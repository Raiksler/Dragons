import names_data
from random import choice

def place_select():
  type = choice([1, 2, 3])
  if type == 1:
    result = choice(names_data.place_adjective_a) + ' ' + choice(names_data.place_noun_a)
  if type == 2:
    result = choice(names_data.place_adjective_b) + ' ' + choice(names_data.place_noun_b)
  if type == 3: 
    result = choice(names_data.place_noun_b)

  return result 