from tkinter.filedialog import *

from pygame import *

index = 0
v_size = 0.30

def player():
    top = Tk()
    top.title('멜로플레이어')
    top.geometry('384x360')

    ls_music = []
    lb_string = StringVar()

    def first_start():
        global index
        dir = os.getcwd() + '\\songs'

        if re.search(r'songs\b', os.getcwd()):
            dir = os.getcwd()
        else:
            os.chdir(dir)

            for files in os.listdir(dir):
                ls_music.append(files)

        mixer.init()
        mixer.music.load(ls_music[index])
        mixer.music.play()
        lb_string.set(ls_music[index])
        song_lb = Label(textvariable=lb_string)
        song_lb.pack()

    def music_list():
        global index

        def list_select(event):
            lb_string.set('')
            index = int(lb.curselection()[0])
            mixer.music.load(ls_music[index])
            mixer.music.play()
            lb_string.set(ls_music[index])

        def list_insert():
            i = 0

            for song in ls_music:
                lb.insert(i, song)
                i += 1

        win = Toplevel(top)
        win.title('목록')
        sb = Scrollbar(win)
        sb.pack(side=RIGHT, fill=Y)
        lb = Listbox(win, width=50, yscrollcommand=sb.set)
        lb.pack(side=LEFT)
        sb.config(command=lb.yview)
        list_insert()

        lb.bind('<<ListboxSelect>>', list_select)

    def play_song(event):
        mixer.music.play(-1)
        lb_update()

    def stop_song(event):
        mixer.music.stop()

    def lb_update():
        global index
        lb_string.set(ls_music[index])

    def previous_song(event):
        global index
        if index == 0:
            return
        index -= 1
        mixer.music.load(ls_music[index])
        mixer.music.play(-1)
        lb_update()

    def next_song(event):
        global index
        if index == len(ls_music[index]) - 1:
            return
        index += 1
        mixer.music.load(ls_music[index])
        mixer.music.play(-1)
        lb_update()

    def volume_down(event):
        global v_size
        mixer.music.set_volume(v_size)
        v_size -= 0.10

    def volume_up(event):
        global v_size
        mixer.music.set_volume(v_size)
        v_size += 0.10

    wall = PhotoImage(file='img/md_w.gif')
    w_lb = Label(image=wall)
    w_lb.place(x=0, y=0)

    img_p = PhotoImage(file='img/md_p.gif')
    b_p = Button(top, height=30, width=30, image=img_p)
    b_p.place(x=155, y=166)

    img_s = PhotoImage(file='img/md_s.gif')
    b_s = Button(top, height=30, width=30, image=img_s)
    b_s.place(x=195, y=166)

    img_b = PhotoImage(file='img/md_b.gif')
    b_b = Button(top, height=30, width=40, image=img_b)
    b_b.place(x=50, y=166)

    img_n = PhotoImage(file='img/md_n.gif')
    b_n = Button(top, height=30, width=40, image=img_n)
    b_n.place(x=290, y=166)

    img_u = PhotoImage(file='img/md_u.gif')
    b_u = Button(top, height=30, width=30, image=img_u)
    b_u.place(x=176, y=48)

    img_d = PhotoImage(file='img/md_d.gif')
    b_d = Button(top, height=30, width=30, image=img_d)
    b_d.place(x=176, y=288)

    img_l = PhotoImage(file='img/md_l.gif')
    b_l = Button(top, height=47, width=30, image=img_l, command=music_list)
    b_l.place(x=326, y=24)

    b_p.bind('<Button-1>', play_song)
    b_s.bind('<Button-1>', stop_song)
    b_b.bind('<Button-1>', previous_song)
    b_n.bind('<Button-1>', next_song)
    b_u.bind('<Button-1>', volume_up)
    b_d.bind('<Button-1>', volume_down)

    first_start()
    music_list()
    top.mainloop()
