import random, datetime, time, sys, signal, shutil

global x, y, best_distance, maxx, maxy
x, y = 1,0
maxx = shutil.get_terminal_size().lines
maxy = shutil.get_terminal_size().columns
move = 0
best_distance = [0,0]

def setBestDistance(x,y):
    global best_distance
    if (x + y) > (sum(best_distance)):
        best_distance[0] = x
        best_distance[1] = y

def ch_xplus():
    global x, maxx
    if x < maxx-1:
        x+=1
    else:
        x-=1

def ch_yplus():
    global y, maxy
    if y < maxy-1:
        y+=1
    else:
        y-=1

def ch_xminus():
    global x
    if x>1:
        x-=1
    else:
        x+=1

def ch_yminus():
    global y
    if y>0:
        y-=1
    else:
        y+=1

def draw(x,y):
    for i in range(x):
        print("\033[{};{}f■".format(x,y))

def handler(signum, frame):
        input("\033[{};{}fDONE!! [press ENTER]\033[{};{}fDistance traveled : {}\033[{};{}fBest distance : ({},{})".format(x,y+50,x+1,y+50,move,x+2,y+50,best_distance[0],best_distance[1]))
        exit(1)
 
signal.signal(signal.SIGINT, handler)
direction = {0:ch_xminus,1:ch_yminus,2:ch_xplus,3: ch_yplus}
random.seed(datetime.datetime.now().timestamp())
print("\033[2J")

while True:
    time.sleep(.02)
    print("\033[{}m".format(random.randint(30, 39)),end="",flush=True)
    direction.get(random.randint(0, 3))()
    setBestDistance(x, y)
    draw(x, y)
    print("\033[{};{}f\033[0m({},{})".format(1,198,x,y), end="", flush=True)
    move+=1
