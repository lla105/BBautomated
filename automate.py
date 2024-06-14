import time
import subprocess



# Your device ID
device_id = "MO23020902000022"

# class ButtonCoordinates:
#     def __init__(self):
#         self.backbutton = (81,660)
#         self.startbutton = (769, 1556)


class ButtonPresser:
    def __init__(self, device_id, coordinates):
        self.device_id = device_id
        self.coordinates = coordinates
    def tap(self, device_id, x, y):
        # print('  tap : ', x, y)
        cmd = f"adb -s {self.device_id} shell input tap {x} {y}"
        subprocess.run(cmd, shell=True)
    def press(self, button_name):
        x,y = self.coordinates[button_name]
        self.tap(device_id, x,y)

# Number of cycles to repeat
num_cycles = 10


coordinates = {'backbutton' : (81,660), 
               'startbutton': (769, 1556),
               'quickstart' : (810, 1800),
               'english' : (290 , 1150),
               'deposit' : (270, 1024),
               'collect' : (530, 1355),
               'fedex' : (604, 1400),
               'canadapost' : (850,1430),
               'DHL' : (850, 1125),
               'unit#' : (542, 1074),
               '1' : (125,1485),
               '2' : (379, 1500),
               '3' : (616, 1500),
               '5' : (365, 1515),
               '0' : (375, 1849),
               'selectbuilding' : (151,1040),
               'selectunit' : (237,1140),
               'enter' : (897, 1784),
               'small' : (158, 1087),
               'medium' : (760,1070),
               'large' : (140, 1310),
               'confirm': (520, 1747),
               'backtohomescreen' : (320,1675)
               }

# coordinates = ButtonCoordinates()
presser  = ButtonPresser(device_id, coordinates)

depositUnit101 = ['english', 'deposit', 'fedex', 'unit#', '1','0','1', 'selectunit', 'enter','small', 'medium', 'large','confirm']
depositUnit102 = ['english', 'deposit', 'fedex', 'unit#', '1','0','2', 'selectunit', 'enter','small', 'medium', 'large','confirm']
depositUnit105 = ['english', 'deposit', 'fedex', 'unit#', '1','0','5', 'selectunit', 'enter','small', 'medium', 'large','confirm']

roundcount = 0
presser.press('startbutton')
for cycle in range(num_cycles):
    roundcount += 1
    print("======= Round ", roundcount, "/", num_cycles, " ========")
    time.sleep(1.5)
    for command in depositUnit101:
        presser.press(command)
        time.sleep(1.5)
    print(' Finished depositing 101')
    time.sleep(2)
    presser.press('backtohomescreen')
    time.sleep(1.5)
    for command in depositUnit102:
        presser.press(command)
        time.sleep(1.5)
    print(' Finished depositing 102')
    time.sleep(2)
    presser.press('backtohomescreen')
    time.sleep(1.5)
    for command in depositUnit105:
        presser.press(command)
        time.sleep(1.5)
    print(' Finished depositing 105')
    time.sleep(2)
    presser.press('backtohomescreen')
    

print("Automation completed.")
