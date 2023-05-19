import random

d = 0

while d < 3000:
    s = random.randint(1, 3)
    t = random.randint(290, 310)
    r = random.randint(20, 25)
    
    print('        <div class="star" style="--s:' + str(s) + 'px; --t:' + str(t) + 's; --d:-' + str(d) + 's; --r:-' + str(r) + 'vh"></div>')
    
    d += 30