from tkinter import *
from tkinter import ttk

class ConnectWindow:

    def __init__(self):

        self.root = Tk()

        self.root.geometry('800x500')

        self.root.title('Connection Status')

        self.background = '#142536'
        
        self.root.config(background = self.background)

        self.main()
        
        self.root.mainloop()

    def main(self):
        self.sensors = [('Wind Sens.','Rev.C',True),('Humidity, Pressure & Temp Sens.', 'BME280',True),('Air Quality Sens.','CCS811',False),('CO & Gas Sens.','MiCS5524',False)]
        self.statusUI()

    def statusUI(self):
 
        self.title = Label(self.root,
                      text = 'Connection Status',
                      fg = 'White',
                      bg = self.background,
                      font = ('Quicksand',50,'bold'))
        self.title.place(x = 170, y = 35)

        self.linkText = Label(self.root,
                      text = 'Linked to CanSat',
                      fg = 'White',
                      bg = self.background,
                      font = ('Quicksand',30,'normal'))
        self.linkText.place(x = 50, y = 150)

        self.linkStatus = Label(self.root,
                      text = '✅',
                      fg = 'Green',
                      bg = self.background,
                      font = ('Quicksand',30,'normal'))
        self.linkStatus.place(x = 700, y = 150)

        self.sensorTextOnes = []
        self.sensorTextTwos = []
        self.sensorStatuses = []

        for i, sensor in enumerate(self.sensors):
            self.sensorTextOnes.append(Label(self.root,
                      text = sensor[0],
                      fg = 'White',
                      bg = self.background,
                      font = ('Quicksand',30,'normal')))
            self.sensorTextTwos.append(Label(self.root,
                      text = sensor[1],
                      fg = 'White',
                      bg = self.background,
                      font = ('Quicksand',30,'normal')))
            self.sensorStatuses.append(Label(self.root,
                      text = '✅' if sensor[2] else '🔄',
                      fg = 'Orange',
                      bg = self.background,
                      font = ('Quicksand',30,'normal')))
            
            gap = 60

            self.sensorTextOnes[-1].place(x = 50, y = 150 + (i+1)*gap)
            self.sensorTextTwos[-1].place(x = 535, y = 150 + (i+1)*gap)
            self.sensorStatuses[-1].place(x = 700, y = 150 + (i+1)*gap)

if __name__ == '__main__':
    application = ConnectWindow()
 