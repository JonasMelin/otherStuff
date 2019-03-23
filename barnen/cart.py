#####################################################
# IMPORTS
#####################################################
import gym
from time import sleep
import threading
from pynput.keyboard import Key, Listener

env = gym.make('CartPole-v0')
env.reset()

#####################################################
# GLOBAL VARIABLES
#####################################################
ACTION = 0

#####################################################
# on press.
#####################################################
def on_press(key):

    global ACTION
    global ABORT

    if key == Key.left:
        ACTION = 0
    if key == Key.right:
        ACTION = 1
    if key == Key.esc:
        ABORT = True

#####################################################
# keyboard thread..
#####################################################
def keyboardThread():
    with Listener(on_press=on_press) as listener:
        listener.join()

t = threading.Thread(target=keyboardThread)
t.start()


#####################################################
# MAIN!
#####################################################
while True:
    env.render()
    observation, reward, done, info = env.step(ACTION)

    print(observation)

    if(done):
        env.reset()

    sleep(0.1)

env.close()


    #Num Observation             Min         Max
    #0   Cart Position           -2.4        2.4
    #1   Cart Velocity           -Inf        Inf
    #2   Pole Angle              ~ -41.8°    ~ 41.8°
    #3   Pole Velocity At Tip    -Inf        Inf
