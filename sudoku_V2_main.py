from tkinter import *
from tkinter import ttk
import random as ran
from tkinter import messagebox 
import time


win = Tk()
win.title("SUDOKU")
win.geometry("275x390")
win.configure(bg="#dbd2d2")
mis=0



#Creating labels


label_2 = Label(win, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=0)
label_2 = Label(win, text="S",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=2)
label_3 = Label(win, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=3)
label_4 = Label(win, text="D",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=4)
label_5 = Label(win, text="O",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=5)
label_6 = Label(win, text="K",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=6)
label_7 = Label(win, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=7)
label_2 = Label(win, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=8)


#Creating Functions
def start_Q():
    root = Tk()
    root.configure(bg="#c8f1f4")
    root.title("SUDOKU")

    #Defining variables
    A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=0


    #Creating a Function that random distinct 5 digit list

    def rand():   
        lst=[]                                                          #Quick Play
        while True:
            temporary=ran.randint(1,5)                                     
            if temporary not in lst:
                lst.append(temporary)
                if len(lst)==5:
                    break
        return lst    


    #Creating Random Puzzle

    row="1"
    main=0
    while True:
    
        if row=="1":
            A,B,C,D,E=rand()
            row="2"
            loop_2=loop_3=loop_4=loop_5=0

        if row=="2":  
            F,G,H,I,J=rand()
        
            while True:
                loop_2+=1
            
                if F in [A,B,C] or G in [A,B,C] or H==C or I in [D,E] or J in [D,E]:
                    F,G,H,I,J=rand()
                    if loop_2==20:                                                          #Quick Play
                        row="1"
                        break
                else:
                    row="3"
                    break
    
        if row=="3":
            K,L,M,N,O=rand()
        
            while True:
                loop_3+=1
            
                if K in [A,F] or L in [B,G,H] or M in [C,H] or N in [I,D]  or O in [D,E,I,J] :
                    K,L,M,N,O=rand()
                    if loop_3==20:
                        row="2"
                        break
                    elif loop_3==40:
                        row="1"
                        break
                else:
                    row="4"
                    break                                  #Quick Play
    
        if row=="4":
            P,Q,R,S,T=rand()                                         
            while True:
                loop_4+=1
            
                if P in [A,F,K] or Q in [B,G,L,H] or R in [H,L,M,N] or S in [D,I,N] or T in [E,J,O]:
                    P,Q,R,S,T=rand()
                    if loop_4==20:
                        row="3"
                        break
                    elif loop_4==40:
                        row="2"
                        break
                    elif loop_4==60:
                        row="1"
                        break
                else:
                    row="5"
                    break
    

        if row=="5":
        
            U,V,W,X,Y=rand()
            while True:
                loop_5+=1
            
                if U in [A,F,K,P] or V in [B,G,L,Q] or W in [C,H,M,R,S,T] or X in [D,I,N,S,T] or Y in [E,J,O,T,S]:
                    U,V,W,X,Y=rand()
                    if loop_5==20:
                        row="4"
                        break
                    elif loop_5==40:
                        row="3"
                        break
                    elif loop_5==60:
                        row="2"
                        break
                    elif loop_5==80:
                        row="1"
                        break
                else:
                    if row=="5":
                        break
    
        if row=="5":
            break
    
                                                                                #Quick Play
         
    #Creating Entry Boxes
    
    b1 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b1.grid(row=1, column=1)

    b2 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b2.grid(row=1, column=2)

    b3 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b3.grid(row=1, column=3)

    b4 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b4.grid(row=1, column=4)

    b5 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b5.grid(row=1, column=5)

    b6 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b6.grid(row=2, column=1)

    b7 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b7.grid(row=2, column=2)

    b8 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b8.grid(row=2, column=3)

    b9 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b9.grid(row=2, column=4)

    b10 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b10.grid(row=2, column=5)

    b11 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b11.grid(row=3, column=1)

    b12 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b12.grid(row=3, column=2)

    b13 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b13.grid(row=3, column=3)

    b14 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b14.grid(row=3, column=4)

    b15 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b15.grid(row=3, column=5)

    b16 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))           #Quick Play
    b16.grid(row=4, column=1)

    b17 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b17.grid(row=4, column=2)

    b18 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b18.grid(row=4, column=3)

    b19 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b19.grid(row=4, column=4)

    b20 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b20.grid(row=4, column=5)

    b21 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b21.grid(row=5, column=1)

    b22 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b22.grid(row=5, column=2)

    b23 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b23.grid(row=5, column=3)

    b24 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b24.grid(row=5, column=4)

    b25 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b25.grid(row=5, column=5)

    randlst = [] ; i_diff = 10 ; t_diff = 1


    #Selecting random hints to be displayed

    while t_diff <= i_diff:
        if t_diff==1:
            tep=ran.randint(65,69)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        elif t_diff==2:
            tep=ran.randint(75,79)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        elif t_diff==3:
            tep=ran.randint(85,89)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        else:
            tep=ran.randint(65,89)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1        
    start=time.time()  #Starting Timmer

    bx = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]

    values = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y]

    value_var = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

    for prt in range(0,25):
        if value_var[prt] in randlst:
            bx[prt].insert(0," ")
            bx[prt].insert(1,values[prt])
        else:
            bx[prt].insert(0," ")


    #Defining command functions
    def  submit():
        global ct
        ct=0
        for rt in bx:
            tj=rt.get()
            if len(tj)==2:
                if tj[1].isdigit():
                    ct+=1
                    print(ct)
        
        if ct<=25:
            end = time.time()       #Stoping Timmer
            Timmer=int(end-start)
            messagebox.showinfo(" ",f'     CONGRATULATIONS YOU WON \n          Your Time is {Timmer} seconds')
            root.destroy()
        else:
            messagebox.showinfo(" ","COMPLETE THE GAME")
            

           
    def check():
        global mis
        global correct
        for lp in range(0,25):
            if bx[lp].get()==" ":
                continue

            else:    
                if value_var[lp] in randlst:
                    continue
                else:
                    vx = bx[lp].get()
                    vv=str(values[lp])                                        #Quick Play
                    if vx[1]!=vv:
                        mis+=1
                        if mis >= 3:
                            messagebox.showinfo("",'''    SORRY

       TRY AGAIN''')
                            root.destroy()
                        label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial",13)).grid(row=6, column=4, columnspan=3)
                        bx[lp].delete(1)
            
    #Defining Buttons

    submit_button = Button(root, text="Submit", padx=30, pady=10, bg="#b2aaa8", command=submit)

    check_button = Button(root, text="Check", padx=30, pady=10, bg="#b2aaa8", command=check)
      


    label=Label(root,text="                ",bg="#c8f1f4").grid(row=6, column=1)
    label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial ",13),bg="#c8f1f4").grid(row=6, column=4, columnspan=3)

    label=Label(root,text="‼ pUzZle YOuR BrAiN ‼", fg="#000000", font=("Arial Black",18),bg="#c8f1f4").grid(row=0, column=0, columnspan=8)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=1, column=0)
    label=Label(root,text=" ‼ ‽",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=2, column=0)
    label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=3, column=0)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=0)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=5, column=0)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=6, column=0)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=0)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=1, column=7)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=2, column=7)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=3, column=7)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=7)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=5, column=7)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=7)
    label=Label(root,text=" ‽ ‼",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=7)

    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=1, columnspan=1)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=6, column=2, columnspan=1)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=3, columnspan=1)

    label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=7, column=0, columnspan=1)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=7, column=3, columnspan=1)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=7, column=7, columnspan=1)


    #Locating Buttons

    submit_button.grid(row=7, column=1, columnspan=2)                        #Quick Play
    check_button.grid(row=7, column=4, columnspan=2)


    root.mainloop()

def qit():
    win.destroy()


# Instructions

def inf():
    win_3 = Tk()
    win_3.configure(bg="#dbd2d2")

    label = Label(win_3, text="INSTRUCTIONS",font=("Arial Black",16,'underline'), bg="#dbd2d2").pack()
    label = Label(win_3,text="  ",bg="#dbd2d2").pack()
    label = Label(win_3, text='''A Sudoku puzzle begins with a grid in which some of the numbers
     are already in place,depending on the game difficulty.''',font=("Arial",12), bg="#dbd2d2").pack() 
    label = Label(win_3, text='''A complete puzzle is one where each number from 1 to 5 appears
     only once in each of the 5 rows,5 column and 5 blocks.''',font=("Arial",12), bg="#dbd2d2").pack()
    label = Label(win_3, text='''Study the grid to find the numbers that might fit into each cell.''',font=("Arial",12), bg="#dbd2d2").pack()

    win_3.mainloop()
    




def start_G():
    
    root = Tk()
    root.configure(bg="#c8f1f4")
    root.title("SUDOKU")

    #Defining variables
    A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=0


    #Creating a Function that random distinct 5 digit list

    def rand():   
        lst=[]
        while True:
            temporary=ran.randint(1,5)
            if temporary not in lst:
                lst.append(temporary)
            if len(lst)==5:
                break
        return lst    


    #Creating Random Puzzle




    row="1"
    main=0
    while True:
        
        if row=="1":
            
            A,B,C,D,E=rand()
            row="2"
            loop_2=loop_3=loop_4=loop_5=0

        if row=="2":  
            F,G,H,I,J=rand()
            
            while True:
                loop_2+=1
                
                if F in [A,B,C] or G in [A,B,C] or H==C or I in [D,E] or J in [D,E]:
                    F,G,H,I,J=rand()
                    if loop_2==20:
                        row="1"
                        break
                else:
                    row="3"
                    break
        
        if row=="3":
            K,L,M,N,O=rand()
            
            while True:
                loop_3+=1
                
                if K in [A,F] or L in [B,G,H] or M in [C,H] or N in [I,D]  or O in [D,E,I,J] :
                    K,L,M,N,O=rand()
                    if loop_3==20:
                        row="2"
                        break
                    elif loop_3==40:
                        row="1"
                        break
                else:
                    row="4"
                    break
        
        if row=="4":
            P,Q,R,S,T=rand()
            
            while True:
                loop_4+=1
                
                if P in [A,F,K] or Q in [B,G,L,H] or R in [H,L,M,N] or S in [D,I,N] or T in [E,J,O]:
                    P,Q,R,S,T=rand()
                    if loop_4==20:
                        row="3"
                        break
                    elif loop_4==40:
                        row="2"
                        break
                    elif loop_4==60:
                        row="1"
                        break
                else:
                    row="5"
                    break
        

        if row=="5":
            
            U,V,W,X,Y=rand()
            while True:
                loop_5+=1
                
                if U in [A,F,K,P] or V in [B,G,L,Q] or W in [C,H,M,R,S,T] or X in [D,I,N,S,T] or Y in [E,J,O,T,S]:
                    U,V,W,X,Y=rand()
                    if loop_5==20:
                        row="4"
                        break
                    elif loop_5==40:
                        row="3"
                        break
                    elif loop_5==60:
                        row="2"
                        break
                    elif loop_5==80:
                        row="1"
                        break
                else:
                    if row=="5":
                        break
        
        if row=="5":
            break
        
        
            
    #Creating Entry Boxes

    b1 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b1.grid(row=1, column=1)

    b2 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b2.grid(row=1, column=2)

    b3 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b3.grid(row=1, column=3)

    b4 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b4.grid(row=1, column=4)

    b5 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b5.grid(row=1, column=5)

    b6 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b6.grid(row=2, column=1)

    b7 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
    b7.grid(row=2, column=2)

    b8 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b8.grid(row=2, column=3)

    b9 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b9.grid(row=2, column=4)

    b10 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b10.grid(row=2, column=5)

    b11 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b11.grid(row=3, column=1)

    b12 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b12.grid(row=3, column=2)

    b13 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b13.grid(row=3, column=3)

    b14 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b14.grid(row=3, column=4)

    b15 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
    b15.grid(row=3, column=5)

    b16 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b16.grid(row=4, column=1)

    b17 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b17.grid(row=4, column=2)

    b18 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
    b18.grid(row=4, column=3)

    b19 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b19.grid(row=4, column=4)

    b20 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b20.grid(row=4, column=5)

    b21 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b21.grid(row=5, column=1)

    b22 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
    b22.grid(row=5, column=2)

    b23 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b23.grid(row=5, column=3)

    b24 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b24.grid(row=5, column=4)

    b25 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
    b25.grid(row=5, column=5)

    randlst = [] ; i_diff = 10 ; t_diff = 1


    #Selecting random hints to be displayed

    while t_diff <= i_diff:
        if t_diff==1:
            tep=ran.randint(65,69)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        elif t_diff==2:
            tep=ran.randint(75,79)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        elif t_diff==3:
            tep=ran.randint(85,89)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1
                
        else:
            tep=ran.randint(65,89)
            if chr(tep) not in randlst:
                randlst.append(chr(tep))
                t_diff+=1        


    start = time.time()  #Starting Timmer

    bx = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]

    values = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y]

    value_var = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

    for prt in range(0,25):
        if value_var[prt] in randlst:
            bx[prt].insert(0," ")
            bx[prt].insert(1,values[prt])
        else:
            bx[prt].insert(0," ")


    mis=0

    #Defining command functions
    def  submit():
        global ct
        ct=0
        for rt in bx:
            tj=rt.get()
            if len(tj)==2:
                if tj[1].isdigit():
                    ct+=1
                    print(ct)
        
        if ct<=25:
            end = time.time()       #Stoping Timmer
            Timmer=int(end-start)
            messagebox.showinfo(" ",f'     CONGRATULATIONS YOU WON \n          Your Time is {Timmer} seconds')
            with open("history.txt",'a+') as fa:
                name = entry_box.get()
                fa.write(f'\n{name} {Timmer}')
            root.destroy()
        else:
            messagebox.showinfo(" ","COMPLETE THE GAME")
            

            
    def check():
        global mis
        global correct
        for lp in range(0,25):
            if bx[lp].get()==" ":
                continue

            else:    
                if value_var[lp] in randlst:
                    continue
                else:
                    vx = bx[lp].get()
                    vv=str(values[lp])
                    if vx[1]!=vv:
                        mis+=1
                        if mis >= 3:
                            messagebox.showinfo("",'''    SORRY

       TRY AGAIN''')
                            with open("history.txt",'a+') as fa:
                                name = entry_box.get()
                                fa.write(f'\n{name} {None}')
                            root.destroy()
                        label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial",13)).grid(row=6, column=4, columnspan=3)
                        bx[lp].delete(1)
            
    #Defining Buttons

    submit_button = Button(root, text="Submit", padx=30, pady=10, bg="#b2aaa8", command=submit)

    check_button = Button(root, text="Check", padx=30, pady=10, bg="#b2aaa8", command=check)
      


    label=Label(root,text="                ",bg="#c8f1f4").grid(row=6, column=1)
    label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial ",13),bg="#c8f1f4").grid(row=6, column=4, columnspan=3)

    label=Label(root,text="‼ pUzZle YOuR BrAiN ‼", fg="#000000", font=("Arial Black",18),bg="#c8f1f4").grid(row=0, column=0, columnspan=8)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=1, column=0)
    label=Label(root,text=" ‼ ‽",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=2, column=0)
    label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=3, column=0)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=0)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=5, column=0)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=6, column=0)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=0)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=1, column=7)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=2, column=7)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=3, column=7)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=7)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=5, column=7)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=7)
    label=Label(root,text=" ‽ ‼",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=7)

    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=1, columnspan=1)
    label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=6, column=2, columnspan=1)
    label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=3, columnspan=1)

    label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=7, column=0, columnspan=1)
    label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=7, column=3, columnspan=1)
    label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=7, column=7, columnspan=1)




    #Locating Buttons

    submit_button.grid(row=7, column=1, columnspan=2)
    check_button.grid(row=7, column=4, columnspan=2)


    root.mainloop()


        
# New Player

def new():
    user = Tk()
    user.geometry("290x250")
    user.configure(bg="#dbd2d2")          # NEW PLAYER MENU
                                         
    label_2 = Label(user, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=0)
    label_2 = Label(user, text="S",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=2)
    label_3 = Label(user, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=3)
    label_4 = Label(user, text="D",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=4)
    label_5 = Label(user, text="O",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=5)
    label_6 = Label(user, text="K",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=6)
    label_7 = Label(user, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=7)
    label_2 = Label(user, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=8)

    label_1 = Label(user,text="Enter Your Name : ",font=("Arial Black",12),bg="#dbd2d2")
    label_1.grid(row=3,column=1,columnspan=7)

    global entry_box
    entry_box = Entry(user,width=18,font=("Arial",15))
    entry_box.grid(row=4,column=1,columnspan=7)

    label_9 = Label(user, text="How Smart Are You ?",font=("Arial Black",12),bg="#dbd2d2")
    label_9.grid(row=6,column=1,columnspan=7)
       
    global dfc
    dfc = IntVar()
    rad1 = Radiobutton(user, text="Easy", bg="#dbd2d2", font=("Arial Black",9), value=0, variable=dfc)                          
    rad2 = Radiobutton(user, text="Medium", bg="#dbd2d2", font=("Arial Black",9), value=1, variable=dfc)                        
    rad3 = Radiobutton(user, text="Difficult", bg="#dbd2d2", font=("Arial Black",9), value=2, variable=dfc)

    rad1.grid(row=7,column=2,columnspan=2)
    rad2.grid(row=7,column=4,columnspan=2)
    rad3.grid(row=7,column=6,columnspan=2)

    label=Label(user,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=0, columnspan=1)
    label=Label(user,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=2, columnspan=2)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=4, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=6, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=8, columnspan=1)

    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=6, column=0, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=6, column=8, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=4, column=8, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=4, column=0, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=0, columnspan=1)
    label=Label(user,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=8, columnspan=1)

    label=Label(user,text="",bg="#dbd2d2").grid(row=5,column=1)

    def custom():
        user.destroy()
        start_G()

    start = Button(user,text="  Start Game  ",font=("Arial Black",9),bg="#dbd2d2",command=custom)
    start.grid(row=8,column=3,columnspan=4)
    
        
    user.mainloop()


def about():
    win_4 = Tk()
    win_4.configure(bg="#dbd2d2")

    label = Label(win_4, text="ABOUT",font=("Arial Black",16,'underline'), bg="#dbd2d2").pack()
    label = Label(win_4,text="  ",bg="#dbd2d2").pack()
    label = Label(win_4, text='''@author: Ͷα√ёẽň''',font=("Arial",12,'underline'), bg="#dbd2d2").pack() 
    label = Label(win_4, text='''Created on 11 July 2020''',font=("Arial",12,'underline'), bg="#dbd2d2").pack()
    label = Label(win_4, text='''Copyright © 2020 by The Black Hole Technologies ''',font=("Arial",12,'underline'), bg="#dbd2d2").pack()
    label = Label(win_4, text='''The Black Hole® is a registered trademark of the The Black Hole Corporation. Inc''',font=("Arial",12,'underline'), bg="#dbd2d2").pack()

    win_4.mainloop()

def select():
    win_5 = Tk()
    win_5.configure(bg="#dbd2d2")
    win_5.geometry("480x270")

    label_1 = Label(win_5, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=0)
    label_2 = Label(win_5, text="S",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=2)
    label_3 = Label(win_5, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=3)
    label_4 = Label(win_5, text="D",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=4)
    label_5 = Label(win_5, text="O",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=5)
    label_6 = Label(win_5, text="K",font=("Arial Black",27),fg="#9f9797",bg="#dbd2d2").grid(row=1, column=6)
    label_7 = Label(win_5, text="U",font=("Arial Black",27),fg="#6d6969",bg="#dbd2d2").grid(row=1, column=7)
    label_8 = Label(win_5, text="‼",font=("Arial Black",27),fg="#949292",bg="#dbd2d2").grid(row=1, column=8)

    label_8 = Label(win_5,text="    Select your name :", bg="#dbd2d2", font=("Arial Black",12))
    label_8.grid(row=2,column=1,columnspan=7)                                                                                    

    label_9 = Label(win_5,text="Note:Your Name will be listed only if you have played before!", bg="#dbd2d2", fg="red", font=("Arial Black",9))
    label_9.grid(row=4,column=1,columnspan=7)

    label = Label(win_5,text="",bg="#dbd2d2")
    label.grid(row=6,column=1,columnspan=3)


    #Defining Combobutton

    with open("history.txt","r") as his:
        LST=[]
        for line in his:
            H_name = line.split()
            if len(H_name)>0:
                LST.append(H_name[0])

    global USER
    USER = StringVar()
    combo_1 = ttk.Combobox(win_5, width=16, textvariable=USER, font=("Arial Black",12), state='readonly')
    combo_1['values'] = LST
    combo_1.grid(row=3,column=1,columnspan=8)
                     

    def back():
        win_5.destroy()

    def start_S():
        root = Tk()
        root.configure(bg="#c8f1f4")
        root.title("SUDOKU")
        
        with open("history.txt","r") as high:
            global highscore
            highscore=""
            for li in high:
                H_name = li.split()
                if len(H_name)>0:
                    if H_name=="USER":
                        highscore = (H_name[1])
                        print(highscore)

        messagebox.showinfo(" ",f'Hello {USER} \n  Your High Score is \n {highscore}')

        #Defining variables
        A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=0


        #Creating a Function that random distinct 5 digit list

        def rand():   
            lst=[]
            while True:
                temporary=ran.randint(1,5)
                if temporary not in lst:
                    lst.append(temporary)
                if len(lst)==5:
                    break
            return lst    


        #Creating Random Puzzle




        row="1"
        main=0
        while True:
            
            if row=="1":      
                A,B,C,D,E=rand()
                row="2"
                loop_2=loop_3=loop_4=loop_5=0

            if row=="2":  
                F,G,H,I,J=rand()
                
                while True:
                    loop_2+=1
                    
                    if F in [A,B,C] or G in [A,B,C] or H==C or I in [D,E] or J in [D,E]:
                        F,G,H,I,J=rand()
                        if loop_2==20:
                            row="1"
                            break
                    else:
                        row="3"
                        break
            
            if row=="3":
                K,L,M,N,O=rand()
                
                while True:
                    loop_3+=1
                    
                    if K in [A,F] or L in [B,G,H] or M in [C,H] or N in [I,D]  or O in [D,E,I,J] :
                        K,L,M,N,O=rand()
                        if loop_3==20:
                            row="2"
                            break
                        elif loop_3==40:
                            row="1"
                            break
                    else:
                        row="4"
                        break
            
            if row=="4":
                P,Q,R,S,T=rand()
                
                while True:
                    loop_4+=1
                    
                    if P in [A,F,K] or Q in [B,G,L,H] or R in [H,L,M,N] or S in [D,I,N] or T in [E,J,O]:
                        P,Q,R,S,T=rand()
                        if loop_4==20:
                            row="3"
                            break
                        elif loop_4==40:
                            row="2"
                            break
                        elif loop_4==60:
                            row="1"
                            break
                    else:
                        row="5"
                        break
            

            if row=="5":
                
                U,V,W,X,Y=rand()
                while True:
                    loop_5+=1
                    
                    if U in [A,F,K,P] or V in [B,G,L,Q] or W in [C,H,M,R,S,T] or X in [D,I,N,S,T] or Y in [E,J,O,T,S]:
                        U,V,W,X,Y=rand()
                        if loop_5==20:
                            row="4"
                            break
                        elif loop_5==40:
                            row="3"
                            break
                        elif loop_5==60:
                            row="2"
                            break
                        elif loop_5==80:
                            row="1"
                            break
                    else:
                        if row=="5":
                            break
            
            if row=="5":
                break
            
            
                
        #Creating Entry Boxes

        b1 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
        b1.grid(row=1, column=1)

        b2 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
        b2.grid(row=1, column=2)

        b3 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
        b3.grid(row=1, column=3)

        b4 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
        b4.grid(row=1, column=4)

        b5 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
        b5.grid(row=1, column=5)

        b6 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
        b6.grid(row=2, column=1)

        b7 = Entry(root, width=2, borderwidth=3,bg="#9cf8d0",font=("Arial",30))
        b7.grid(row=2, column=2)

        b8 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
        b8.grid(row=2, column=3)

        b9 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
        b9.grid(row=2, column=4)

        b10 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
        b10.grid(row=2, column=5)

        b11 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
        b11.grid(row=3, column=1)

        b12 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
        b12.grid(row=3, column=2)

        b13 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
        b13.grid(row=3, column=3)

        b14 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
        b14.grid(row=3, column=4)

        b15 = Entry(root, width=2, borderwidth=3,bg="#c0d6e4",font=("Arial",30))
        b15.grid(row=3, column=5)

        b16 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
        b16.grid(row=4, column=1)

        b17 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
        b17.grid(row=4, column=2)

        b18 = Entry(root, width=2, borderwidth=3,bg="#93e993",font=("Arial",30))
        b18.grid(row=4, column=3)

        b19 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
        b19.grid(row=4, column=4)

        b20 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
        b20.grid(row=4, column=5)

        b21 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
        b21.grid(row=5, column=1)

        b22 = Entry(root, width=2, borderwidth=3,bg="#fae9d5",font=("Arial",30))
        b22.grid(row=5, column=2)

        b23 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
        b23.grid(row=5, column=3)

        b24 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
        b24.grid(row=5, column=4)

        b25 = Entry(root, width=2, borderwidth=3,bg="#f6c5db",font=("Arial",30))
        b25.grid(row=5, column=5)

        randlst = [] ; i_diff = 10 ; t_diff = 1


        #Selecting random hints to be displayed

        while t_diff <= i_diff:
            if t_diff==1:
                tep=ran.randint(65,69)
                if chr(tep) not in randlst:
                    randlst.append(chr(tep))
                    t_diff+=1
                    
            elif t_diff==2:
                tep=ran.randint(75,79)
                if chr(tep) not in randlst:
                    randlst.append(chr(tep))
                    t_diff+=1
                    
            elif t_diff==3:
                tep=ran.randint(85,89)
                if chr(tep) not in randlst:
                    randlst.append(chr(tep))
                    t_diff+=1
                    
            else:
                tep=ran.randint(65,89)
                if chr(tep) not in randlst:
                    randlst.append(chr(tep))
                    t_diff+=1        


        bx = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]

        values = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y]

        value_var = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

        for prt in range(0,25):
            if value_var[prt] in randlst:
                bx[prt].insert(0," ")
                bx[prt].insert(1,values[prt])
            else:
                bx[prt].insert(0," ")


        mis=0

        #Defining command functions
        def  submit():
            global ct
            ct=0
            for rt in bx:
                tj=rt.get()
                if len(tj)==2:
                    if tj[1].isdigit():
                        ct+=1
                        print(ct)
            
            if ct<=25:
                end = time.time()       #Stoping Timmer
                Timmer=int(end-start)
                messagebox.showinfo(" ",f'     CONGRATULATIONS YOU WON \n          Your Time is {Timmer} seconds')
                root.destroy()
            else:
                messagebox.showinfo(" ","COMPLETE THE GAME")
                

                
        def check():
            global mis
            global correct
            for lp in range(0,25):
                if bx[lp].get()==" ":
                    continue

                else:    
                    if value_var[lp] in randlst:
                        continue
                    else:
                        vx = bx[lp].get()
                        vv=str(values[lp])
                        if vx[1]!=vv:
                            mis+=1
                            if mis >= 3:
                                messagebox.showinfo("",'''    SORRY

           TRY AGAIN''')
                                root.destroy()
                            label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial",13)).grid(row=6, column=4, columnspan=3)
                            bx[lp].delete(1)
                
        #Defining Buttons

        submit_button = Button(root, text="Submit", padx=30, pady=10, bg="#b2aaa8", command=submit)

        check_button = Button(root, text="Check", padx=30, pady=10, bg="#b2aaa8", command=check)
          


        label=Label(root,text="                ",bg="#c8f1f4").grid(row=6, column=1)
        label=Label(root,text=f'Mistakes={mis}/3', fg="red", font=("Arial ",13),bg="#c8f1f4").grid(row=6, column=4, columnspan=3)

        label=Label(root,text="‼ pUzZle YOuR BrAiN ‼", fg="#000000", font=("Arial Black",18),bg="#c8f1f4").grid(row=0, column=0, columnspan=8)
        label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=1, column=0)
        label=Label(root,text=" ‼ ‽",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=2, column=0)
        label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=3, column=0)
        label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=0)
        label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=5, column=0)
        label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=6, column=0)
        label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=0)
        label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=1, column=7)
        label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=2, column=7)
        label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=3, column=7)
        label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=4, column=7)
        label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=5, column=7)
        label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=7)
        label=Label(root,text=" ‽ ‼",font=("Arial Black",9), fg="#fae9d5",bg="#c8f1f4").grid(row=7, column=7)

        label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=1, columnspan=1)
        label=Label(root,text=" ? ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=6, column=2, columnspan=1)
        label=Label(root,text=" ¿ ‽",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=6, column=3, columnspan=1)

        label=Label(root,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#c8f1f4").grid(row=7, column=0, columnspan=1)
        label=Label(root,text=" ‽ ¿",font=("Arial Black",9), fg="#4aec19",bg="#c8f1f4").grid(row=7, column=3, columnspan=1)
        label=Label(root,text=" ‼ ¿",font=("Arial Black",9), fg="#f23c1b",bg="#c8f1f4").grid(row=7, column=7, columnspan=1)


        #Locating Buttons

        submit_button.grid(row=7, column=1, columnspan=2)
        check_button.grid(row=7, column=4, columnspan=2)



        root.mainloop()

    def play():
        win_5.destroy()
        start_G()

    #Defining Buttons

    button_1 = Button(win_5,text="Go Back", bg="#dbd2d2", font=("Arial Black",12),command=back)
    button_1.grid(row=7,column=1,columnspan=4)

    button_2 = Button(win_5,text="Start Game", bg="#dbd2d2", font=("Arial Black",12),command=play)
    button_2.grid(row=7,column=5,columnspan=4)

    #Radio Buttons

    dfc1 = IntVar()
    rad11 = Radiobutton(win_5, text="Easy", bg="#dbd2d2", font=("Arial Black",9), value=8, variable=dfc1)
    rad22 = Radiobutton(win_5, text="Medium", bg="#dbd2d2", font=("Arial Black",9), value=6, variable=dfc1)
    rad33 = Radiobutton(win_5, text="Difficult", bg="#dbd2d2", font=("Arial Black",9), value=5, variable=dfc1)

    rad11.grid(row=5,column=2,columnspan=2)
    rad22.grid(row=5,column=4,columnspan=2)
    rad33.grid(row=5,column=6,columnspan=2)

    label=Label(win_5,text=" ¿ ‼",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=0, columnspan=1)
    label=Label(win_5,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=2, columnspan=1)
    label=Label(win_5,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=2, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=4, columnspan=1)
    label=Label(win_5,text="     ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=6, columnspan=1)
    label=Label(win_5,text=" ‼ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=6, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=2, column=8, columnspan=1)

    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=6, column=0, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=6, column=8, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=4, column=8, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=4, column=0, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=0, columnspan=1)
    label=Label(win_5,text=" ‽ ¿",font=("Arial Black",9), fg="#000000",bg="#dbd2d2").grid(row=8, column=8, columnspan=1)


    win_5.mainloop()

#Creating Buttons  "MAIN MENU"

button_1 = Button(win, text="  Quick Play  ",font=("Arial",12), padx=50, pady=10,bg="#c1c0c0",command=start_Q)
button_2 = Button(win, text="  New Player  ",font=("Arial",12), padx=48, pady=10,bg="#d8d2d2",command=new)
button_3 = Button(win, text=" Select Player ",font=("Arial",12), padx=45, pady=10,bg="#c1c0c0",command=select)
button_4 = Button(win, text=" Instructions ",font=("Arial",12), padx=52, pady=10,bg="#d8d2d2",command=inf)
button_5 = Button(win, text=" About Author ",font=("Arial",12), padx=45, pady=10,bg="#c1c0c0",command=about)
button_6 = Button(win, text="     Exit     ",font=("Arial",12), padx=61, pady=10,bg="#d8d2d2",command=qit)


#Displaying Buttons "MAIN MENU"

label=Label(win ,text=" ‼ ¿",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=3, column=0)
label=Label(win ,text=" ‼ ¿",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=3, column=8)
button_1.grid(row=3,column=1, columnspan=7)

label=Label(win ,text=" ¿ ‽",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=4, column=0)
label=Label(win ,text=" ¿ ‽",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=4, column=8)
button_2.grid(row=4,column=1, columnspan=7)

label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=5, column=0)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=5, column=8)
button_3.grid(row=5,column=1, columnspan=7)

label=Label(win ,text=" ‼ ¿",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=6, column=0)
label=Label(win ,text=" ‼ ¿",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=6, column=8)
button_4.grid(row=6,column=1, columnspan=7)

label=Label(win ,text=" ¿ ‽",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=7, column=0)
label=Label(win ,text=" ¿ ‽",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=7, column=8)
button_5.grid(row=7,column=1, columnspan=7)

label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=8, column=0)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=8, column=8)
button_6.grid(row=8,column=1, columnspan=7)

label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=9, column=0,columnspan=2)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=9, column=2,columnspan=2)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=9, column=4,columnspan=2)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=9, column=6,columnspan=2)
label=Label(win,text=" ‽ ‼",font=("Arial",12), fg="#000000",bg="#dbd2d2").grid(row=9, column=8,columnspan=2)

win.mainloop()

#E_N_D
