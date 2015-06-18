#!/usr/bin/env python

import os
import yaml
#from wizard import BASE_DIR

homedir = '~/.archivecd/'
#homedir = '~'
configfile= 'archivecd.yml'
thepath= ''

# read()
#_________________________________________________________________________________________
def read((base_dir)):
    global homedir
    try:
        homedir= os.path.expanduser(homedir)
        thepath= os.path.join(homedir,configfile)
        if not os.path.exists(thepath):
            if os.path.exists(os.path.join(base_dir,configfile)):
                thepath= os.path.join(base_dir,configfile)
        f = open(thepath)
        config = yaml.safe_load(f)
    except Exception:
        print('Could not read {p}'.format(p=os.path.join(thepath,configfile)))
        config = {}
    return config


# save()
#_________________________________________________________________________________________
def save(config):
    try:
        f = open(thepath, 'w')
        yaml.dump(config, f, default_flow_style=False)
        print yaml.dump(config, default_flow_style=False)
    except Exception:
        #raise ScribeException('Could not save config to {p}'.format(p=path))
        print('Could not save config to {p}'.format(p=thepath))

