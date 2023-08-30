import tkinter as tk
import random as rd

row = 12       
col = 9    
map_data = []
select_chip = 0
candy=0
stage=1
timer=0
key=""
index=0

char_data = []
char_list=[]



class mob:
    name=""
    xy=[]
    img=""
    img_num=0
    direction=0

    def __init__(self,name,img,img_num):
        self.name=name
        self.img=img
        self.img_num=img_num
        print(name,"생성")

    def move(self):
        x=0
        y=0

        if self.name!="blue":
            self.direction=rd.randint(1,4)

            
        #하1, 상2, 좌3, 우4
        if self.direction==1:
            y=1
            self.img_num=3
        elif self.direction==2:
            y=-1
            self.img_num=0
        elif self.direction==3:
            x=-1
            self.img_num=6
        elif self.direction==4:
            x=1
            self.img_num=9
        x+=self.xy[0]
        y+=self.xy[1]

        if 0<=x<row and 0<=y<col:
            if map_data[y][x]>=2:
                self.xy[1]=y
                self.xy[0]=x

                
        self.direction=0


def move_char():
    global candy, stage
    
    for i in char_list:
        i.move()

    x=char_list[0].xy[0]
    y=char_list[0].xy[1]
    
    if map_data[y][x]==3:
        map_data[y][x]=2
        candy-=1
        if candy==0:
            stage+=1
            set_map()
    
    for i in char_list:
        if i.name!="blue" and candy==0:
            if i.xy[0]==x and i.xy[1]==y:
                stage+=1
                set_map()
    root.after(1000,move_char)
    
def init_char():
    temp=mob("blue",img_pen,3)
    char_list.append(temp)
    
    temp=mob("red",img_red,3)
    char_list.append(temp)
    
    temp=mob("kuma",img_kuma,0)
    char_list.append(temp)
    
    temp=mob("seiuchi",img_seiuchi,0)
    char_list.append(temp)

    

def set_map():
    global stage, map_data, candy, index

    if stage==1:
        map_data = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 2, 2, 2, 3, 2, 2, 2, 2, 0, 0, ],
        [0, 0, 2, 2, 2, 3, 3, 2, 2, 2, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 0, 0, ],
        [0, 2, 2, 2, 2, 2, 3, 0, 2, 2, 0, 0, ],
        [0, 2, 2, 2, 2, 2, 2, 0, 3, 2, 0, 0, ],
        [2, 0, 0, 0, 0, 0, 2, 2, 3, 2, 0, 0, ],
        [2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, ],
        [2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, ]
        ]
        candy =7
        char_list[0].xy = [9, 6]
        char_list[1].xy = [3, 1]
        char_list[2].xy = [9, 1]
        char_list[3].xy = [2, 5]    

    if stage==2:
        map_data = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, ],
        [0, 3, 2, 3, 3, 3, 2, 2, 2, 2, 3, 0, ],
        [0, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 0, ],
        [0, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 0, ],
        [0, 3, 2, 2, 2, 3, 2, 2, 2, 2, 3, 0, ],
        [0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, ],
        [0, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 0, ],
        [1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, ]
        ]
        candy =38
        char_list[0].xy = [9, 2]
        char_list[1].xy = [2, 2]
        char_list[2].xy = [7, 5]
        char_list[3].xy = [3, 5]

    if stage==3:
        map_data = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
                                    ]
        candy =0
        char_list[0].xy = [13,13]
        char_list[1].xy = [13,13]
        char_list[2].xy = [13,13]
        char_list[3].xy = [13,13]
        index+=1
        
    move_char()
        
def draw_map():
    global row,col,map_data,timer,index
    fnt=("맑은 고딕 Semilight",20,"bold")

    for y in range(0,col):
        for x in range(0,row):
                canvas.create_image(x*60+30,y*60+30,image=img_chip[map_data[y][x]],tag = "BG")
    if index ==0:
        canvas.create_image(350,250,image=img_title,tag="BG")
        
    elif index==1:
        canvas.create_text(100,20,text="Candy:"+str(candy),font=fnt,fill="darkred",tag="BG")
        canvas.create_text(500,20,text="Time:"+str(timer),font=fnt,fill="darkred",tag="BG")
    elif index==2:
        canvas.delete("BG")
        canvas.create_image(350,250,image=img_end,tag="end")
        
    
    for i in char_list:
            canvas.create_image(i.xy[0]*60+30,i.xy[1]*60+30,image=i.img[i.img_num+timer%3],tag="BG")
        
    timer=(timer+1)
    root.after(1000,draw_map)
        
def key_down(e):
    global index
    key=e.keysym


    if key=="s":
        char_list[0].direction=1
    elif key=="w":
        char_list[0].direction=2
    elif key=="a":
        char_list[0].direction=3
    elif key=="d":
        char_list[0].direction=4
    elif key=="space" and index==0:
        index=1
    



    
def main():
    init_char()
    set_map()
    draw_map()



root=tk.Tk()
root.title("펭귄게임")
root.geometry("720x540")
root.resizable(False,False)
root.bind("<KeyPress>",key_down)


canvas=tk.Canvas(width=720,height=540,bg="white")
canvas.pack()

img_pen=[
                    tk.PhotoImage(file="pen00.png"),
                    tk.PhotoImage(file="pen01.png"),
                    tk.PhotoImage(file="pen02.png"),
                    tk.PhotoImage(file="pen03.png"),
                    tk.PhotoImage(file="pen04.png"),
                    tk.PhotoImage(file="pen05.png"),
                    tk.PhotoImage(file="pen06.png"),
                    tk.PhotoImage(file="pen07.png"),
                    tk.PhotoImage(file="pen08.png"),
                    tk.PhotoImage(file="pen09.png"),
                    tk.PhotoImage(file="pen10.png"),
                    tk.PhotoImage(file="pen11.png")
                     ]
                    
img_red=[
                    tk.PhotoImage(file="red00.png"),
                    tk.PhotoImage(file="red01.png"),
                    tk.PhotoImage(file="red02.png"),
                    tk.PhotoImage(file="red03.png"),
                    tk.PhotoImage(file="red04.png"),
                    tk.PhotoImage(file="red05.png"),
                    tk.PhotoImage(file="red06.png"),
                    tk.PhotoImage(file="red07.png"),
                    tk.PhotoImage(file="red08.png"),
                    tk.PhotoImage(file="red09.png"),
                    tk.PhotoImage(file="red10.png"),
                    tk.PhotoImage(file="red11.png")
                        ]
img_kuma=[
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="kuma01.png"),
                    tk.PhotoImage(file="kuma02.png"),
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="kuma01.png"),
                    tk.PhotoImage(file="kuma02.png"),
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="kuma01.png"),
                    tk.PhotoImage(file="kuma02.png"),
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="kuma01.png"),
                    tk.PhotoImage(file="kuma02.png")
                    
                    ]

img_seiuchi=[
                    tk.PhotoImage(file="seiuchi00.png"),
                    tk.PhotoImage(file="seiuchi01.png"),
                    tk.PhotoImage(file="seiuchi02.png"),
                    tk.PhotoImage(file="seiuchi00.png"),
                    tk.PhotoImage(file="seiuchi01.png"),
                    tk.PhotoImage(file="seiuchi02.png"),
                    tk.PhotoImage(file="seiuchi00.png"),
                    tk.PhotoImage(file="seiuchi01.png"),
                    tk.PhotoImage(file="seiuchi02.png"),
                    tk.PhotoImage(file="seiuchi00.png"),
                    tk.PhotoImage(file="seiuchi01.png"),
                    tk.PhotoImage(file="seiuchi02.png")
                    ]

img_title=tk.PhotoImage(file="title.png")

img_end=tk.PhotoImage(file="ending.png")

img_chip=[
                tk.PhotoImage(file="chip00.png"),
                tk.PhotoImage(file="chip01.png"),
                tk.PhotoImage(file="chip02.png"),
                tk.PhotoImage(file="chip03.png")
                    ]
main()
root.mainloop()
