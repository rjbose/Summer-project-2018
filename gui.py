import tkinter as tk
import subprocess
import os

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self,width=1800,height=400)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    def go_super(self):
        cmd = subprocess.Popen(["sudo" , "bash"]) 



    def display_nic(self,T1):
        cmd = subprocess.Popen(["bash" , "./shell.sh"])
        T1.insert('end', open('output1.txt', 'r').read())


    def start_mon(self,T1,T2):
        inputValue = T1.get("1.0" , "end-1c") #Enter nic using which you'll start monitoring network
    #cmd = subprocess.check_call(["./shell2.sh", inputValue ],shell=True)
        with open('output2.txt','a') as f:
            f.write(inputValue)

        cmd = subprocess.Popen(["bash" , "./shell1.sh"])

        T2.insert('end', open('output3.txt', 'r').read())


    def airodump_1(self):
        cmd = subprocess.Popen(["bash" , "./shell2.sh"])


    def airodump_2(self,T3,T4):
        inputValue1 = T3.get("1.0" , "end-1c") #Enter bssid of desired router
        inputValue2 = T4.get("1.0" , "end-1c") #Enter Router Channel
    #cmd = subprocess.check_call(["./shell2.sh", inputValue ],shell=True)
        with open('output4.txt','a') as f:
            f.write(inputValue1)


        with open('output5.txt','a') as f:
            f.write(inputValue2)

        cmd = subprocess.Popen(["bash" , "./shell3.sh"])


    def aireplay(self):

        cmd = subprocess.Popen(["bash" , "./shell4.sh"])



    def reset(self):

        cmd = subprocess.Popen(["bash" , "./delete.sh"])



        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        button1 = tk.Button(self, text="Enable superuser",width=20,height=5,bg="light blue",font="courier 12 bold",
                            command=lambda: controller.go_super())
        #button.place(relx = 700,rely = 150)
        button1.grid(row=4,column=6)

        button1.pack()


        button2 = tk.Button(self, text="Next",width=20,height=5,bg="light blue",font="courier 12 bold",
                            command= lambda: controller.show_frame(PageOne))
        button2.place(relx = 700,rely = 150)
        

        button2.pack()
 
 


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       

        button3 = tk.Button(self, text="Display NICs",width=20,height=1,bg="light blue",font="courier 12 bold",
                            command= lambda: controller.display_nic(T1))
        button3.place(x = 700,y = 150)

        button3.pack()


        T1 = tk.Text(self , height=3, width=20)
        T1.place(x = 500, y=250)
       
        T1.pack() 


        label = tk.Label(self, text="Enter NIC", font="courier 12 bold",width=20,height=2)
        label.pack(pady=2,padx=2) 
        T2 = tk.Text(self , height=3, width=40)
        T2.place(x = 500, y=350)
        T2.pack()
        button4 = tk.Button(self, text = "Start Monitor Mode",width=20,height=1,bg="light blue",font="courier 12 bold", command=lambda: controller.start_mon(T1,T2))
        button4.place(x = 500,y = 450)
        button4.pack()

        button5 = tk.Button(self, text = "Next",width=20,height=1,bg="light blue",font="courier 12 bold", command=lambda: controller.show_frame(PageTwo))
        button5.place(x = 500,y = 450)
        button5.pack()


class PageTwo(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        button6 = tk.Button(self, text="Monitor nearby routers",width=20,height=5,bg="light blue",font="courier 12 bold",
                            command=lambda: controller.airodump_1())
        #button.place(relx = 700,rely = 150)
        button6.grid(row=4,column=6)

        button6.pack()

        label = tk.Label(self, text="Copy desired router bssid and click next", font="courier 8 bold",width=50,height=5)
        label.pack(pady=10,padx=10) 


        button7 = tk.Button(self, text="Next",width=20,height=5,bg="light blue",font="courier 12 bold",
                            command= lambda: controller.show_frame(PageThree))
        button7.place(relx = 700,rely = 150)
        

        button7.pack()



class PageThree(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Bssid", font="courier 9 bold",width=20,height=5)
        label1.pack(pady=10,padx=10)

        T3 = tk.Text(self , height=5, width=40)
        T3.place(x = 900, y=900)
        T3.pack()

        label2= tk.Label(self, text="Channel", font="courier 9 bold",width=20,height=5)
        label2.pack(pady=10,padx=10)

        T4 = tk.Text(self , height=5, width=40)
        T4.place(x = 900, y=900)
        T4.pack()

        button8 = tk.Button(self, text="Dump",width=20,height=5,bg="light blue",font="courier 8 bold",
                                command= lambda: controller.airodump_2(T3,T4))
        button8.place(relx = 700,rely = 150)
        button8.pack()

        button9 = tk.Button(self, text="Next",width=20,height=5,bg="light blue",font="courier 8 bold",
                                command= lambda: controller.show_frame(PageFour))
        button9.place(relx = 70,rely = 150)
        button9.pack()





class PageFour(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        button10 = tk.Button(self, text="Dos router",width=20,height=5,bg="light blue",font="courier 12 bold",
                                command= lambda: controller.aireplay())
        button10.place(relx = 700,rely = 150)
        button10.pack()

        button11 = tk.Button(self, text="Reset",width=20,height=5,bg="light blue",font="courier 12 bold",
                                command= lambda: controller.reset())
        button11.place(relx = 700,rely = 150)
        button11.pack()







   


app = SeaofBTCapp()
app.mainloop()
