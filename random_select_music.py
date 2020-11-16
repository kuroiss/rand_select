import csv
import pandas as pd
import random

level = input('please input insane level(1 ~ 25 or any, rand) : ')

if level == 'any' or level == 'rand' or level == 'all':
    level = str(random.randrange(1, 26, 1))

if '~' in level or '～' in level:
    level.replace('～', '~')
    level.replace(' ', '')
    level_split = level.split('~')
    level_split.sort()
    level = str(random.randrange(int(level_split[1]), int(level_split[0]) + 1))

df = pd.read_csv('./insane_table/insane_'+level+'.csv')
music_list = df['タイトル']
 
print(level + ' : ' + random.choice(music_list))
