import settings
import time
from functools import partial
import winsound
import threading
import random
def percentage_width(per):
    return (settings.WIDTH /100) * per

def percentage_heigth(per):
    return (settings.HEIGTH /100) * per



#def status_check():
def check_neighbours(komorki,x,y):
    live_neigh = 0
    for row in range(max(0,x-1),min(settings.GRID_SIZE,x+2)):
        for column in range(max(0,y-1),min(settings.GRID_SIZE,y+2)):
            if row == x and column ==y:
                continue
            if komorki[row][column].state == 'alive':
                live_neigh +=1

    return live_neigh

def new_generation(komorki):
    #inicjuje liste podstawionymi wartosciami
    new_komorki = [[False for _ in range(settings.GRID_SIZE)] for _ in range(settings.GRID_SIZE)]
    for row in range(settings.GRID_SIZE):
        for column in range(settings.GRID_SIZE):
            num_of_neighbours = check_neighbours(komorki,row,column)
            state = komorki[row][column].state
            if (state == 'alive' and (num_of_neighbours == 2 or num_of_neighbours == 3)):
                new_komorki[row][column] = 'alive'
            elif state == 'dead' and (num_of_neighbours==3) :
                new_komorki[row][column] = 'alive'
            elif((state == 'alive') and (num_of_neighbours>3 or num_of_neighbours<2)):
                new_komorki[row][column] = 'dead'
            else:
                new_komorki[row][column] = 'dead'

    for row in range(settings.GRID_SIZE):
        for column in range(settings.GRID_SIZE):
            komorki[row][column].state = new_komorki[row][column]
            komorki[row][column].update_button()


def import_sound():
    winsound.PlaySound('chemia_nowej_ery.wav', winsound.SND_FILENAME)

def start_game(root,komorki,label):
    sound_thread = threading.Thread(target=import_sound)
    sound_thread.start()
    settings.is_running = True
    game_loop(root,komorki,label)


def stop_game():
    settings.is_running=False
    print(settings.is_running)

def game_loop(root, komorki,label):
    new_generation(komorki)
    if settings.is_running == True:
        settings.generation +=1
        label.configure(text = f"Generation: {settings.generation}")
        root.after(200,partial(game_loop,root, komorki,label))

def randomize_grid(komorki):
    settings.generation = 0
    for row in range(settings.GRID_SIZE):
        for column in range(settings.GRID_SIZE):
            komorki[row][column].state = random.choice(['dead','alive','dead','dead','dead','dead'])
            komorki[row][column].update_button()





