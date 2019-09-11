import os
from tasks.tools import identifyImg
from time import sleep


# type :reset,shutdown,sleep
def shutdown_computer(type):
    print("开始执行休眠/重启/关机")
    sleep(1)
    identifyImg.wait_for_a_moment_and_click_template("start_button.png",3,0.8)
    sleep(1)
    identifyImg.wait_for_a_moment_and_click_template("shutdown.png",3,0.8)
    sleep(1)
    if type == "reset":
        identifyImg.wait_for_a_moment_and_click_template("reset.png",3,0.8)
    elif type == "shutdown":
        identifyImg.wait_for_a_moment_and_click_template("shutdown.png",3,0.8)
    else:
        identifyImg.wait_for_a_moment_and_click_template("sleep.png",3,0.8)
