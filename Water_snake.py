from tkinter import*
from tkinter import messagebox
import random

import pygame
from pygame import mixer

check = 0
score = 0

class Snake:

    def __init__(self):
        global photo1
        self.width = 600
        self.height = 400
        self.snake_size = 20
        self.fish = [0,0]

        self.cells = [[self.snake_size*2, self.snake_size],
                      [self.snake_size, self.snake_size]]

        s.create_image(self.cells[0][0], self.cells[0][1], image=photo1, anchor=NW)
        s.create_image(self.cells[1][0], self.cells[1][1], image=photo1, anchor=NW)

        #как будут изменятся направления головы
        self.moving = {"Вниз": (0, self.snake_size), "Вправо": (self.snake_size, 0),
                        "Вверх": (0, -self.snake_size), "Влево": (-self.snake_size, 0)}

        self.direction = self.moving["Вправо"]

    def run(self):
        #закрашиваем последнюю ячейку, при передвижении змейки
        index = len(self.cells)-1
        s.create_rectangle(self.cells[index][0], self.cells[index][1],
                           self.cells[index][0]+ self.snake_size, self.cells[index][1]+ self.snake_size, fill='paleturquoise', outline = 'paleturquoise')

        for i in range(index, 0, -1):
            self.cells[i][0]= self.cells[i-1][0] #сдвигаются координаты яеек с последней до второй
            self.cells[i][1] = self.cells[i-1][1]

        self.cells[0][0] = self.cells[0][0] + self.direction[0] #расчитываются новые координаты  первой ячейки
        self.cells[0][1] = self.cells[0][1] + self.direction[1]

        s.create_image(self.cells[0][0], self.cells[0][1], image=photo1, anchor=NW)

    #обрабатываю нажатие клавиш, соответствующеее направление(в противоположное направление двигаться нельзя)
    def modific(self, key):
        if key.keycode == 37 and  self.direction != self.moving['Вправо']:  #запрещаем идти в противоположное направление
            self.direction = self.moving['Влево']
        elif key.keycode == 38 and self.direction != self.moving['Вниз']:
            self.direction = self.moving['Вверх']
        elif key.keycode == 39 and self.direction != self.moving['Влево']:
            self.direction = self.moving['Вправо']
        elif key.keycode == 40 and self.direction != self.moving['Вверх']:
            self.direction = self.moving['Вниз']

    #рандомно ставит одну рыбку
    def make_fish(self):
        global photo
        self.fish[0] = self.snake_size * random.randint(1, (self.width - self.snake_size)/self.snake_size) #рандомно выбераю клетку  и умножаю, чтобы найти координаты
        self.fish[1] = self.snake_size * random.randint(1, (self.height - self.snake_size)/self.snake_size)
        s.create_image(self.fish[0], self.fish[1] , image=photo, anchor=NW)


def main():
    global score
    global  check
    if check == 0:
        m.run()
        #запрет на выход змейки из границ
        if m.cells[0][0] + m.snake_size  > m.width or  m.cells[0][0]<0 or  m.cells[0][1] + m.snake_size > m.height or  m.cells[0][1] < 0:
            check = 1
        #ловит рыбку
        elif m.cells[0][0] == m.fish[0] and m.cells[0][1] == m.fish[1]:
            m.cells.append([0,0])
            m.make_fish()
            score+=1
            sound.play()
            b = 'Водная змея            Ваш результат: '+str(score)
            window.title(b)
        else:
            for i in range(1, len(m.cells)):
                if m.cells[i][0] == m.cells[0][0] and m.cells[i][1] == m.cells[0][1]:
                    check = 2

        window.after(200, main)
    elif check == 1:
        messagebox.showinfo('Игра закончена', 'ойй!!!')
    elif check == 2:
        messagebox.showinfo('Игра закончена', 'ОТКУСИЛ СЕБЕ ХВОСТ!!!')

a = 'Водная змея            Ваш результат:'
window = Tk()
window.title(a)

photo = PhotoImage(file='fish1.gif')
photo1 = PhotoImage(file='head.gif')

s = Canvas(window, width=600, height=400, bg="paleturquoise")
s.grid()
m = Snake()
s.focus_set()
s.bind('<Key>', m.modific)

mixer.init()
sound = pygame.mixer.Sound('STAPLER.wav')
 
mixer.music.load('music.mp3')
mixer.music.play(-1)

m.make_fish()
main()
window.mainloop()

