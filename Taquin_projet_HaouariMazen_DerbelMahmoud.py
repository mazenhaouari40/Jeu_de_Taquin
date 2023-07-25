from tkinter import *
import tkinter as tk
import copy
from tkinter.ttk import *

#***** Etat finale **************:
final=[[1,2,3],[8,0,4],[7,6,5]]     # 1 3
#final=[[1,2,3],[6,4,5],[0,7,8]]     #2
#********************************

#***** Etat Initiale *********** :
initiale=  [[1,2,3],[8,6,0],[7,5,4]]      #1
#initiale= [[2,8,3],[1,6,4],[7,0,5]];     #3
#initiale= [[1,2,3],[4,0,5],[6,7,8]];     #2
#*******************************

#*******************************************************************
def numero(t,x,y):
    return t[x][y];

def afficher_taquin(t):
    print(t);
    
def etat_depart():
    global initiale;
    
    return initiale;     

def estEtatFinal(t):
    global finale;
    test=True;
    for i in range(3):
        for j in range(3):
            if (final[i][j]!=t[i][j]):
                return False;
    return True;

def position_case_vide(t):
    for i in range(3):
        for j in range(3):
            if (t[i][j]==0):
                return i,j;           

def permuter(t,x1,y1,x2,y2):
    t[x1][y1],t[x2][y2]=t[x2][y2],t[x1][y1];

def transition(m):
    adjacence=[];
    i,j=position_case_vide(m);
    #down
    if i!=0:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i-1,j)
        adjacence.append(temp)
    #up
    if i!=2:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i+1,j)
        adjacence.append(temp)
    #left
    if j!=0:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i,j-1)
        adjacence.append(temp)
    #right
    if j!=2:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i,j+1)
        adjacence.append(temp)
    return adjacence;

def transition2(m,niveau):
    adjacence=[];
    i,j=position_case_vide(m);
    #down
    if i!=0:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i-1,j)
        temp=[temp,niveau+1]
        adjacence.append(temp)
    #up
    if i!=2:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i+1,j)
        temp=[temp,niveau+1]
        adjacence.append(temp)
    #left
    if j!=0:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i,j-1)
        temp=[temp,niveau+1]
        adjacence.append(temp)
    #right
    if j!=2:
        temp=copy.deepcopy(m)
        permuter(temp,i,j,i,j+1)
        temp=[temp,niveau+1]
        adjacence.append(temp)
    return adjacence;


def h(chemin):
    #nombre de jetons mal places :
    global final;
    nb=0;
    for i in range(3):
        for j in range(3):
            if (chemin[i][j]!=final[i][j]) and (chemin[i][j]!=0):
                nb=nb+1;
    return nb;

def f(chemin,level):
    #avec niveau
    return h(chemin)+level;
    #sans niveau
    #return h(chemin)+1;
def meilleur_noeud(OPEN):
    temp=OPEN[0];
    pos=0;
    for i in range(1,len(OPEN)):
        if f(OPEN[i][0],OPEN[i][1])<f(temp[0],temp[1]):
            temp=copy.deepcopy(OPEN[i])
            pos=i;
    return pos;
#*****************************************************************

#*********Les Algorithmes***********

#****************Recherche en largeur d'abord********************
def largeur():
    delete()
    t=etat_depart();
    global final;
    CLOSED= []
    OPEN = [t]
    nb=1;
    print("ordre : down up left right")
    print('etat initiale-->',t);
    print("etat finale-->",final)
    while OPEN:
        noeud = OPEN.pop(0)
        CLOSED.append(noeud)
        print(noeud);
        if estEtatFinal(noeud):
            print("fin");
            print("nombre de noeud clos",nb);
            print("nombre de noeud explore",len(CLOSED))
            #affichage
            disp_tf1.configure(state='normal')
            disp_tf.configure(state='normal')
            disp_tf.insert(0,f'nombre de noeud clos{nb} .')
            disp_tf1.insert(0,f'nombre de noeud explore {len(CLOSED)} .')
            disp_tf.configure(state='disabled')
            disp_tf1.configure(state='disabled')
            #**************
            return CLOSED;
        noeudpossible = transition(noeud)
        for chemin in noeudpossible:
            if chemin not in CLOSED:
                OPEN.append(chemin)
                nb=nb+1;
                
#*************************************************************
               
#****************    Recherche en profondeur d'abord   *******
def profondeur():
    t=etat_depart();
    global final;
    CLOSED= []
    OPEN = [t]
    nb=1;
    print("ordre : down up left right")
    print('etat initiale-->',t);
    print("etat finale-->",final)
    while OPEN:
        noeud = OPEN.pop(0)
        CLOSED.append(noeud)
        print(noeud);
        if estEtatFinal(noeud):
            print("fin");
            print("nombre de noeud clos",nb);
            print("nombre de noeud explore",len(CLOSED))
            disp_tf1.configure(state='normal')
            disp_tf.configure(state='normal')
            disp_tf.insert(0,f'nombre de noeud clos{nb} .')
            disp_tf1.insert(0,f'nombre de noeud explore {len(CLOSED)} .')
            disp_tf.configure(state='disabled')
            disp_tf1.configure(state='disabled')
            return CLOSED;
        noeudpossible = transition(noeud)
        for chemin in noeudpossible:
            if chemin not in CLOSED:
                nb=nb+1
                OPEN.insert(0,chemin)
#*************************************************************
    
#***************     Recherche en profondeur limitée  ******
def profondeur_limitee(lim):
    t=etat_depart();
    global final;
    t2=[t,0]
    CLOSED= []
    OPEN = [t2]
    nb=1;
    print("ordre : down up left right")
    print('etat initiale -->',t);
    print("etat finale-->",final)
    while OPEN:
        noeud = OPEN.pop(0)
        CLOSED.append(noeud[0])
        print(noeud[0],noeud[1]);
        if estEtatFinal(noeud[0]):
            print("fin");
            print("nombre de noeud clos",nb);
            print("nombre de noeud explore",len(CLOSED))
            disp_tf1.configure(state='normal')
            disp_tf.configure(state='normal')
            disp_tf.insert(0,f'nombre de noeud clos{nb} .')
            disp_tf1.insert(0,f'nombre de noeud explore {len(CLOSED)} .')
            disp_tf.configure(state='disabled')
            disp_tf1.configure(state='disabled')
            return CLOSED;
        if noeud[1]<lim:
            noeudpossible = transition2(noeud[0],noeud[1])
            for i in range(len(noeudpossible)):
                if noeudpossible[i][0] not in CLOSED:
                    OPEN.insert(0,noeudpossible[i])
                    nb=nb+1
    if not OPEN:
        print("nombre de noeud clos",nb);
        print("nombre de noeud explore",len(CLOSED))
        print("solution introuvable")
        disp_tf1.configure(state='normal')
        disp_tf.configure(state='normal')
        disp_tf.insert(0,f'nombre de noeud explore {len(CLOSED)} .')
        disp_tf1.insert(0,f'Solution introuvable .')
        disp_tf.configure(state='disabled')
        disp_tf1.configure(state='disabled')
        return CLOSED;
#************************************************************

#****************   Solution A*     *************************
def solution_A_etoile():
    t=etat_depart();
    global final;
    t2=[t,0]
    CLOSED= []
    OPEN = [t2]
    nb=1;
    print("ordre : down up left right")
    print('etat initiale -->',t);
    print("etat finale-->",final)
    while OPEN:
        pos=meilleur_noeud(OPEN);
        noeud = OPEN.pop(pos)
        CLOSED.append(noeud[0])
        print(noeud[0],noeud[1]);
        if estEtatFinal(noeud[0]):
            print("fin");
            print("nombre de noeud clos",nb);
            print("nombre de noeud explore",len(CLOSED))
            disp_tf1.configure(state='normal')
            disp_tf.configure(state='normal')
            disp_tf.insert(0,f'nombre de noeud clos{nb} .')
            disp_tf1.insert(0,f'nombre de noeud explore {len(CLOSED)} .')
            disp_tf.configure(state='disabled')
            disp_tf1.configure(state='disabled')
            return CLOSED;
        noeudpossible = transition2(noeud[0],noeud[1])
        for i in range(len(noeudpossible)):
            if noeudpossible[i][0] not in CLOSED:
                OPEN.append(noeudpossible[i])
                nb=nb+1;
#***************************************************************
                
#***************************************************************
#Graphique:
window = Tk()
window.configure(width=900, height=700)
window.configure(bg='#ee6c4d')
window.title('Taquin Game')
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))
window.minsize(1000,800)
window.maxsize(1000,900)

def affiche1(res):
    mat=res.pop(0)
    for i in range(3):
         for j in range(3):
            x, y=180*j, 180*i
            A, B, C=(x, y), (x+180, y+180), (x+90, y+90)
            if mat[i][j]!=0:
                rect = can.create_rectangle(A, B, fill="Navyblue")
                txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)
            else:
                rect = can.create_rectangle(A, B, fill="white")
                txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)
    if(res):
        window.after(250,affiche1,res)
        
def affiche2(mat):    
    for i in range(3):
         for j in range(3):
            x, y=180*j, 180*i
            A, B, C=(x, y), (x+180, y+180), (x+90, y+90)
            if mat[i][j]!=0:
                rect = can.create_rectangle(A, B, fill="Navyblue")
                txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)
            else:
                rect = can.create_rectangle(A, B, fill="white")
                txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)              

def getdata():
    lim= entry1.get()
    return(lim)

def afflar():
    disp_tf1.configure(state='normal')
    disp_tf.configure(state='normal')
    delete()
    disp_tf.configure(state='disabled')
    disp_tf1.configure(state='disabled')
    mat=largeur()
    affiche1(mat)

def affpro():
    disp_tf1.configure(state='normal')
    disp_tf.configure(state='normal')
    delete()
    disp_tf.configure(state='disabled')
    disp_tf1.configure(state='disabled')
    mat=profondeur()
    affiche1(mat)

def affprolim():
    if (getdata()):
        disp_tf1.configure(state='normal')
        disp_tf.configure(state='normal')
        delete()
        disp_tf.configure(state='disabled')
        disp_tf1.configure(state='disabled')
        mat=profondeur_limitee(int(getdata()))
        affiche1(mat)
    else:
        print("aucun limite saisie")

def affaet():
    disp_tf1.configure(state='normal')
    disp_tf.configure(state='normal')
    delete()
    disp_tf.configure(state='disabled')
    disp_tf1.configure(state='disabled')
    mat=solution_A_etoile()
    affiche1(mat)
    
def refresh():
    disp_tf1.configure(state='normal')
    disp_tf.configure(state='normal')
    delete()
    disp_tf.configure(state='disabled')
    disp_tf1.configure(state='disabled')
    affiche2(etat_depart())

def delete():
    disp_tf1.delete("0","end")
    disp_tf.delete("0","end")

style = Style() 
style.configure('TButton', font =('calibri', 20, 'bold'),borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],background = [('active', 'black')])

style1 = Style()
style.configure('W.TButton', font = ('calibri', 20, 'bold',),foreground = 'Navyblue')


largeur1=Button(window, text="Largeur",style = 'W.TButton',width=15,command=afflar)
largeur1.pack()
largeur1.place(x=700,y=100)
profondeur1 =  Button(window, text="Profondeur ",style = 'W.TButton',width=15,command=affpro)
profondeur1.pack()
profondeur1.place(x=700,y=150)
profondeur_limite1 =  Button(window, text="Profondeur_limite",style = 'W.TButton',width=15,command=affprolim)
profondeur_limite1.pack()
profondeur_limite1.place(x=700,y=200)
solution_A1=  Button(window, text="Solution A * ",style = 'W.TButton',width=15,command=affaet)
solution_A1.pack()
solution_A1.place(x=700,y=250)
limite1 =  Button(window, text="Limite",style = 'W.TButton',width=15,command=getdata )
limite1.pack()
limite1.place(x=700,y=500)
refresh1 =  Button(window, text="Refresh ",style = 'W.TButton',width=15,command=refresh)
refresh1.pack()
refresh1.place(x=700,y=600)
entry1 = tk.Entry(fg="yellow", bg="gray",font=('calibri',20, 'bold'),width=7,justify='center')
entry1.pack()
entry1.place(x=760,y=450)
disp_tf = tk.Entry(fg="yellow", bg="gray",font=('calibri',20, 'bold'),width=30,justify='center',state='disabled')
disp_tf.pack(pady=5)
disp_tf.place(x=80,y=10)
disp_tf1 = tk.Entry(fg="yellow", bg="gray",font=('calibri',20, 'bold'),width=30,justify='center',state='disabled')
disp_tf1.pack(pady=5)
disp_tf1.place(x=80,y=50)

#Creation de canva :
can=Canvas( width=540,height=540,bg='white')
can.pack( side =LEFT, padx =20, pady =20)
can.pack(expand=NO)
FONT=('Ubuntu', 35, 'bold')

mat=etat_depart()
for i in range(3):
    for j in range(3):
        x, y=180*j, 180*i
        A, B, C=(x, y), (x+180, y+180), (x+90, y+90)
        if mat[i][j]!=0:
            rect = can.create_rectangle(A, B, fill="Navyblue")
            txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)
        else:
            rect = can.create_rectangle(A, B, fill="white")
            txt = can.create_text(C, text=mat[i][j], fill="white",font=FONT)
window.mainloop()
#***************************************************************
