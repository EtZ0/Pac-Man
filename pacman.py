#__author__ = 'Meelis Tapo'
__author__ = 'Eduard'
#TODO tondid parkinsonist terveks ravida/loogika (chaser, ambusher, fickle, stupid)
#TODO tonte juurde
#TODO kaardisüsteem ümber(50*50px ruudud? i*50-25), kaardid suuremaks ja juurde
#TODO menüü taoline asjandus/hiscore/etc
#TODO nupu allavajutamisel astub 1 sammu, siis jõnksatab korraks seisma, siis liigub sujuvalt edasi, wot?
#TODO suu käima
#TODO helid (kaustas olemas die.ogg, intro.ogg)
#TODO pelletid/powerupid
#TODO loogika eraldi faili?


from tkinter import *
import time
import random

sammu_pikkus = 10
alg_pos = [275,275]
wall_pos = ([25,25], [25,75], [25,125], [25,175],[25,225], [25,275], [25,325], [25,375], [25,425], [25,475], [25,525],
            [525,25], [525,75], [525,125], [525,175],[525,225], [525,275], [525,325], [525,375], [525,425], [525,475], [525,525],
            [75,25],[125,25],[175,25],[225,25],[275,25],[325,25],[375,25],[425,25],[475,25],
            [75,525], [125,525],[175,525],[225,525],[275,525],[325,525],[375,525],[425,525],[475,525],
            [125,125], [175,125], [225,125], [275,125], [325,125], [375,125], [425,125],
            [125,425], [175,425], [225,425], [275,425], [325,425], [375,425], [425,425])

pac_pos = [alg_pos[0], alg_pos[1]]
ghost_pos = [175,275]

# loome akna
raam = Tk()
raam.title("Pacman")
raam.geometry("700x700")
tahvel = Canvas(raam, width=550, height=550, background="blue")
tahvel.grid(column=3, row=5, columnspan=5, rowspan=5, sticky=(N, S, W, E))



def samm(pos,):
    üles = [pos[0], pos[1]-sammu_pikkus]
    alla = [pos[0], pos[1]+sammu_pikkus]
    vasakule = [pos[0]-sammu_pikkus, pos[1]]
    paremale = [pos[0]+sammu_pikkus, pos[1]]
    return üles, alla, vasakule, paremale


def nool_üles(event):
    global pac_pos
    if not wall2(samm(pac_pos)[0]):
        update_pac_dir(pac_north_img)
        tahvel.move(pac_id, 0, -sammu_pikkus)
        pac_pos[1] -= sammu_pikkus
        print(pac_pos)

def nool_alla(event):
    global pac_pos
    if not wall2(samm(pac_pos)[1]):
        update_pac_dir(pac_south_img)
        tahvel.move(pac_id, 0, sammu_pikkus)
        pac_pos[1] += sammu_pikkus
        print(pac_pos)

def nool_vasakule(event):
    global pac_pos
    if not wall2(samm(pac_pos)[2]):
        update_pac_dir(pac_west_img)
        tahvel.move(pac_id, -sammu_pikkus, 0)
        pac_pos[0] -= sammu_pikkus
        print(pac_pos)

def nool_paremale(event):
    global pac_pos
    if not wall2(samm(pac_pos)[3]):
        update_pac_dir(pac_east_img)
        tahvel.move(pac_id, sammu_pikkus, 0)
        pac_pos[0] += sammu_pikkus
        print(pac_pos)

def wall(pos): # ei kasuta seda enam
    for i in range(len(wall_pos)):
        if wall_pos[i][0] == pos[0] and wall_pos[i][1] == pos[1]:
            return True
    return False

def wall2(pos):
    for wall_elem in wall_pos:
        if collision(pos, wall_elem):
            return True
    return False

def update_pac_dir(new_img):
    global pac_id
    global pac_pos
    tahvel.delete(pac_id)
    pac_id = tahvel.create_image(pac_pos[0], pac_pos[1], image=new_img)

#ruut 50px x 50 px, kus koordinaadid on ruudu keskpunktiks.
#tipud on vastava ümbrisruudu tipud (nt pos 25x25 puhul 0x0, 0x50, 50x0, 50x50)
def tipud(pos):
    tipud = []
    tipud.append([pos[0]-25, pos[1]-25]) # Ül Vas
    tipud.append([pos[0]-25, pos[1]+25]) # Al Vas
    tipud.append([pos[0]+25, pos[1]-25]) # Ül Par
    tipud.append([pos[0]+25, pos[1]+25]) # Al Par
    #külgede keskpunktid
    tipud.append([pos[0], pos[1]-25])
    tipud.append([pos[0], pos[1]+25])
    tipud.append([pos[0]-25, pos[1]])
    tipud.append([pos[0]+25, pos[1]])
    return tipud

#kontrollib 2 objekti kokkupõrget
#kontrollib kas ühe objekti mingi piirnurk asub teise objekti piirides
def collision(pos_obj1, pos_obj2):
    tipud_obj1 = tipud(pos_obj1)
    for elem in tipud_obj1:
        if elem[0] > pos_obj2[0]-25 and elem[0] < pos_obj2[0]+25:
            if elem[1] > pos_obj2[1]-25 and elem[1] < pos_obj2[1]+25:
                return True
    #eraldi kontroll -OK, lisaks elemendi ümbrisnelinurga tippudele kontrollib ka külgede keskpunkte

# tavaline pildi sisselugemine
pac_east_img = PhotoImage(file="media/pac_e.png")
pac_west_img = PhotoImage(file="media/pac_w.png")
pac_north_img = PhotoImage(file="media/pac_n.png")
pac_south_img = PhotoImage(file="media/pac_s.png")
wall_img = PhotoImage(file="media/wall.png")
ghost_img = PhotoImage(file="media/ghost.png")

# pildi loomisel jätan meelde pildi id
pac_id = tahvel.create_image(alg_pos[0], alg_pos[1], image=pac_east_img)
ghost_id = tahvel.create_image(ghost_pos[0], ghost_pos[1], image=ghost_img)

wall_id =[]
for i in range(len(wall_pos)):
    wall_id.append(tahvel.create_image(wall_pos[i][0], wall_pos[i][1], image=wall_img))

# seon nooleklahvid vastavate funktsioonidega
raam.bind_all("<Up>",    nool_üles)
raam.bind_all("<Down>",  nool_alla)
raam.bind_all("<Left>",  nool_vasakule)
raam.bind_all("<Right>", nool_paremale)

liigu = ['üles','alla','vasakule','paremale']

def liikumine(indeks):
    if liigu[indeks] == 'üles':
        return [0,-sammu_pikkus]
    elif liigu[indeks] == 'alla':
        return [0,+sammu_pikkus]
    elif liigu[indeks] == 'vasakule':
        return [-sammu_pikkus,0]
    elif liigu[indeks] == 'paremale':
        return [+sammu_pikkus,0]

def uuenda():
    global ghost_pos
    global pac_pos
    global alg_pos
    global pac_id
    #print(ghost_pos)
    indeks = random.randint(0,3)
    kuhu = liikumine(indeks)
    if wall2(samm(ghost_pos)[indeks]) != True:
        ghost_pos[0] += kuhu[0]
        ghost_pos[1] += kuhu[1]
        tahvel.move(ghost_id,kuhu[0],kuhu[1])
    if collision(ghost_pos, pac_pos):
        tahvel.delete(pac_id)
        pac_id = tahvel.create_image(alg_pos[0], alg_pos[1], image=pac_east_img)
        pac_pos = [alg_pos[0], alg_pos[1]]

    # ootame 0,02 sekundit ja siis uuendame positsiooni
    raam.after(20, uuenda)

uuenda()




# ilmutame akna ekraanile
raam.mainloop()
