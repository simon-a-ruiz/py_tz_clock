from tkinter import *
from datetime import datetime
import time
import pytz
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)

global label_t
global label_d
global label_desc
global frame
global tz

label_t = {}
label_d = {}
label_desc = {}
frame = {}
tz = {}


def Draw():
    c_row = 0
    for region in cfg['TimeZones']:
        for city in cfg['TimeZones'][region]:
            o_city = cfg['TimeZones'][region][city]
            c_row+=1
            frame[city] = {}
            label_desc[city] = {}

            for i in range(0, 3):
                frame[city][i] = Frame(root,
                    width=cfg['defaults']['frame']['width'],
                    height=cfg['defaults']['frame']['height'],
                    background=cfg['defaults']['colors']['background'])

                frame[city][i].grid(
                    row=c_row-1,
                    column=i,
                    sticky = W)

            label_desc[city] = Label(
                frame[city][0],
                text=o_city["description"],
                background=cfg['defaults']['colors']['background'],
                fg=o_city['colors']['description'],
                font=(
                    cfg['defaults']['label']['font']['face'],
                    cfg['defaults']['label']['font']['size'],
                    cfg['defaults']['label']['font']['weight']),
                padx=cfg['defaults']['label']['padding']['x'],
                pady=cfg['defaults']['label']['padding']['y'],
                justify=cfg['defaults']['label']['justify'])

            label_t[city] = Label(
                frame[city][1],
                text=o_city["description"],
                background=cfg['defaults']['colors']['background'],
                fg=o_city['colors']['time'],
                font=(
                    cfg['defaults']['label']['font']['face'],
                    cfg['defaults']['label']['font']['size'],
                    cfg['defaults']['label']['font']['weight']),
                padx=cfg['defaults']['label']['padding']['x'],
                pady=cfg['defaults']['label']['padding']['y'],
                justify=cfg['defaults']['label']['justify'])

            label_d[city] = Label(
                frame[city][2],
                text=o_city["description"],
                background=cfg['defaults']['colors']['background'],
                fg=o_city['colors']['date'],
                font=(
                    cfg['defaults']['label']['font']['face'],
                    cfg['defaults']['label']['font']['size'],
                    cfg['defaults']['label']['font']['weight']),
                padx=cfg['defaults']['label']['padding']['x'],
                pady=cfg['defaults']['label']['padding']['y'],
                justify=cfg['defaults']['label']['justify'])

            label_desc[city].pack()
            label_t[city].pack()
            label_d[city].pack()

def Refresher():
    for region in cfg['TimeZones']:
        for city in cfg['TimeZones'][region]:
            o_city = cfg['TimeZones'][region][city]
            tz[city] = pytz.timezone(o_city['tz'])

            label_t[city].configure(
                text=datetime.now(
                    tz[city]
                ).strftime(
                    cfg['defaults']['format']['time']
                ),
                fg=o_city['colors']['time'])

            label_d[city].configure(
                text=datetime.now(
                    tz[city]
                ).strftime(
                    cfg['defaults']['format']['date']
                ),
                fg=o_city['colors']['date'])
    root.after(1000, Refresher)

root = Tk()
#root.wm_attributes('-alpha',0.6)
root.wm_minsize(
    width=cfg['defaults']['window']['width'],
    height=cfg['defaults']['window']['height'])

root.title(
    string=cfg['appName'])

root.configure(
    background=cfg['defaults']['colors']['background'])

Draw()
Refresher()
root.mainloop()
