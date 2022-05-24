import random

easy_scales = ['C Major', 'C Natural Minor', 'C Harmonic Minor', 'C Melodic Minor',
               'G Major', 'G Natural Minor', 'G Harmonic Minor', 'G Melodic Minor',
               ]

practice_scale = random.choice(scales) + ' ' + random.choice(modes)
print(practice_scale)