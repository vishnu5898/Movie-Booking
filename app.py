from tkinter import *
root = Tk()
root.title("Movie Booking")
root.geometry("800x640+250+25")

global count
count=0

# ********************************* Classes definition ************************************
class seats():
    take=StringVar()
    seats_booked=[]
    seats_available=[]
    seats_read=[]
    
    
    def __init__(self):
        with open("seats.txt","r") as f:
            a=f.readline()
            a=a.split()
            for i in a:
                i=int(i)
                self.seats_booked.append(i)
        self.get_available(self.seats_booked)
        #self.seat_ava_read()
        
    def seat_ava_read(self):
        self.seats_read=[]
        with open("seat_available.txt","r") as f:
            a=f.readline()
            a=a.split()
            for i in a:
                i=int(i)
                self.seats_read.append(i)
        
    def get_available(self,b):
        a=range(1,11)
        i=0
        j=0
        while(j<len(b) or j<10):
            while(i<len(a)):
                if(j<len(b)):
                    if(a[i]==b[j]):
                        i+=1
                        break
                self.seats_available.append((a[i]))
                i+=1
            j+=1
        with open("seat_available.txt","w") as f:
            for i in self.seats_available:
                f.write(str(i)+" ")
        i=0
        while(i<len(self.seats_available)):
            self.seats_available.pop(i)

                
    def scan(self,seat_no):
        count=0
        for i in self.seats_booked:
            if(i==seat_no):
                return count
            count+=1
            
    def remove_seat(self,seat_no):
        a=self.scan(self,seat_no)
        self.seats_booked.pop(a)
        self.seats_booked.sort
        print(self.seats_booked)
        with open("seats.txt","w") as f:
            for i in self.seats_booked:
                f.write(str(i)+" ")

    def add_seat(self,seat_no):
        self.seats_booked.append(seat_no)
        self.seats_booked.sort()
        with open("seats.txt","w") as f:
            for i in self.seats_booked:
                f.write(str(i)+" ")           
        self.get_available(seats,self.seats_booked)
                
class ticket():
    def __init__(self):
        pass
        
    
    def unbook(self,seat_no):
        check=self.check_seat_availability(seat_no)
        if not check:
            seats.remove_seat(seats,seat_no)
            print("Successfully unbooked the Seat No.",seat_no)
        else:
            print("The seat is not booked")
        
    def book(self,seat_no):
        check=self.check_seat_availability(seat_no)
        if check:
            if(seat_no<11 and seat_no>0):
                label = Label(anchor="center",width=25,text="",bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=200)
                label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=250)
                #label = Label(text="Total 10 seats are there",bg="black",fg="white",font=("Courier",20))
                #label.place(x=200,y=235)
                label = Label(anchor="center",width=20,text="",bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=200)
                label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=250)
                #bring_entry_box()
                seats.add_seat(seats,seat_no)
                seats.seat_ava_read(seats)
                label = Label(anchor="center",width=20,text=seats.seats_booked,bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=375)
                label = Label(text="Seat No. "+str(seat_no)+" booked successfully",bg="black",fg="white",font=("Courier",18))
                label.place(x=200,y=425)
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=450)
                label = Label(anchor="center",text="Seats available",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=475)
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=500)
                label = Label(anchor="center",text=seats.seats_read,width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=525)
            else:
                label = Label(anchor="center",width=25,text="",bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=200)
                label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=250)
                #label = Label(text="Total 10 seats are there",bg="black",fg="white",font=("Courier",20))
                #label.place(x=200,y=235)
                label = Label(anchor="center",width=20,text="",bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=200)
                label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=250)
                #bring_entry_box()
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=200,y=425)
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=375)
                label = Label(anchor="center",text="Invalid Seat No.",width=25,bg="black",fg="white",font=("Courier",18))
                label.place(x=215,y=425)
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=450)
                label = Label(anchor="center",text="Seats available",width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=475)
                label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=500)
                label = Label(anchor="center",text=seats.seats_read,width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=250,y=525)
        elif(len(seats.seats_booked)!=10):
            label = Label(anchor="center",width=25,text="",bg="black",fg="white",font=("Courier",18))
            label.place(x=50,y=200)
            label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=50,y=250)
            #label = Label(text="Total 10 seats are there",bg="black",fg="white",font=("Courier",20))
            #label.place(x=200,y=235)
            label = Label(anchor="center",width=20,text="",bg="black",fg="white",font=("Courier",18))
            label.place(x=450,y=200)
            label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=450,y=250)
            #bring_entry_box()
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
            label = Label(text="Seat No. "+str(seat_no)+" not available",bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=450)
            label = Label(anchor="center",text="Seats available",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=475)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=500)
            label = Label(anchor="center",text=seats.seats_read,width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=525)
        else:
            label = Label(anchor="center",width=25,text="",bg="black",fg="white",font=("Courier",18))
            label.place(x=50,y=200)
            label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=50,y=250)
            #label = Label(text="Total 10 seats are there",bg="black",fg="white",font=("Courier",20))
            #label.place(x=200,y=235)
            label = Label(anchor="center",width=20,text="",bg="black",fg="white",font=("Courier",18))
            label.place(x=450,y=200)
            label = Label(anchor="center",text="",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=450,y=250)
            #bring_entry_box()
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=375)
            label = Label(anchor="center",text="Seat Full",width=25,bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=450)
            label = Label(anchor="center",text="Seats available",width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=475)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=500)
            label = Label(anchor="center",text=seats.seats_read,width=20,bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=525)
            
            
            
    def check_seat_availability(self,seat_no):
        for i in seats.seats_booked:
            if(i==seat_no):
                return False
        return True

    
                
# ********************* Functions ****************************************                
                
def bring_entry_box():
    label = Label(text="Enter seat no. to book : ",font=("Calibri",12),bg="black",fg="white")
    label.place(x=150,y=325)
    entry = Entry(textvariable=seats.take)
    entry.place(x=325,y=325)
    submit = Button(text="Submit",command=ticket_assign)
    submit.place(x=500,y=325) 
    
def ticket_assign():
    a=seats.take.get()
    a=int(a)
    t1=ticket()
    t1.book(a)
    
def start():
    global count
    if(count==0):
        count+=1
        a=seats()
        seats.seat_ava_read(seats)
        if(len(seats.seats_booked)<10):
            if(seats.seats_booked==a.seats_booked):
                label = Label(anchor="center",width=25,text="Seat No. already booked",bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=200)
                label = Label(anchor="center",text=a.seats_booked,width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=50,y=250)
                #label = Label(text="Total 10 seats are there",bg="black",fg="white",font=("Courier",20))
                #label.place(x=200,y=235)
                label = Label(anchor="center",width=20,text="Seat No. available",bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=200)
                label = Label(anchor="center",text=a.seats_read,width=20,bg="black",fg="white",font=("Courier",18))
                label.place(x=450,y=250)
                bring_entry_box()
        else:
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
            label = Label(text="                                                                             ",bg="black",fg="white",font=("Courier",18))
            label.place(x=250,y=375)
            label = Label(anchor="center",text="Seat Full",width=25,bg="black",fg="white",font=("Courier",18))
            label.place(x=200,y=425)
    
        

        
# ******************** Main ***********************

# Menu
def welcome():
    mymenu = Menu()
    listone = Menu()
    listone.add_command(label="New")
    listone.add_command(label="Open")
    listone.add_command(label="Save")
    mymenu.add_cascade(label="File",menu=listone)
    root.config(menu=mymenu,background="black")

    # Welcome
    welcome_text = Label(text="Welcome to movie ticket booking",bg="black",fg="white",font=("Courier",24))
    welcome_text.place(x=100,y=50)

    # Buttons
    book_tickets = Button(anchor="center",width=10,text="Book tickets",command=start)
    book_tickets.place(x=300,y=150)
    exit = Button(anchor="center",width=10,text="Exit",command=dest)
    exit.place(x=400,y=150)

def dest():
    root.destroy()

welcome()

root.mainloop()
