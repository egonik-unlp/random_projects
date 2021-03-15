#!/usr/bin/env python
# -*- coding: utf-8 -*-


def walker():
    for root, dirs, files in os.walk(".", topdown=False):
        print('root', root)
        print('dirs', dirs)
        print('files', files)
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))