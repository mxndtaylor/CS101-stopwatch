# Source: http://www.codeskulptor.org/#user48_b0mAQacYpS_8.py
# Submission for "Stopwatch: The Game"

import simplegui
import math

# define global variables
ELAPSED = 0
STOPS = 0
GOOD_STOPS = 0
HIGH_SCORE = 0
HIGH_STREAK = 0
HIGH_TIME = 0
LONGEST_TIME = 0
LONGEST_SCORE = 0
STREAK = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # tenths is the first digit, mod by 10 to get that
    tenths = str(t % 10)
    
    # seconds are the number
    seconds = str((t/10) % 60)
    minutes = str(t // 600)
    if len(seconds) < 2:
        seconds = "0" + seconds
    return minutes + ":" + seconds + "." + tenths
        
# calculates the score as per the mini-project video
def calc_score():
    return 4 * GOOD_STOPS - STOPS

# updates all records
def update_bests():
    update_high_score()
    update_streak()
    update_longest_game()

# updates the stored high score, prioritizing
#	quicker scores to break ties 
def update_high_score():
    global HIGH_SCORE, HIGH_TIME
    score = calc_score()
    
    # highest score is always displayed
    # in the case of tie, the lower time is displayed
    if ((HIGH_SCORE == score and ELAPSED < HIGH_TIME)
            or (HIGH_SCORE < score)):
        HIGH_SCORE = score
        HIGH_TIME = ELAPSED

# updates the stored best streak
def update_streak():
    global HIGH_STREAK
    if (STREAK > HIGH_STREAK):
        HIGH_STREAK = STREAK
    
# updates and records the longest game
def update_longest_game():
    global LONGEST_TIME, LONGEST_SCORE
    if LONGEST_TIME < ELAPSED:
        LONGEST_TIME = ELAPSED
        LONGEST_SCORE = calc_score()
    
# starts the timer
def start():
    TIMER.start()

# stops the timer
def stop():
    global STOPS, GOOD_STOPS, SCORE, STREAK
    if TIMER.is_running():
        TIMER.stop()
        STOPS += 1
        if ELAPSED % 10 == 0:
            GOOD_STOPS += 1
            STREAK += 1
        else:
            STREAK = 0
    update_bests()
            

# resets the timer and the score, updates the scoreboard
def reset():
    global ELAPSED, STOPS, GOOD_STOPS
    stop()
    ELAPSED = 0
    STOPS = 0
    GOOD_STOPS = 0
    STREAK = 0

# define event handler for timer with 0.1 sec interval
def watch():
    global ELAPSED
    ELAPSED += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(ELAPSED), [30, 80], 48, "White")
    canvas.draw_text(str(GOOD_STOPS) + "/" + str(STOPS),
                        [140, 30], 24, "Green")
    canvas.draw_text("Bests:", 
                        [10, 100], 15, "Yellow")
    canvas.draw_text("Streak: " + str(HIGH_STREAK),
                        [20, 112], 12, "Yellow")
    canvas.draw_text("Score: " + str(HIGH_SCORE) 
                        + "pts in " + format(HIGH_TIME),
                        [20, 124], 12, "Yellow")
    canvas.draw_text("Time: " 
                        + format(LONGEST_TIME) + " with " 
                        + str(LONGEST_SCORE) + "pts",
                        [20, 136], 12, "Yellow")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",180,140)

# register event handlers
TIMER = simplegui.create_timer(100, watch)
START = frame.add_button("Start", start, 100)
STOP = frame.add_button("Stop", stop, 100)
RESET = frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()
