# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 10:14:59 2018
Modified on Sat Nov 21 15:15:15 2020

@author: ryan
"""

from datetime import datetime
from psychopy import core, gui, visual, event
from random import shuffle

data = {}
data['Expname'] = 'Go/nogo Test'
#Creat a string version of the current year/month/day hour/minute
data['Expdate'] = datetime.now().strftime('%Y%m%d_%H%M')
data['ParticipantID'] = ''
data['Gender'] = ''

#Set up input dialog
#Use the 'fixed' argument to stop the user changing the 'expname' and 'expdate' parameter
#Use the 'order' argument to set the order in which to display the fields
dlg = gui.DlgFromDict(data, title='Input data', fixed=['Expname','Expdate'],
                      order=['Expname','Expdate','ParticipantID','Gender'])
                    
#if participant quit, scripts end here
if not dlg.OK:
   print("User cancelled the experiment")
   core.quit()

filename = 'part_%s_%s.csv' % (data['ParticipantID'],data['Expdate'])
f = open(filename, 'a+')

#Print the title of data form
f.write('trialID,stimuli,rt,acc\n')

#set experiment window
win = visual.Window([1024,768],fullscr = False, \
                     allowGUI =True, units = "pix", color = (0,0,0))

#set instructions of the experiment
instruction1 = visual.TextStim(win, text = 'If you see M, press SPACE, if see W, do nothing', pos=(0, 88), color = (1,1,1))
instruction2 = visual.TextStim(win, text = 'Press ENTER to start practice', pos=(0, -88), color = (1,1,1))
instruction3 = visual.TextStim(win, text = 'Press ENTER to start experiment', pos=(0, -88), color = (1,1,1))
instruction4 = visual.TextStim(win, text = 'Rest for a while', pos=(0, -88), color = (1,1,1))
instruction5 = visual.TextStim(win, text = 'This is the end of the experiment. Thank you!', pos=(0, -88), color = (1,1,1))

#set fixations and stimuli of the experiment
fix = visual.TextStim(win, text = '+', height=50, pos=(0, 0), color = (1,1,1))

sti = visual.TextStim(win, text = 'B', height=36, pos=(0, 0), color = (1,1,1))

#define a empty list for storing stimulis
sti_list = []                   

#define a function for trial loop
def trial(n_trial):
    #randomize the stimulus list
    shuffle(sti_list)
    for i in range(n_trial):
        core.wait(0.4)
        fix.draw()
        win.flip()
        core.wait(0.5)
        sti.setText(sti_list[i])
        sti.draw()
        displaytime = win.flip()
        core.wait(0.1)
        win.flip()
        core.wait(0.8)
        keys = event.getKeys(keyList=['space'],timeStamped=True)
        
        #calculate rt
        if keys:
            rt = keys[0][1] - displaytime
        else:
            rt = "none"
        
        #calculate accuracy
        if sti_list[i] == "M":
            if not keys:
                acc = "0"
            else:
                acc = "1"
        elif sti_list[i] == "W":
            if not keys:
                acc = "1"
            else:
                acc = "0"
        
        #write into data file
        f.write(str(n_trial) + ',')
        f.write(sti_list[i] + ',')
        f.write(str(rt) + ',')
        f.write(acc + ',')
        f.write('\n')
        
instruction1.draw()
instruction2.draw()
win.flip()         
event.waitKeys(keyList=['return'])
core.wait(1.0)     

#set the practice stimulus list (fixed)
sti_list = ["M","W","M","W","M","W","M","W","M","W","M","W","M","W"]

#practice block
trial(10)

#mark between practice and experiment
f.write('experiment starts below\n')

#ready to run the experiment
win.flip()
instruction3.draw()
win.flip()
event.waitKeys(keyList=['return'])
core.wait(1.0) 

#set the first experiment stimulus list (generate)
sti_list = []
temp = ["M","W","W","W","W"]
for i in range(3):
    sti_list.extend(temp)

#first experiment block begin
trial(15)

#rest
instruction4.draw()
win.flip()
core.wait(5.0)

#second experiment block begin
trial(15)

#the end of the experiment, close the window and exit psychopy core
instruction5.draw()
win.flip()
event.waitKeys()
win.close()
core.quit()