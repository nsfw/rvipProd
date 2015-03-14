#!/usr/bin/env python -i 
###############################################################################
# lightGate - an http / osc gateway for making lights blink
###############################################################################
"""
Acts as a web / osc gateway
"""
import CCore
from appscript import *
from subprocess import *

import pdb

def ccoreDump(msg):
    # dump a CommuniCore message to stdout and remember the last value we saw
    # in an in memory database
    print "path: %s %s %s from: %s" % ( msg.path, type(msg.data), msg.data, msg.source )

def dispatch(msg):
    # ccoreDump(msg)
    pass

###############################################################################
# OSC Message Handlers
###############################################################################

# OSC Senders 

# same format as OOCP
def sendKey(keyname, state):
    # send the osc message [keyname, state], where 1 is PRESSED 
    print "key = %s %s" % (keyname, state)
    if state == "press":
        val = 1
    else:
        val = 0
    panel.send("/oocp", [keyname, val])

def sendMsg(path, data):
    panel.send(path, data)

###############################################################################
# Webserver - bottle!
###############################################################################
import bottle
from bottle import route, run, static_file, redirect, template, HTTPResponse
from simplejson import dumps as json_dumps
import time

@route('/')
@route('/index.html')
@route('/lights')
def index():
    return static_file('lights.html','./views')

@route('/jquery-1.9.1.js')
def jquery():
    return static_file('jquery-1.9.1.js','./views')

@route('/jq')
def jquery():
    return static_file('jquery-1.9.1.js','./views')

@route('/media/lights.jpg')
def kirk_logo_gif():
    return static_file('lights.jpg','./views/media')

@route('/css/app.css')
def app_css():
    return static_file('app.css','./views/css')

###############################################################################
## SendScreen Control
###############################################################################

# Sendscreen Presets
# May be better to put this in web-page
presets = [
    ["Video",67,100,6],
    ["Game",0,0,8]
    ]

@route('/sendscreen/preset/<preset>')
def sendPreset (preset):
    p = presets[int(preset)]
    print p
    sendScreen.send("/pos",p[1:3])
    sendScreen.send("/displayMag",p[3:4])

@route('/sendscreen/send/<path>/<data>')
def sendToSendScreen(path,data):
    print "path: "+path
    print "data: "+data
    d = list(eval(data))
    sendScreen.send("/"+path, d)

###############################################################################
## Entry
###############################################################################

# should be false in "production", true disables template caching
# bottle.debug(debugFlag)
bottle.debug(True)

panel = CCore.CCore(pubsub="osc-udp:")	# use default bidirectional multicast
panel.subscribe("*", dispatch)

sendScreen = False;

# if we're running on the RVIP, then use our IP address otherwise, we use
# localhost for easier debuging

ifconfig = Popen(['ifconfig'], stdout = PIPE).communicate()[0]

if ifconfig.find("192.168.1.11") > 0:
    # running on RVIP
    sendScreen = CCore.CCore(pub="osc-udp://192.168.1.22:9998")
    run(host='192.168.1.11', port=8181, server="paste")
else:
    # development
    sendScreen = CCore.CCore(pub="osc-udp://localhost:9998")
    call(['say',"Light Gate In Development Mode"])
    run(host='localhost', port=8182, server="paste")

while True:
    time.sleep(1.0)

