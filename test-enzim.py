#!/usr/bin/python
#coding: utf-8

__author__ = 'mesutevin'

from aktos_dcs import *


ProxyActor(brokers='192.168.1.42:5012:5013')

Actor().send({'S':{}})

wait_all()