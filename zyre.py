#!/usr/bin/env waf
'''
This is a wafit tool for using zyre
'''
import util

def options(opt):
    opt.load("czmq")    
    util.generic_options(opt, "cppzmq", libs=False)
    

def configure(cfg):
    cfg.load("czmq")
    util.generic_configure_incs(cfg, "czmq", "czmq.h")
    util.generic_configure_libs(cfg, "czmq", "czmq")

