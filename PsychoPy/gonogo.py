#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.6),
    on 十一月 21, 2020, at 15:37
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.6'
expName = 'gonogo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\坚果云同步盘\\Ryan的同步文件\\201122Python分享\\Git\\gonogo.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "ins1"
ins1Clock = core.Clock()
ins1_text = visual.TextStim(win=win, name='ins1_text',
    text='If you see M, press SPACE, if see W, do nothing\n\nPress ENTER to start practice',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ins1 = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
fix_text = visual.TextStim(win=win, name='fix_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sti_text = visual.TextStim(win=win, name='sti_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ins2"
ins2Clock = core.Clock()
ins2_text = visual.TextStim(win=win, name='ins2_text',
    text='Press ENTER to start experiment',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_ins2 = keyboard.Keyboard()

# Initialize components for Routine "exp1"
exp1Clock = core.Clock()
fix1_text = visual.TextStim(win=win, name='fix1_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sti1_text = visual.TextStim(win=win, name='sti1_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Rest for a while',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "exp2"
exp2Clock = core.Clock()
fix2_text = visual.TextStim(win=win, name='fix2_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
si2_text = visual.TextStim(win=win, name='si2_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "finish"
finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='This is the end of the experiment.\n\nThank you!',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_finish = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ins1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_ins1.keys = []
key_resp_ins1.rt = []
_key_resp_ins1_allKeys = []
# keep track of which components have finished
ins1Components = [ins1_text, key_resp_ins1]
for thisComponent in ins1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins1"-------
while continueRoutine:
    # get current time
    t = ins1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins1_text* updates
    if ins1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins1_text.frameNStart = frameN  # exact frame index
        ins1_text.tStart = t  # local t and not account for scr refresh
        ins1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins1_text, 'tStartRefresh')  # time at next scr refresh
        ins1_text.setAutoDraw(True)
    
    # *key_resp_ins1* updates
    waitOnFlip = False
    if key_resp_ins1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ins1.frameNStart = frameN  # exact frame index
        key_resp_ins1.tStart = t  # local t and not account for scr refresh
        key_resp_ins1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ins1, 'tStartRefresh')  # time at next scr refresh
        key_resp_ins1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_ins1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_ins1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ins1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ins1.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_ins1_allKeys.extend(theseKeys)
        if len(_key_resp_ins1_allKeys):
            key_resp_ins1.keys = _key_resp_ins1_allKeys[-1].name  # just the last key pressed
            key_resp_ins1.rt = _key_resp_ins1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins1"-------
for thisComponent in ins1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins1_text.started', ins1_text.tStartRefresh)
thisExp.addData('ins1_text.stopped', ins1_text.tStopRefresh)
# the Routine "ins1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_list.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    sti_text.setText(sti)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    practiceComponents = [fix_text, sti_text, key_resp]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_text* updates
        if fix_text.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            fix_text.frameNStart = frameN  # exact frame index
            fix_text.tStart = t  # local t and not account for scr refresh
            fix_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_text, 'tStartRefresh')  # time at next scr refresh
            fix_text.setAutoDraw(True)
        if fix_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix_text.tStop = t  # not accounting for scr refresh
                fix_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_text, 'tStopRefresh')  # time at next scr refresh
                fix_text.setAutoDraw(False)
        
        # *sti_text* updates
        if sti_text.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            sti_text.frameNStart = frameN  # exact frame index
            sti_text.tStart = t  # local t and not account for scr refresh
            sti_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sti_text, 'tStartRefresh')  # time at next scr refresh
            sti_text.setAutoDraw(True)
        if sti_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sti_text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sti_text.tStop = t  # not accounting for scr refresh
                sti_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sti_text, 'tStopRefresh')  # time at next scr refresh
                sti_text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(ans)) or (key_resp.keys == ans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prac_trials.addData('fix_text.started', fix_text.tStartRefresh)
    prac_trials.addData('fix_text.stopped', fix_text.tStopRefresh)
    prac_trials.addData('sti_text.started', sti_text.tStartRefresh)
    prac_trials.addData('sti_text.stopped', sti_text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac_trials (TrialHandler)
    prac_trials.addData('key_resp.keys',key_resp.keys)
    prac_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        prac_trials.addData('key_resp.rt', key_resp.rt)
    prac_trials.addData('key_resp.started', key_resp.tStartRefresh)
    prac_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'prac_trials'


# ------Prepare to start Routine "ins2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_ins2.keys = []
key_resp_ins2.rt = []
_key_resp_ins2_allKeys = []
# keep track of which components have finished
ins2Components = [ins2_text, key_resp_ins2]
for thisComponent in ins2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ins2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ins2"-------
while continueRoutine:
    # get current time
    t = ins2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ins2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins2_text* updates
    if ins2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins2_text.frameNStart = frameN  # exact frame index
        ins2_text.tStart = t  # local t and not account for scr refresh
        ins2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins2_text, 'tStartRefresh')  # time at next scr refresh
        ins2_text.setAutoDraw(True)
    
    # *key_resp_ins2* updates
    waitOnFlip = False
    if key_resp_ins2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_ins2.frameNStart = frameN  # exact frame index
        key_resp_ins2.tStart = t  # local t and not account for scr refresh
        key_resp_ins2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_ins2, 'tStartRefresh')  # time at next scr refresh
        key_resp_ins2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_ins2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_ins2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_ins2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_ins2.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_ins2_allKeys.extend(theseKeys)
        if len(_key_resp_ins2_allKeys):
            key_resp_ins2.keys = _key_resp_ins2_allKeys[-1].name  # just the last key pressed
            key_resp_ins2.rt = _key_resp_ins2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ins2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ins2"-------
for thisComponent in ins2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins2_text.started', ins2_text.tStartRefresh)
thisExp.addData('ins2_text.stopped', ins2_text.tStopRefresh)
# the Routine "ins2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
exp1_trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_list.xlsx'),
    seed=None, name='exp1_trials')
thisExp.addLoop(exp1_trials)  # add the loop to the experiment
thisExp1_trial = exp1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp1_trial.rgb)
if thisExp1_trial != None:
    for paramName in thisExp1_trial:
        exec('{} = thisExp1_trial[paramName]'.format(paramName))

for thisExp1_trial in exp1_trials:
    currentLoop = exp1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExp1_trial.rgb)
    if thisExp1_trial != None:
        for paramName in thisExp1_trial:
            exec('{} = thisExp1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "exp1"-------
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    sti1_text.setText(sti)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    exp1Components = [fix1_text, sti1_text, key_resp_2]
    for thisComponent in exp1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    exp1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "exp1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = exp1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=exp1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1_text* updates
        if fix1_text.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            fix1_text.frameNStart = frameN  # exact frame index
            fix1_text.tStart = t  # local t and not account for scr refresh
            fix1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1_text, 'tStartRefresh')  # time at next scr refresh
            fix1_text.setAutoDraw(True)
        if fix1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix1_text.tStop = t  # not accounting for scr refresh
                fix1_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix1_text, 'tStopRefresh')  # time at next scr refresh
                fix1_text.setAutoDraw(False)
        
        # *sti1_text* updates
        if sti1_text.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            sti1_text.frameNStart = frameN  # exact frame index
            sti1_text.tStart = t  # local t and not account for scr refresh
            sti1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sti1_text, 'tStartRefresh')  # time at next scr refresh
            sti1_text.setAutoDraw(True)
        if sti1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sti1_text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sti1_text.tStop = t  # not accounting for scr refresh
                sti1_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sti1_text, 'tStopRefresh')  # time at next scr refresh
                sti1_text.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exp1"-------
    for thisComponent in exp1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp1_trials.addData('fix1_text.started', fix1_text.tStartRefresh)
    exp1_trials.addData('fix1_text.stopped', fix1_text.tStopRefresh)
    exp1_trials.addData('sti1_text.started', sti1_text.tStartRefresh)
    exp1_trials.addData('sti1_text.stopped', sti1_text.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for exp1_trials (TrialHandler)
    exp1_trials.addData('key_resp_2.keys',key_resp_2.keys)
    exp1_trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        exp1_trials.addData('key_resp_2.rt', key_resp_2.rt)
    exp1_trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    exp1_trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'exp1_trials'


# ------Prepare to start Routine "rest"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = [rest_text]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_text* updates
    if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_text.frameNStart = frameN  # exact frame index
        rest_text.tStart = t  # local t and not account for scr refresh
        rest_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
        rest_text.setAutoDraw(True)
    if rest_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_text.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            rest_text.tStop = t  # not accounting for scr refresh
            rest_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rest_text.started', rest_text.tStartRefresh)
thisExp.addData('rest_text.stopped', rest_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
exp2_trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_list.xlsx'),
    seed=None, name='exp2_trials')
thisExp.addLoop(exp2_trials)  # add the loop to the experiment
thisExp2_trial = exp2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp2_trial.rgb)
if thisExp2_trial != None:
    for paramName in thisExp2_trial:
        exec('{} = thisExp2_trial[paramName]'.format(paramName))

for thisExp2_trial in exp2_trials:
    currentLoop = exp2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExp2_trial.rgb)
    if thisExp2_trial != None:
        for paramName in thisExp2_trial:
            exec('{} = thisExp2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "exp2"-------
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    si2_text.setText(sti)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    exp2Components = [fix2_text, si2_text, key_resp_3]
    for thisComponent in exp2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    exp2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "exp2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = exp2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=exp2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix2_text* updates
        if fix2_text.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
            # keep track of start time/frame for later
            fix2_text.frameNStart = frameN  # exact frame index
            fix2_text.tStart = t  # local t and not account for scr refresh
            fix2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2_text, 'tStartRefresh')  # time at next scr refresh
            fix2_text.setAutoDraw(True)
        if fix2_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix2_text.tStop = t  # not accounting for scr refresh
                fix2_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2_text, 'tStopRefresh')  # time at next scr refresh
                fix2_text.setAutoDraw(False)
        
        # *si2_text* updates
        if si2_text.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
            # keep track of start time/frame for later
            si2_text.frameNStart = frameN  # exact frame index
            si2_text.tStart = t  # local t and not account for scr refresh
            si2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(si2_text, 'tStartRefresh')  # time at next scr refresh
            si2_text.setAutoDraw(True)
        if si2_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > si2_text.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                si2_text.tStop = t  # not accounting for scr refresh
                si2_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(si2_text, 'tStopRefresh')  # time at next scr refresh
                si2_text.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # was this correct?
                if (key_resp_3.keys == str(ans)) or (key_resp_3.keys == ans):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exp2"-------
    for thisComponent in exp2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp2_trials.addData('fix2_text.started', fix2_text.tStartRefresh)
    exp2_trials.addData('fix2_text.stopped', fix2_text.tStopRefresh)
    exp2_trials.addData('si2_text.started', si2_text.tStartRefresh)
    exp2_trials.addData('si2_text.stopped', si2_text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for exp2_trials (TrialHandler)
    exp2_trials.addData('key_resp_3.keys',key_resp_3.keys)
    exp2_trials.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        exp2_trials.addData('key_resp_3.rt', key_resp_3.rt)
    exp2_trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    exp2_trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'exp2_trials'


# ------Prepare to start Routine "finish"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_finish.keys = []
key_resp_finish.rt = []
_key_resp_finish_allKeys = []
# keep track of which components have finished
finishComponents = [finish_text, key_resp_finish]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    
    # *key_resp_finish* updates
    waitOnFlip = False
    if key_resp_finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_finish.frameNStart = frameN  # exact frame index
        key_resp_finish.tStart = t  # local t and not account for scr refresh
        key_resp_finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_finish, 'tStartRefresh')  # time at next scr refresh
        key_resp_finish.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_finish.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_finish.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_finish.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_finish.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'return'], waitRelease=False)
        _key_resp_finish_allKeys.extend(theseKeys)
        if len(_key_resp_finish_allKeys):
            key_resp_finish.keys = _key_resp_finish_allKeys[-1].name  # just the last key pressed
            key_resp_finish.rt = _key_resp_finish_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finish_text.started', finish_text.tStartRefresh)
thisExp.addData('finish_text.stopped', finish_text.tStopRefresh)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
