__author__ = 'mesut'

from aktos_dcs import *

ProxyActor(brokers='192.168.1.42:5012:5013')
while True:
    print "sending.."
    Actor().send({'Enzim1': {}})
    sleep(1)
wait_all()