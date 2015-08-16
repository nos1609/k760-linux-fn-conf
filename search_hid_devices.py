#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import glob

def all_hid_devices():
    return glob.glob('/sys/class/hidraw/hidraw*/device/uevent')

def read_hid_name(uevent_file):
    with open(uevent_file, 'r') as uevent:
        return next(u.strip().replace('HID_NAME=', '') for u in uevent.readlines() if u.startswith('HID_NAME='))

def get_device_map():
    devices = {}
    for dev_file in all_hid_devices():
        dev_path = '/dev/' + dev_file.replace('/sys/class/hidraw/', '').split('/')[0]
        dev_name = read_hid_name(dev_file)
        devices[dev_path] = dev_name
    return devices

if __name__ == '__main__':
    for path, name in get_device_map().iteritems():
        print('{0}: {1}'.format(path, name))
