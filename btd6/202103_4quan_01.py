import pyautogui
import time
from PIL import ImageGrab

class Game:
    def time(self):
        t = time.time() - self.start
        print(t)
        return t
    
    def upgrade_available(self, point):
        color = ImageGrab.grab().getpixel(point)
        if abs(color[0]-80)<20 and abs(color[1]-220)<20 and abs(color[2]-0)<20:
            return True
        else:
            return False
        
    def create_available(self):
        color = ImageGrab.grab().getpixel(self.cancel_point)
        for i in range(3):
            if abs(color[i] - 255) > 10:
                return False
        return True
    
    def press(self, k, count=1):
        for i in range(count):
            pyautogui.press(k)
            time.sleep(self.interval)
        
    def move(self, x, y, d=0.03):
        pyautogui.moveTo(x, y, duration=d)
        time.sleep(self.interval)
        
    def click(self):
        pyautogui.click()
        time.sleep(self.interval)
        
    def create_force(self, tid):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        self.press(tower[2])
        self.click()      
        
    def create(self, tid):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        while (not self.create_available()):
            self.press(tower[2])
        self.click()  
        
    def change_attack(self, tid, a):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        self.press('tab', a)
        self.press('esc')
        
    def upgrade_force(self, tid, a, b, c):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        self.press(',', a)
        self.press('.', b)
        self.press('/', c)
        self.press('esc')
        
    def upgrade(self, tid, a, b, c):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        left_right = 0 if tower[0] >= self.mid_x else 1
        for i in range(a):
            while not self.upgrade_available(self.upgrade_points[left_right][0]):
                time.sleep(self.interval)
            self.press(',')
        for i in range(b):
            while not self.upgrade_available(self.upgrade_points[left_right][1]):
                time.sleep(self.interval)
            self.press('.')
        for i in range(c):
            while not self.upgrade_available(self.upgrade_points[left_right][2]):
                time.sleep(self.interval)
            self.press('/')
        self.press('esc')
        
    def remove(self, tid):
        tower = self.towers[tid]
        self.move(tower[0], tower[1])
        self.click()
        self.press('backspace')
        
    def clean(self, tid):
        trash = self.trash[tid]
        self.move(trash[0], trash[1])
        self.click()
        self.move(trash[2], trash[3])
        self.click()
        
    def go(self):
        self.press('space')
    
    def go_speed(self, level):
        if self.speed == 1:
            self.go()
        pyautogui.keyDown('shift')
        for i in range(level - self.current):
            self.press('space')
        pyautogui.keyUp('shift')
        self.current = level
        if self.speed == 1:
            self.go()
        
    def change_speed(self):
        self.go()
        self.speed = 1 - self.speed
    
    def run(self):
        # params
        self.interval = 0.002
        # boards
        self.upgrade_points = [[(181, 367), (181, 461), (181, 564)], [(993, 367), (993, 461), (993, 564)]]
        self.mid_x = 555
        self.cancel_point = (1066, 118)
        # positions
        self.towers = [(323, 600, 'u'), (82, 603, 't'), 
                       (713, 469, 'v'), (713, 369, 'v'),
                       (692, 527, 't'), (749, 520, 't'), 
                       (815, 443, 't'), (453, 144, 't'),
                       (573, 386, 'y'), (424, 371, 'v'),
                       (514, 456, 'v')]
        self.trash = [(0, 0, 0, 0)]
        # function
        self.start = time.time()
        self.speed = 0
        self.current = 0
        # c 230 start
        self.create(0)
        self.create(1)
        self.go_speed(13)
        self.create(2)
        self.change_attack(2, 2)
        self.go_speed(16)
        self.upgrade(2, 0, 2, 0)
        self.go_speed(22)
        time.sleep(2)
        self.remove(1)
        self.upgrade(2, 0, 1, 0)
        self.go_speed(30)
        self.upgrade(2, 1, 0, 0)
        self.create(4)
        self.upgrade(4, 2, 0, 0)
        self.go_speed(40)
        self.upgrade(4, 1, 2, 0)
        self.create(3)
        self.change_attack(3, 2)
        self.upgrade(3, 0, 3, 0)
        self.upgrade(3, 1, 0, 0)
        self.go_speed(49)
        self.create(5)
        self.upgrade(5, 3, 2, 0)
        self.go_speed(55)
        self.create(6)
        self.upgrade(6, 3, 2, 0)
        self.create(8)
        self.upgrade(8, 0, 2, 0)
        self.go_speed(80)
        self.upgrade(8, 0, 2, 0)
        self.upgrade(8, 2, 0, 0)
        time.sleep(3)
        self.remove(2)
        self.remove(3)
        self.remove(4)
        self.remove(5)
        self.remove(6)
        self.upgrade(8, 0, 1, 0)
        self.press('2')
        self.interval = 0.3
        self.create(7)
        self.upgrade(7, 0, 4, 0)
        self.upgrade(7, 2, 0, 0)
        self.create(9)
        self.change_attack(9, 3)
        self.upgrade(9, 0, 3, 1)
        self.remove(8)
        self.upgrade(9, 0, 1, 0)
        self.create(10)
        self.change_attack(10, 3)
        self.upgrade(10, 0, 3, 1)
        
        
        
        
#        self.change_speed()
        

game = Game()
game.run()
