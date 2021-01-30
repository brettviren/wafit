#!/usr/bin/env python3

import os
import sys
import configparser

# so ctx.load("tool") finds our tools
sys.path.append(os.path.dirname(__file__))

class WafIT:
    def __init__(self, cfgfile):
        if not os.path.exists(cfgfile):
            raise ValueError(f'no such file: {cfgfile}')
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(cfgfile)

    @property
    def version(self):
        return self.config['project']['version']

    @property
    def name(self):
        return self.config['project']['name']

    @property
    def options(self):
        def options_f(opt):
            opt.add_option('--prefix-path', action="append",
                           help="Path to search for installed files")
            for tool in self.config["tools"]:
                opt.load(tool)
        return options_f

    @property
    def configure(self):
        def configure_f(cfg):
            for tool in self.config["tools"]:
                cfg.load(tool)
        return configure_f
