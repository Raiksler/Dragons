#!/usr/bin/env python3

import names_data
from place import place_select
import random


def choise_name(): # Выбор первого имени дракона и прозвища. Собирается из частей.
  block_from = 0
  abillity_surname = 0
  name = random.choice(names_data.name_first) + random.choice(names_data.name_second)
  if random.randrange(1,100) >= 30:
    surname = random.choice(names_data.surname)
  else:
    surname = random.choice(names_data.surname_power_first) + random.choice(names_data.surname_power_second)
    if random.randrange(1,100) >= 75:
      surname = surname + random.choice(names_data.constructions) + name + ' ' + random.choice(names_data.surname)
  result = name + ' ' + surname
  

  if (surname[-1] == 'а' or surname[-1] == 'ь' or surname == 'Защитник') and random.choice([0, 1]) == 1: # Условие, определяющее, будет ли дракон иметь привязку к месту и т.д.
    result = result + ' ' + random.choice(names_data.ending_a)
    if surname == 'Легенда' or surname == 'Гроза':
      block_from = 1 

  if surname[-7:] == 'Потомок':
    result = result + ' ' + random.choice(names_data.name_first) + random.choice(names_data.name_second) + 'а'

  if (surname[-2:] == 'из' or surname[-7:] == 'Легенда' or surname[-5] == 'Гроза') and block_from == 0:
    result = result + ' ' + place_select()
    
    
  return result

i = 1
while i <= 15:
  print(choise_name())
  i += 1 
  