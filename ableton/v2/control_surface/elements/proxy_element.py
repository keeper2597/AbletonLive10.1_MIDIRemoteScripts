# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/proxy_element.py
# Compiled at: 2019-04-09 19:23:45
from __future__ import absolute_import, print_function, unicode_literals
from ...base import Proxy
from ..control_element import ControlElement

class ProxyElement(Proxy, ControlElement):

    def reset(self):
        try:
            super(ProxyElement, self).__getattr__('reset')()
        except AttributeError:
            pass