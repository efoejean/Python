# EfoeExam 3

import tkinter

import tkinter.messagebox

class TipGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create four frames
        self.subtotal_frame = tkinter.Frame(self.main_window)
        self.percent_frame = tkinter.Frame(self.main_window)
        self.tip_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the subtotal frame
        self.subtotal_label = tkinter.Label \
                             (self.subtotal_frame, \
                              text = 'Enter the amount of the ticket:')
        self.subtotal_entry = tkinter.Entry(self.subtotal_frame, width = 10)

        # Pack the subtotal frame widgets
        self.subtotal_label.pack(side = 'left')
        self.subtotal_entry.pack(side = 'left')

        # Create the widgets for the  percent frame
        self.percent_label = tkinter.Label \
                           (self.percent_frame, \
                            text = 'Enter the tip as a percentage :')
        self.percent_entry = tkinter.Entry(self.percent_frame, width = 10)                                 

        # Pack the  percent frame widgets
        self.percent_label.pack(side ='left')
        self.percent_entry.pack(side = 'left')
        
        # Create the widgets for the tip frame
        self.result_label = tkinter.Label(self.tip_frame, \
                             text = 'Tip Amount: $')
        
        # Create a blank label 
        self.tip = tkinter.StringVar()
        self.tip_label = tkinter.Label(self.tip_frame, \
                                       textvariable= self.tip)
        # Pack the tip frame widgets
        self.result_label.pack(side = 'left')
        self.tip_label.pack(side = 'left')
        
        # Create the widgets for the total frame
        self.result_label = tkinter.Label \
                            (self.total_frame, \
                             text = 'Total Amount: $')
        
        # Create a blank label total
        self.total = tkinter.StringVar()
        self.total_label = tkinter.Label(self.total_frame, \
                                       textvariable= self.total)
        # Pack the total frame widgets
        self.result_label.pack(side = 'left')
        self.total_label.pack(side = 'left')

    
                                                           
        # Create the two buttons in the bottom frame
        self.total_button = tkinter.Button \
                          (self.bottom_frame, \
                           text = 'Calculate', \
                           command = self.calculate_total)
        self.exit_button = tkinter.Button \
                           (self.bottom_frame, \
                            text = 'Exit', \
                            command = self.main_window.destroy)
              
        # Pack the widgets in the bottom frame
        self.total_button.pack(side='left')
        self.exit_button.pack(side='left')
                
        # Pack the frames
        self.subtotal_frame.pack()
        self.percent_frame.pack()
        self.tip_frame.pack()
        self.total_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def calculate_total(self):
        # Get the values entered
        self.subtotal = float(self.subtotal_entry.get())
        if self.subtotal <= 0:
            tkinter.messagebox.showwarning('Wrong input!'+
                                           ' Amount must be '
                               + 'greater than zero')
            self.tip.set("")
            self.total.set("")


            
        self.percent = float(self.percent_entry.get().strip('%'))
   
        if self.percent <= 0:
            tkinter.messagebox.showwarning('Wrong input! Percentage must be '
                               + 'greater than zero')
            
            self.tip.set("")
            self.total.set("")


            

        # Calculate tip
        self.tip_per_amount = float(self.subtotal) * float(self.percent) / 100

        # Update the tip_label
        self.tip.set(format(self.tip_per_amount,',.2f'))

        #Calculate total amount
        self.total_per_amount = float(self.subtotal) + float(self.tip_per_amount)

        # Update the tip_label
        self.total.set(format(self.total_per_amount,',.2f'))

# Create an instance of TipGUI
total = TipGUI()


