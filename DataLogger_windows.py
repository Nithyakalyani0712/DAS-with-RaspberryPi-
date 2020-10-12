import tkinter as tk  
from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import Calendar, DateEntry
from time import strftime

mail_filename="mail_ids.txt"                                         #enter the filename to store mail id

class windowclass():
         
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,font="Helvetica 9 bold italic", width = 193,height=2, background = "white")
                self.label.grid(row=0,column=0)
                def clock():
                    time = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S %p")
                    self.label.config(text=time)
    #lab['text'] = time
                    master.after(1000, clock) # run itself again after 1000 ms

# run first time
                clock()
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=700)
                self.main_frame.grid(row=1,column=0)
               
                self.frame = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame.grid(row=1,column=0)
               
                self.label1=tk.Label(self.frame,text="CHANNEL 1",width=24,height=2,font="Helvetica 9 bold ",background="white").grid(row=0,column=0)
                self.label1=tk.Label(self.frame,text="650 C",width=24,height=2,background="white")
                self.label1.grid(row=1,column=0)
               
               
                self.label2=tk.Label(self.frame,text="LSV 850 C",width=24,height=1,background="white")
                self.label2.grid(row=2,column=0)
               
                self.label3=tk.Label(self.frame,text="HSV 750 C",width=24,height=2,background="white")
                self.label3.grid(row=3,column=0)
               
               
                self.frame1 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame1.grid(row=2,column=0)
               
                self.label1=tk.Label(self.frame1,text="CHANNEL 9",width=24,height=2,font="Helvetica 9 bold ",background="white").grid(row=0,column=0)
                self.label2=tk.Label(self.frame1,text="650 C",width=24,height=2,background="white").grid(row=1,column=0)
                self.label3=tk.Label(self.frame1,text="LSV 850 C",width=24,height=1,background="white").grid(row=2,column=0)
                self.label4=tk.Label(self.frame1,text="HSV 850 C",width=24,height=2,background="white").grid(row=3,column=0)
               
                self.frame2 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame2.grid(row=3,column=0)
               
                self.label1=tk.Label(self.frame2,text="CHANNEL 17",width=24,height=2,font="Helvetica 9 bold ",background="white").grid(row=0,column=0)
                self.label2=tk.Label(self.frame2,text="750 C",width=24,height=2,background="white").grid(row=1,column=0)
                self.label3=tk.Label(self.frame2,text="LSV 750 C",width=24,height=1,background="white").grid(row=2,column=0)
                self.label4=tk.Label(self.frame2,text="HSV 950 C",width=24,height=2,background="white").grid(row=3,column=0)
               
                self.frame3 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame3.grid(row=4,column=0)
               
                self.label1=tk.Label(self.frame3,text="CHANNEL 25",width=24,height=2,font="Helvetica 9 bold ",background="white").grid(row=0,column=0)
                self.label2=tk.Label(self.frame3,text="850 C",width=24,height=2,background="white").grid(row=1,column=0)
                self.label3=tk.Label(self.frame3,text="LSV 850 C",width=24,height=1,background="white").grid(row=2,column=0)
                self.label4=tk.Label(self.frame3,text="HSV 850 C",width=24,height=2,background="white").grid(row=3,column=0)
               
                self.frame4= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame4.grid(row=1,column=1)
               
                self.label2=tk.Label(self.frame4,text="CHANNEL 2",width=22,height=8,background="white").grid(row=0,column=0)
               
                self.frame5 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame5.grid(row=2,column=1)
               
                self.label2=tk.Label(self.frame5,text="CHANNEL 10",width=22,height=8,background="white").grid(row=0,column=0)
               
                self.frame6 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame6.grid(row=3,column=1)
                self.label2=tk.Label(self.frame6,text="CHANNEL 18",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame7 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame7.grid(row=4,column=1)
                self.label2=tk.Label(self.frame7,text="CHANNEL 26",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame8 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame8.grid(row=1,column=2)
                self.label2=tk.Label(self.frame8,text="CHANNEL 3",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame9 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame9.grid(row=2,column=2)
                self.label2=tk.Label(self.frame9,text="CHANNEL 11",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame10= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame10.grid(row=3,column=2)
                self.label2=tk.Label(self.frame10,text="CHANNEL 19",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame11 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame11.grid(row=4,column=2)
                self.label2=tk.Label(self.frame11,text="CHANNEL 27",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame12 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame12.grid(row=1,column=3)
                self.label2=tk.Label(self.frame12,text="CHANNEL 4",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame13 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame13.grid(row=2,column=3)
                self.label2=tk.Label(self.frame13,text="CHANNEL 12",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame14 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame14.grid(row=3,column=3)
                self.label2=tk.Label(self.frame14,text="CHANNEL 20",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame15= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame15.grid(row=4,column=3)
                self.label2=tk.Label(self.frame15,text="CHANNEL 28",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame16= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame16.grid(row=1,column=4)
                self.label2=tk.Label(self.frame16,text="CHANNEL 5",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame17 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame17.grid(row=2,column=4)
                self.label2=tk.Label(self.frame17,text="CHANNEL 13",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame18 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame18.grid(row=3,column=4)
                self.label2=tk.Label(self.frame18,text="CHANNEL 21",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame19 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame19.grid(row=4,column=4)
                self.label2=tk.Label(self.frame19,text="CHANNEL 29",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame20 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame20.grid(row=1,column=5)
                self.label2=tk.Label(self.frame20,text="CHANNEL 6",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame21 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame21.grid(row=2,column=5)
                self.label2=tk.Label(self.frame21,text="CHANNEL 14",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame22= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame22.grid(row=3,column=5)
                self.label2=tk.Label(self.frame22,text="CHANNEL 22",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame23 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame23.grid(row=4,column=5)
                self.label2=tk.Label(self.frame23,text="CHANNEL 30",width=22,height=8,background="white").grid(row=0,column=0)
                self.frame24 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame24.grid(row=1,column=6)
                self.label2=tk.Label(self.frame24,text="CHANNEL 7",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame25 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame25.grid(row=2,column=6)
                self.label2=tk.Label(self.frame25,text="CHANNEL 15",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame26 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame26.grid(row=3,column=6)
                self.label2=tk.Label(self.frame26,text="CHANNEL 23",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame27 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame27.grid(row=4,column=6)
                self.label2=tk.Label(self.frame27,text="CHANNEL 31",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame28= tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame28.grid(row=1,column=7)
                self.label2=tk.Label(self.frame28,text="CHANNEL 8",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame29 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame29.grid(row=2,column=7)
                self.label2=tk.Label(self.frame29,text="CHANNEL 16",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame30 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                self.frame30.grid(row=3,column=7)
                self.label2=tk.Label(self.frame30,text="CHANNEL 24",width=23,height=8,background="white").grid(row=0,column=0)
                self.frame31 = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=170, height=130)
                self.frame31.grid(row=4,column=7)
                self.label2=tk.Label(self.frame31,text="CHANNEL 32",width=23,height=8,background="white").grid(row=0,column=0)

                global photoimage
                global photoimage1
                global photoimage2
                global photoimage3
               
                #photo = Image.open( r"C:\Users\Admin\Downloads\icons8-home-144 (1).png")
               
                #photo = PhotoImage(file = r"C:\Users\Admin\Downloads\icons8-home-144 (1).png")
                photoimage = photo.subsample(3,2)
                photoimage1 = photo1.subsample(10, 7)
                photoimage2 = photo2.subsample(3, 3)
                photoimage3 = photo3.subsample(35, 35)
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                self.button= tk.Button(self.eframe5, text = 'DISPLAY',image=photoimage,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'PRINT SCREEN',image=photoimage1,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'MENU',image=photoimage2,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'DISPLAY', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'PRINT SCREEN', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'MENU', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.594, rely=0.05, height=35, width=50)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title( datetime.datetime.now())
       
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass1(self.newWindow1)
                   if(arg==2):
                           self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
                           
                           
                                   
                           
class windowclass1(windowclass):
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,font="Helvetica 9 bold italic", width = 193,height=2, background = "white")
                self.label.grid(row=0,column=0)
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=700)
                self.main_frame.grid(row=1,column=0)
                def clock():
                    time = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S %p")
                    self.label.config(text=time)
    #lab['text'] = time
                    master.after(1000, clock) # run itself again after 1000 ms

# run first time
                clock()
                vsb = tk.Scrollbar(self.main_frame, orient="vertical")
                vsb.grid(row=0, column=5, sticky='ns')
                canvas = tk.Canvas(self.main_frame, bg="white",width=1337,height=540)
                canvas.grid(row=0, column=2, sticky="news")
                scrollable_frame=tk.Frame(canvas)
                scrollable_frame.bind(
                        "<Configure>",
                        lambda e: canvas.configure(
                                scrollregion=canvas.bbox("all")
                                )
                        )
                canvas.create_window((0,0),window=scrollable_frame,anchor="nw")
                vsb['command']= canvas.yview
                canvas.configure(yscrollcommand=vsb.set)
                for i in range(32):
                        tk.Label(scrollable_frame,text="CHANNEL NAME",bg="lightblue",width=40,font="Helvetica 9 bold italic").grid(row=0,column=0)
                        tk.Label(scrollable_frame,text="Reading",bg="lightblue",width=35,font="Helvetica 9 bold italic").grid(row=0,column=1)
                        tk.Label(scrollable_frame,text="Alarm low set value",bg="lightblue",width=40,font="Helvetica 9 bold italic").grid(row=0,column=2)
                        tk.Label(scrollable_frame,text="Alarm high set value",bg="lightblue",width=35,font="Helvetica 9 bold italic").grid(row=0,column=3)
                        tk.Label(scrollable_frame,text="Alarm status",bg="lightblue",width=40,font="Helvetica 9 bold italic").grid(row=0,column=4)
                        if ((i%2)==0):
                               
                                tk.Label(scrollable_frame,text="Channel "+str(i+1),bg="white",width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=0)
                                tk.Label(scrollable_frame,text="27",bg="white",width=32,font="Helvetica 9 bold italic").grid(row=i+1,column=1)
                                tk.Label(scrollable_frame,text="26 C",bg="white",width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=2)
                                tk.Label(scrollable_frame,text="27.6 C",bg="white",width=32,font="Helvetica 9 bold italic").grid(row=i+1,column=3)
                                tk.Label(scrollable_frame,text="Normal",bg="white",width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=4)
                        else:
                                tk.Label(scrollable_frame,text="Channel "+str(i+1),width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=0)
                                tk.Label(scrollable_frame,text="27",width=32,font="Helvetica 9 bold italic").grid(row=i+1,column=1)
                                tk.Label(scrollable_frame,text="26 C",width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=2)
                                tk.Label(scrollable_frame,text="27.6 C",width=32,font="Helvetica 9 bold italic").grid(row=i+1,column=3)
                                tk.Label(scrollable_frame,text="Normal",width=40,font="Helvetica 9 bold italic").grid(row=i+1,column=4)
               
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")

                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                self.button= tk.Button(self.eframe5, text = 'DISPLAY',image=photoimage,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'PRINT SCREEN',image=photoimage1,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'MENU',image=photoimage2,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'DISPLAY', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'PRINT SCREEN', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'MENU', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.594, rely=0.05, height=35, width=50)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
        def new_window(self,arg):
                   self.master.withdraw()
                   if(arg==1):
                           self.newWindow1 = tk.Toplevel(self.master)
                           self.app =windowclass(self.newWindow1)
                   else:
                           super().new_window(arg)
class windowclass2(windowclass1):
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1, text = 'MAIN MENU',font="Helvetica 9 bold", width = 193,height=2, background = "white").grid(row=0,column=0)
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=545)
                self.main_frame.grid(row=1,column=0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title( "MAIN MENU")
                def button(enter,a):
                   global i
                   global j
                   tk.Button(self.main_frame,text=enter,width=20,height=5,bg="skyblue",command=lambda:self.enter(a)).grid(row=i,column=j,padx=94,pady=46)
                   j+=1
                   if j>=4:
                           i+=1
                           j=0
                button("Channel \nON / OFF",1)
                button("Log \nInterval",2)
                button("EMAIL ID\nSETTING",3)
                button("Report",4)
                button("HISTORY VIEW",5)
                button("COPY TO\nPENDRIVE",6)
                button("PRINT RECORDS",7)
                button("EMAIL RECORDS",8)
                button("ERASE RECORDS",9)
                button("DATE AND\n TIME",10)
                button("ALARM SET \nVALUES",11)
                button("DATE LOGGER\n INFO",12)
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=117)
                self.eframe5.grid(row=5,column=0)
                global photoimage4
                global photoimage5
                global photoimage6
               
               
                #photo = Image.open( r"C:\Users\Admin\Downloads\icons8-home-144 (1).png")
               
                #photo = PhotoImage(file = r"C:\Users\Admin\Downloads\icons8-home-144 (1).png")
                photoimage4 = photo4.subsample(3,3)
                photoimage5 = photo5.subsample(4,4)
                photoimage6 = photo6.subsample(3,3)
                self.button= tk.Button(self.eframe5, text = 'HOME',image=photoimage4,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'FACTORY',image=photoimage5,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'SUPERVISORY',image=photoimage6,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'HOME', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'FACTORY', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'SUPERVISORY', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.584, rely=0.05, height=35, width=80)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
               
        def home(self):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.app = windowclass(self.newWindow1)
                   self.master.withdraw()
        def menu(self):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.app = windowclass2(self.newWindow1)
                   self.master.withdraw()
        def enter(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass3(self.newWindow1)
                   if(arg==2):
                           self.app =windowclass4(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass5(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass6(self.newWindow1)
                   if(arg==5):
                           self.app =windowclass7(self.newWindow1,"History view","REPORT VIEW","GRAPH VIEW")
                   if(arg==6):
                           self.app =windowclass8(self.newWindow1)
                   if(arg==7):
                           self.app =windowclass9(self.newWindow1,"Print mode","PRINT","Print Records")
                   if(arg==8):
                           self.app =windowclass9(self.newWindow1,"Email mode","EMAIL","Email Records")
                   if(arg==9):
                           self.app =windowclass7(self.newWindow1,"Erase records","ERASE","ERASE ALL")
                   if(arg==10):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==11):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==12):
                           pass
class windowclass3(windowclass2):
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.main_frame1.grid_propagate(0)
                self.label= tk.Label(self.main_frame1, text = 'CHANNELS',font="Helvetica 10 bold", width = 196,height=2, background = "white").grid(row=0,column=0)
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1368, height=545)
                self.main_frame.grid(row=1,column=0)
                self.main_frame.grid_propagate(0)
               
                def frames(a):
                        global i,j
               
                        self.frame = tk.Frame(self.main_frame,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF",width=170, height=130)
                        self.frame.grid(row=i,column=j)
                        j+=1
                        if j>=8:
                                j=0
                                i+=1
                        v = tk.IntVar()
                        v.set(2)
                        def selection():  
                                selection = print( v.get())
               
                        self.label1=tk.Label(self.frame,text="CHANNEL "+str(a),width=23,height=2,font="Helvetica 9 bold ",background="white").grid(row=0,column=0)
                        self.radio1=tk.Radiobutton(self.frame,text="ON",font="Helvetica 9 bold ",value=1,variable=v,width=14,height=2,background="white",command=selection).grid(row=1,column=0)
                        self.radio2=tk.Radiobutton(self.frame,text="OFF",font="Helvetica 9 bold ",value=2,width=14,variable=v,height=3,background="white",command=selection).grid(row=2,column=0)
                for b in range(32):
                        frames(b+1)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title( "MAIN MENU")
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1385, height=117)
                self.eframe5.grid(row=5,column=0)
                self.eframe5.grid_propagate(0)
               
                global photoimage7
                global photoimage8
                global photoimage4
                global photoimage3
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                photoimage7 = photo7.subsample(35,35)
                photoimage8 = photo8.subsample(3,3)
                self.button= tk.Button(self.eframe5, text = 'HOME',image=photoimage4,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'SAVE',image=photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK',image=photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'HOME', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'SAVE', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'BACK', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.584, rely=0.05, height=35, width=80)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
               
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass1(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
class windowclass4(windowclass2):
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.main_frame1.grid_propagate(0)
                self.label= tk.Label(self.main_frame1, text = 'LOG INTERVAL',font="Helvetica 10 bold", width = 193,height=2, background = "white").grid(row=0,column=0)
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=545)
                self.main_frame.grid(row=1,column=0)
                self.main_frame.grid_propagate(0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title( "MAIN MENU")
                number1 = tk.StringVar()  
                number2 = tk.StringVar()
                number3 = tk.StringVar()  
                number4 = tk.StringVar()
                def save():
                        print(number1.get())
                        print(number2.get())
                        print(number3.get())
                        print(number4.get())
                self.label1=tk.Label(self.main_frame,text="HOURS",width=23,height=3,font="Helvetica 15 bold ",background="white").grid(row=0,column=0,sticky="NEWS")
                self.label1=tk.Label(self.main_frame,text="MINUTES",width=23,height=3,font="Helvetica 15 bold ",background="white").grid(row=0,column=1,sticky="NEWS")
                self.label1=tk.Label(self.main_frame,text="SECONDS",width=23,height=3,font="Helvetica 15 bold ",background="white").grid(row=0,column=2,sticky="NEWS")
                self.label1=tk.Label(self.main_frame,text="MILLI SECONDS",width=23,height=3,font="Helvetica 15 bold ",background="white").grid(row=0,column=3,sticky="NEWS")
                self.entry1=tk.Entry(self.main_frame,textvariable=number1,width=10,font="Helvetica 15 bold ",relief="solid",background="white").grid(row=1,column=0,sticky="NEWS",padx=94,pady=43)
                self.entry2=tk.Entry(self.main_frame,textvariable=number2,width=10,font="Helvetica 15 bold ",relief="solid",background="white").grid(row=1,column=1,sticky="NEWS",padx=94,pady=43)
                self.entry3=tk.Entry(self.main_frame,textvariable=number3,width=10,font="Helvetica 15 bold ",relief="solid",background="white").grid(row=1,column=2,sticky="NEWS",padx=94,pady=43)
                self.entry4=tk.Entry(self.main_frame,textvariable=number4,width=10,font="Helvetica 15 bold ",relief="solid",background="white").grid(row=1,column=3,sticky="NEWS",padx=94,pady=43)
                #print(self.entry1.get())
                #self.label1=tk.Label(self.main_frame,text=" ",width=72,height=26,font="Helvetica 9 bold ",background="white").grid(row=2,column=3,sticky="NEWS")
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=117)
                self.eframe5.grid(row=5,column=0)
                self.eframe5.grid_propagate(0)
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                self.button= tk.Button(self.eframe5, text = 'HOME',image=photoimage4,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'SAVE',image=photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK',image=photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'HOME', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'SAVE', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'BACK', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.584, rely=0.05, height=35, width=80)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)


class windowclass5(windowclass4):
        def __init__(self , master):
                def mail_file(mail):                                  # write mail id to file
                    mail=mail
                    try:
                        ff=open(mail_filename,"a")
                        ff.write(mail+"\n")
                       
                    except:
                        ff.close()
                        mail_file(mail)
                   
                    finally:
                        ff.close()  
                def show_mail_id(con=1):                                   # show the mails from file
                   
                    r=1
                    try:
                        ff=open(mail_filename,"r")
                    except:
                        ff=open(mail_filename,"a")
                        ff.close()
                        show_mail_id()
                    if(con==0):
                        print("should be deleted")
                        self.master.withdraw()
                        self.newWindow1 = tk.Toplevel(self.master)
                        self.app =windowclass5(self.newWindow1)
                           
                    try:
                        for emails in ff:
                            email_label=tk.Label(scrollable_frame,text=r,width=20,height=2,bg="white",font="Helvetica 10 bold italic")
                            email_label.grid(row=r,column=0,pady=2,padx=2)
                            email_label1=tk.Label(scrollable_frame,text=emails,width=128,bg="white",font="Helvetica 10 bold italic")
                            email_label1.grid(row=r,column=1,pady=2,padx=2)
                            r+=1
                       
                    except:
                        try:
                            ff.close()
                            ff=open(mail_filename,"r")
                            show_mail_id()
                        except:
                            pass
                    finally:
                            ff.close()

                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=50)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,font="Helvetica 9 bold italic", width = 193,height=2, background = "white")
                self.label.grid(row=0,column=0)
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=550)
                self.main_frame.grid(row=1,column=0)
                self.mainframe = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1065, height=530)
                self.mainframe.grid(row=1,column=0)
                self.main_frame.grid_propagate(0)
               
                self.label= tk.Label(self.main_frame,text="Max.Char.50",font="Helvetica 11 bold italic", width =25,height=2, background = "white")
                self.label.place(relx=0.875, rely=0.007, height=50, width=90)
                vsb = tk.Scrollbar(self.mainframe, orient="vertical")
                vsb.grid(row=1, column=4, sticky='ns')
                canvas = tk.Canvas(self.mainframe, bg="white",width=1200,height=400)
                canvas.grid(row=1, column=3, sticky="ne")
                canvas.grid_propagate(0)
                scrollable_frame=tk.Frame(canvas)
                scrollable_frame.bind(
                        "<Configure>",
                        lambda e: canvas.configure(
                                scrollregion=canvas.bbox("all")
                                )
                        )
                canvas.create_window((0,0),window=scrollable_frame,anchor="nw")
                vsb['command']= canvas.yview
                canvas.configure(yscrollcommand=vsb.set)
                #for i in range(32):
                list1=[]

               
                show_mail_id()                                                          #show the mail at the starting





                def check_mail(answer):                                                        # check for proper mail id    
                    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                    if(re.search(regex,answer)):  
                        return True
         
                    else:  
                        return False
                def duplicate(email):
                    try:
                        with open(mail_filename) as ff:
                            for line in ff:
                                if(line.lower().rstrip()==email):
                                    return(True)
                                           
                    except Exception:
                        pass
                     
                   
                def create(text="Enter your Mail ID:"):
                        print("clicked")
                        global i
                        answer = simpledialog.askstring("Input",text,
                                parent=master)
                           
                        if(check_mail(answer)):
                            if(duplicate(answer)):
                                create(text="Email is already registered !!!")
                            else:
                               
                                mail_file(answer)                                                  # function to store new gmail in  file
                                print("Your MAIL ID is ", answer)
                        else:
                            create(text="Your mail id is not valid enter valid mail id")       # called if mail id is not valid
                           
                            print("please enter valid mail id")
                        show_mail_id()                                                         # function to display mail ids

                #def delete():
                def test(intvar_dict):
                    print("here")
                    a=[]
                    intvar_dict=intvar_dict
                    for key, value in intvar_dict.items():
                        if value.get() > 0:
                            a.append(key)
                    if(len(a)==0):
                        return 0
                       

 
                    ff=open(mail_filename,"r")
                    lst = []
                   
                    for line in ff:
                        for word in a:
                            if word in line:
                                print("del "+ word)
                                line = line.replace(word,'')
                            lst.append(line)
                    ff.close()
                    ff = open(mail_filename,'w')
                    for line in lst:
                        ff.write(line)
                        print(line)
                    ff.close()
                    show_mail_id(con=0)
                   
                check_box_list = []
                def delete_checkbutton():                                               #delete checkbutton
                    print(check_box_list)
                    for i in check_box_list:
                        i.pack_forget()    # forget checkbutton
                        i.destroy()        # use destroy if you dont need those checkbuttons in future


                def delete():
                    r=1
                    intvar_dict = {}
                    checkbutton_list = []
                    for cb in checkbutton_list:
                        cb.destroy()
                    checkbutton_list.clear()
                    try:
                        ff=open(mail_filename,"r")
                    except:
                        ff.close()
                        ff=open(mail_filename,"r")
                               
                   
                    intvar_dict.clear()
                    for cb in checkbutton_list:
                        cb.destroy()
                    checkbutton_list.clear()
                    for emails in ff:
                        intvar_dict[emails] = tk.IntVar()
                        c = Checkbutton( scrollable_frame, variable=intvar_dict[emails])
                        c.grid(row=r,column=0,pady=2)
                        checkbutton_list.append(c)
                        check_box_list.append(c)
                        r+=1
                    ff.close()
                    btn1 = Button(self.main_frame,text="Delete selected", bg="lightblue",command=lambda:(c.destroy(),btn1.destroy(),test(intvar_dict),delete_checkbutton()))
                    btn1.place(relx=0.465,rely=0.89,height=40,width=90)
                   
                       

                                   
                       
                tk.Label(scrollable_frame,text="S.No",bg="lightblue",width=20,font="Helvetica 10 bold ").grid(row=0,column=0)
                tk.Label(scrollable_frame,text="Email ID",bg="lightblue",width=128,font="Helvetica 10 bold ").grid(row=0,column=1)
                self.button= tk.Button(self.main_frame, text = 'CREATE NEW', width = 5,height=5, background = "lightblue",command=lambda:create())
                self.button1= tk.Button(self.main_frame, text = 'DELETE', width = 5,height=5 ,background = "lightblue",command=lambda:delete())
                self.button.place(relx=0.275, rely=0.89, height=50, width=90)
                self.button1.place(relx=0.634, rely=0.89, height=50, width=90)
               
               
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
               
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                self.button= tk.Button(self.eframe5, text = 'HOME',image=photoimage4,command= lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'SAVE',image=photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK',image=photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',image=photoimage3,command=lambda:self.new_window(4))
                self.button10= tk.Label(self.eframe5, text = 'HOME', width = 5,height=5,bg="white")
                self.button11= tk.Label(self.eframe5, text = 'SAVE', width = 5,height=5 ,bg="white")
                self.button12= tk.Label(self.eframe5, text = 'BACK', width = 5,height=5,bg="white" )
                self.button13= tk.Label(self.eframe5, text = 'HELP', width = 5,height=5,bg="white" )
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)              
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
                self.button10.place(relx=0.075, rely=0.05, height=35, width=60)
                self.button11.place(relx=0.320, rely=0.05, height=35, width=90)              
                self.button12.place(relx=0.584, rely=0.05, height=35, width=80)
                self.button13.place(relx=0.847, rely=0.05, height=30, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
class windowclass6():
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=60)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,text="Report Logo, Header & Footer",font="Helvetica 16 bold ", width = 100,height=2, background = "white")
                self.label.grid(row=0,column=0,sticky="w")
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=550)
                self.main_frame.grid(row=1,column=0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")
                self.main_frame.grid_propagate(0)
                self.main_frame1.grid_propagate(0)
                self.label=tk.Label(self.main_frame, text = "Template Name:", width=50,bg="white",font = ("Times New Roman", 18)).place(relx=0.125, rely=0.03)
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                # Combobox creation
                n = tk.StringVar()
                self.templates = ttk.Combobox(self.main_frame, width = 27, textvariable = n,font = ("Times New Roman", 14))

                # Adding combobox drop down list
                self.templates['values'] = (' Template 1',' Template 2',' Template 3')

                self.templates.place(relx=0.435, rely=0.037)
                self.templates.current(1)
                tk.Label(self.main_frame, text = "Logo:", width=50,bg="white",font = ("Times New Roman", 18)).place(relx=0.160, rely=0.16)
                self.button= tk.Button(self.main_frame, text = 'Browse',bg="skyblue",font = ("Times New Roman", 15), width = 12,height=1 ,command=lambda:self.new_window(1)).place(relx=0.435, rely=0.16)
                tk.Label(self.main_frame, text = "Logo.png", width=10,bg="white",font = ("Times New Roman", 18)).place(relx=0.560, rely=0.16)
                tk.Label(self.main_frame, text = "Logo", width=80,height=35,image = photoimage4,bg="white",font = ("Times New Roman", 18)).place(relx=0.660, rely=0.16)
                tk.Label(self.main_frame, text = "Header Line 1:", width=30,bg="white",font = ("Times New Roman", 18)).place(relx=0.223, rely=0.29)
                               
                tk.Label(self.main_frame, text = "Header Line 2:", width=30,bg="white",font = ("Times New Roman", 18)).place(relx=0.223, rely=0.39)
                tk.Label(self.main_frame, text = "Header Line 3:", width=30,bg="white",font = ("Times New Roman", 18)).place(relx=0.223, rely=0.49)
                tk.Label(self.main_frame, text = "Footer left:", width=30,bg="white",font = ("Times New Roman", 18)).place(relx=0.237, rely=0.59)
                tk.Label(self.main_frame, text = "Footer Right:", width=30,bg="white",font = ("Times New Roman", 18)).place(relx=0.229, rely=0.69)
                #tk.Label(self.main_frame, text = "Logo", width=80,height=35,bg="white",font = ("Times New Roman", 18)).place(relx=0.660, rely=0.13)
                tk.Button(self.main_frame, text = "Create New Template", width=20,bg="skyblue",font = ("Times New Roman", 18)).place(relx=0.123, rely=0.83)
                tk.Button(self.main_frame, text = "Delete", width=10,bg="skyblue",font = ("Times New Roman", 18)).place(relx=0.47, rely=0.83)
                tk.Button(self.main_frame, text = "Preview", width=10,bg="skyblue",font = ("Times New Roman", 18)).place(relx=0.729, rely=0.83)
                e1 = tk.Entry(self.main_frame,width=60,font = ("Times New Roman", 18),relief='solid',highlightcolor='gray').place(relx=0.423, rely=0.29)
                e2 = tk.Entry(self.main_frame,width=60,relief='solid',font = ("Times New Roman", 18)).place(relx=0.423, rely=0.39)
                e3 = tk.Entry(self.main_frame,width=60,relief='solid',font = ("Times New Roman", 18)).place(relx=0.423, rely=0.49)
                e4 = tk.Entry(self.main_frame,width=60,relief='solid',font = ("Times New Roman", 18)).place(relx=0.423, rely=0.59)
                e5 = tk.Entry(self.main_frame,width=60,relief='solid',font = ("Times New Roman", 18)).place(relx=0.423, rely=0.69)
               
                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                self.button= tk.Button(self.eframe5, text = 'HOME', image = photoimage4, width = 5,height=5 ,command=lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'SAVE', image = photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK', image = photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',  image = photoimage3,command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
class windowclass7():
        def __init__(self , master,topic,b1text,b2text):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=60)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,text=topic,font="Helvetica 16 bold ", width = 100,height=2, background = "white")
                self.label.grid(row=0,column=0,sticky="w")
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=550)
                self.main_frame.grid(row=1,column=0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")
                self.main_frame.grid_propagate(0)
                self.main_frame1.grid_propagate(0)
                self.label=tk.Label(self.main_frame,text="From date:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.075, rely=0.03)
                self.label=tk.Label(self.main_frame,text="To date:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.5075, rely=0.03)
                e2 = tk.Entry(self.main_frame,width=40,relief='solid',font = ("Times New Roman", 14)).place(relx=0.198, rely=0.039)
                e3 = tk.Entry(self.main_frame,width=40,relief='solid',font = ("Times New Roman", 14)).place(relx=0.623, rely=0.039)
               
                a1=0.05
                b1=0.17
                for i in range(32):
                       
                        c = Checkbutton( self.main_frame, text="Ch"+str(i+1))
                        a1+=0.1
                        if a1>0.9:
                                b1+=0.2
                                a1=0.15
                        c.place(relx=a1, rely=b1)
                        #checkbutton_list.append(c)

                self.button= tk.Button(self.main_frame, text = 'RESET',height=2,width=10,bg="lightblue",command=lambda:self.new_window(1))
                self.button1= tk.Button(self.main_frame, text = 'SELECT ALL',height=2,width=10,bg="lightblue",command=lambda:self.new_window(2))
                self.button2= tk.Button(self.main_frame, text = b1text,height=2,width=10,bg="lightblue", command=lambda:self.new_window(3))
                self.button3= tk.Button(self.main_frame, text = b2text,height=2,width=10,bg="lightblue", command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.85)
                self.button1.place(relx=0.334, rely=0.85)
                self.button2.place(relx=0.594, rely=0.85)
                self.button3.place(relx=0.847, rely=0.85)

                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                self.button= tk.Button(self.eframe5, text = 'HOME', image = photoimage4, width = 5,height=5 ,command=lambda:self.new_window(1))
                self.button1= tk.Button(self.eframe5, text = 'SAVE', image = photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK', image = photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',  image = photoimage3,command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                self.button1.place(relx=0.334, rely=0.3, height=50, width=50)
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
class windowclass8():
        def __init__(self , master):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=60)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,text="Copy to Pendrive",font="Helvetica 16 bold ", width = 100,height=2, background = "white")
                self.label.grid(row=0,column=0,sticky="w")
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=550)
                self.main_frame.grid(row=1,column=0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")
                self.main_frame.grid_propagate(0)
                self.main_frame1.grid_propagate(0)
                def selection():
                        pass
                v = tk.IntVar()
               
                self.label=tk.Label(self.main_frame,text="Copy Mode:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.075, rely=0.1)
                self.radio1=tk.Radiobutton(self.main_frame,text="Auto",font="Helvetica 15 bold ",value=1,variable=v,background="white",command=selection)
                self.radio2=tk.Radiobutton(self.main_frame,text="Manual",font="Helvetica 15 bold ",value=2,variable=v,background="white",command=selection)
                v.set(2)
                self.radio1.place(relx=0.2,rely=0.099)
                self.radio2.place(relx=0.28,rely=0.099)
                hours= tk.IntVar()
                minutes = tk.IntVar()
                hours.set(24)
                minutes.set(58)
                       
                self.label=tk.Label(self.main_frame,text="Auto delay:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.5075, rely=0.1)
                self.label=tk.Label(self.main_frame,text="Hours",font="Helvetica 13 ",width = 10, background = "white").place(relx=0.603, rely=0.04)
                self.label=tk.Label(self.main_frame,text="Minutes",font="Helvetica 13 ", width = 10, background = "white").place(relx=0.665, rely=0.04)
                e2 = tk.Entry(self.main_frame,width=5,relief="solid",textvariable=hours,font = ("Helvetica", 14)).place(relx=0.680, rely=0.1)
                e3 = tk.Entry(self.main_frame,width=5,relief="solid",textvariable=minutes,font = ("Helvetica", 14)).place(relx=0.623, rely=0.1)
                self.label=tk.Label(self.main_frame,text="From date:",font="Helvetica 16 bold ",width = 10, background = "white").place(relx=0.075, rely=0.27)
                self.label=tk.Label(self.main_frame,text="To date:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.5075, rely=0.27)
                e2 = tk.Entry(self.main_frame,width=40,relief="solid",font = ("Times New Roman", 14)).place(relx=0.198, rely=0.279)
                e3 = tk.Entry(self.main_frame,width=40,relief="solid",font = ("Times New Roman", 14)).place(relx=0.623, rely=0.279)
               
                a1=0.05
                b1=0.37
                for i in range(32):
                       
                        c = Checkbutton( self.main_frame, text="Ch"+str(i+1))
                        a1+=0.1
                        if a1>0.9:
                                b1+=0.15
                                a1=0.15
                        c.place(relx=a1, rely=b1)
                        #checkbutton_list.append(c)

                self.button= tk.Button(self.main_frame, text = 'RESET',height=2,width=10,bg="lightblue",command=lambda:self.new_window(1))
                self.button1= tk.Button(self.main_frame, text = 'SELECT ALL',height=2,width=10,bg="lightblue",command=lambda:self.new_window(2))
                self.button2= tk.Button(self.main_frame, text = 'COPY CSV',height=2,width=10,bg="lightblue", command=lambda:self.new_window(3))
                self.button3= tk.Button(self.main_frame, text = 'COPY PDF',height=2,width=10,bg="lightblue", command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.9)
                self.button1.place(relx=0.334, rely=0.9)
                self.button2.place(relx=0.594, rely=0.9)
                self.button3.place(relx=0.847, rely=0.9)

                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                self.button= tk.Button(self.eframe5, text = 'HOME', image = photoimage4, width = 5,height=5 ,command=lambda:self.new_window(1))
                #self.button1= tk.Button(self.eframe5, text = 'SAVE', image = photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK', image = photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',  image = photoimage3,command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                #self.button1.place(relx=0.334, rely=0.3, height=50, width=50)
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)
class windowclass9():
        def __init__(self , master,mode,btext,main_text):
                self.master = master
                self.main_frame1 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=60)
                self.main_frame1.grid(row=0,column=0)
                self.label= tk.Label(self.main_frame1,text=main_text,font="Helvetica 16 bold ", width = 100,height=2, background = "white")
                self.label.grid(row=0,column=0,sticky="w")
                self.main_frame = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=550)
                self.main_frame.grid(row=1,column=0)
                self.master.state("zoomed")
                self.master.configure(background="#FFFFFF")
                master.title("MAIN WINDOW")
                self.main_frame.grid_propagate(0)
                self.main_frame1.grid_propagate(0)
                def selection():
                        pass
                v = tk.IntVar()
               
                self.label=tk.Label(self.main_frame,text=mode,font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.075, rely=0.1)
                self.radio1=tk.Radiobutton(self.main_frame,text="Auto",font="Helvetica 15 bold ",value=1,variable=v,background="white",command=selection)
                self.radio2=tk.Radiobutton(self.main_frame,text="Manual",font="Helvetica 15 bold ",value=2,variable=v,background="white",command=selection)
                v.set(2)
                self.radio1.place(relx=0.2,rely=0.099)
                self.radio2.place(relx=0.28,rely=0.099)
                hours= tk.IntVar()
                minutes = tk.IntVar()
                hours.set(24)
                minutes.set(58)
                       
                self.label=tk.Label(self.main_frame,text="Auto delay:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.5075, rely=0.1)
                self.label=tk.Label(self.main_frame,text="Hours",font="Helvetica 13 ",width = 10, background = "white").place(relx=0.603, rely=0.04)
                self.label=tk.Label(self.main_frame,text="Minutes",font="Helvetica 13 ", width = 10, background = "white").place(relx=0.665, rely=0.04)
                e2 = tk.Entry(self.main_frame,width=5,relief="solid",textvariable=hours,font = ("Helvetica", 14)).place(relx=0.680, rely=0.1)
                e3 = tk.Entry(self.main_frame,width=5,relief="solid",textvariable=minutes,font = ("Helvetica", 14)).place(relx=0.623, rely=0.1)
                self.label=tk.Label(self.main_frame,text="From date:",font="Helvetica 16 bold ",width = 10, background = "white").place(relx=0.075, rely=0.27)
                self.label=tk.Label(self.main_frame,text="To date:",font="Helvetica 16 bold ", width = 10, background = "white").place(relx=0.5075, rely=0.27)
                e2 = tk.Entry(self.main_frame,width=40,relief="solid",font = ("Times New Roman", 14)).place(relx=0.198, rely=0.279)
                e3 = tk.Entry(self.main_frame,width=40,relief="solid",font = ("Times New Roman", 14)).place(relx=0.623, rely=0.279)
               
                a1=0.05
                b1=0.37
                for i in range(32):
                       
                        c = Checkbutton( self.main_frame, text="Ch"+str(i+1))
                        a1+=0.1
                        if a1>0.9:
                                b1+=0.15
                                a1=0.15
                        c.place(relx=a1, rely=b1)
                        #checkbutton_list.append(c)

                self.button= tk.Button(self.main_frame, text = 'RESET',height=2,width=10,bg="lightblue",command=lambda:self.new_window(1))
                self.button1= tk.Button(self.main_frame, text = 'SELECT ALL',height=2,width=10,bg="lightblue",command=lambda:self.new_window(2))
                self.button2= tk.Button(self.main_frame, text = btext,height=2,width=10,bg="lightblue", command=lambda:self.new_window(3))
                #self.button3= tk.Button(self.main_frame, text = 'COPY PDF',height=2,width=10,bg="lightblue", command=lambda:self.new_window(4))
                self.button.place(relx=0.095, rely=0.9)
                self.button1.place(relx=0.434, rely=0.9)
                self.button2.place(relx=0.794, rely=0.9)
                #self.button3.place(relx=0.847, rely=0.9)

                self.eframe5 = tk.Frame(master,highlightthickness=1,borderwidth="2",relief="groove",background="#FFFFFF", width=1365, height=128)
                self.eframe5.grid(row=5,column=0)
                global photoimage7
                global photoimage8
                global photoimage3
                global photoimage4
                photoimage3 = photo3.subsample(35, 35)
                photoimage4 = photo4.subsample(3, 3)
                photoimage7 = photo7.subsample(13,13)
                photoimage8 = photo8.subsample(4,4)
                self.button= tk.Button(self.eframe5, text = 'HOME', image = photoimage4, width = 5,height=5 ,command=lambda:self.new_window(1))
                #self.button1= tk.Button(self.eframe5, text = 'SAVE', image = photoimage7,command=lambda:self.new_window(2))
                self.button2= tk.Button(self.eframe5, text = 'BACK', image = photoimage8,command=lambda:self.new_window(3))
                self.button3= tk.Button(self.eframe5, text = 'HELP',  image = photoimage3,command=lambda:self.new_window(4))
                self.button.place(relx=0.075, rely=0.3, height=50, width=50)
                #self.button1.place(relx=0.334, rely=0.3, height=50, width=50)
                self.button2.place(relx=0.594, rely=0.3, height=50, width=50)
                self.button3.place(relx=0.847, rely=0.3, height=50, width=50)
        def new_window(self,arg):
                   self.newWindow1 = tk.Toplevel(self.master)
                   self.master.withdraw()
                   if(arg==1):
                           self.app =windowclass(self.newWindow1)
                   if(arg==2):
                           pass #self.app =windowclass1(self.newWindow1)
                   if(arg==3):
                           self.app =windowclass2(self.newWindow1)
                   if(arg==4):
                           self.app =windowclass2(self.newWindow1)

       
                       
a=1                
i=0
j=0
a1=0.05
b1=0.37
root = tk.Tk()

photo =tk.PhotoImage(file = r"display.png")        #display.png
photo1 =tk.PhotoImage(file = r"screen.png")        #icons8-home-144 (1)
photo2 =tk.PhotoImage(file = r"menu1.png")
photo3 =tk.PhotoImage(file = r"help.png")
photo4 =tk.PhotoImage(file = r"icons8-home-144.png")        #display.png
photo5 =tk.PhotoImage(file = r"factory.png")        #icons8-home-144 (1)
photo6 =tk.PhotoImage(file = r"supervisor.png")
photo7 =tk.PhotoImage(file = r"save.png")        #icons8-home-144 (1)
photo8 =tk.PhotoImage(file = r"back.png")
windowclass(root)

root.mainloop()
