from tkinter import *
from tkinter import ttk

class MainWindow:

    def __init__(self):

        self.root = Tk()

        self.root.geometry('800x500')

        self.root.title('CanSat Project')

        self.background = '#123456'
        
        self.root.config(background = self.background)

        self.main()
        
        self.root.mainloop()

    def main(self):
        self.homeScreenUI()

    def homeScreenUI(self):
 
        self.title = Label(self.root,
                      text = 'CanSat Project',
                      fg = 'White',
                      bg = self.background,
                      font = ('Quicksand',50,'bold'))
        self.title.place(x = 220, y = 35)

        self.connectButton = Button(self.root,
                      text = 'Connect',
                      fg = self.background,
                      width = 16,
                      height = 5,
                      bg = 'Orange',
                      font = ('Quicksand',30,'bold'),
                      command = lambda: self.optionPress('Connect'))
        self.connectButton.place(x = 35, y = 150)

        self.troubleshootButton = Button(self.root,
                      text = 'Troubleshoot',
                      fg = self.background,
                      width = 16,
                      height = 5,
                      bg = 'Red',
                      font = ('Quicksand',30,'bold'),
                      command = lambda: self.optionPress('Troubleshoot'))
        self.troubleshootButton.place(x = 420, y = 150)

        self.playButton = Button(self.root,
                      text = 'Begin',
                      fg = self.background,
                      width = 53,
                      height = 2,
                      bg = 'Green',
                      font = ('Quicksand',20,'bold'),
                      command = lambda: self.optionPress('Begin'))
        self.playButton.place(x = 35, y = 380)

    def optionPress(self, value):
        if value == 'Connect':
            self.connect()
        elif value == 'Troubleshoot':
            self.troubleshoot()
        elif value == 'Begin':
            self.begin()
        else:
            print('Error 1 - Unknown Option')

    def troubleshoot(self):
        print('Troubleshooting...')

    def connect(self):
        print('Connecting...')

    def begin(self):
        print('Beginning...')
        self.root.destroy()
        self.running = Running()
        
        

class Running:
    def __init__(self):
        self.running = Tk()
        self.background = '#654321'
        self.running.geometry('800x500')
        self.running.title('Running')
        self.running.config(background = self.background)
        self.running.mainloop()
  
if __name__ == '__main__':
    application = MainWindow()# sample-code
