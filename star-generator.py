import random

d = 0

while d < 3000:
    s = random.randint(1, 3)
    t = random.randint(290, 310)
    r = random.randint(30, 35)
    
    print('        <div class="star hero-star" style="--s:' + str(s) + 'px; --p:' + str(t) + 's; --d:-' + str(d) + 's; --r:-' + str(r) + 'vh"></div>')
    
    d += 30