import random

d = 0

while d < 4000:
    s = random.randint(0, 5)
    t = random.randint(3500, 4500)
    r = random.randint(350, 420)
    
    print('        <svg class="star" style="--s:' + str(s) + 'px; --t:' + str(t) + 's; --d:-' + str(d) + 's; --r:' + str(r) + 'vh" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M496,203.3H312.36L256,32,199.64,203.3H16L166.21,308.7,107.71,480,256,373.84,404.29,480,345.68,308.7Z" fill="white"></path></svg>')
    
    d += 2