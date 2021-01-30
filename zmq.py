#!/usr/bin/env waf
'''
This is a wafit tool for using ZeroMQ libzmq
'''
import util

def options(opt):
    util.generic_options(opt, "zmq")

def configure(cfg):
    util.generic_configure_incs(cfg, "zmq", ["zmq.h"])
    util.generic_configure_libs(cfg, "zmq", ["zmq"])    
    

