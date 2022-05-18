import pgzrun
gennaro=Actor('gennaro',(400, 300))
WIDTH=800
HEIGHT=600

sound= tone.create('D7', 0.5)

def draw():
    screen.clear()
    gennaro.draw()

def update():
   if keyboard.left:
    gennaro.x-=1
   elif keyboard.right:
    gennaro.x+=1
   if keyboard.up:
    gennaro.y-=1
   elif keyboard.down:
    gennaro.y+=1

def on_mouse_down(pos):
   if gennaro.collidepoint(pos):
       set_gennaro_hit()
       print("SWUSH")
   else:
       print("eheh")

def set_gennaro_hit():
   gennaro.image= "megacalcio"
   clock.schedule_unique(set_gennaro_normal, 0.2)
   sound.play()

def set_gennaro_normal():
    gennaro.image= "gennaro"
pgzrun.go()