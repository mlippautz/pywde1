#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Researchstudio iSpace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "build","lib"))


from wde1 import WDE1

def sensor_listener(src, event):
    print("=== listener: adr=2, only changes ===")
    print("Sensor Address: " + str(event.adr))
    print("Changed since last receive:" + str(event.changed))
    print("Event type: " + event.event_type)
    print("Timestamp: " + str(event.timestamp))
    print("Temperature: " + str(event.temperature))
    print("Humidity: " + str(event.humidity))
    print("")

w = WDE1("/dev/ttyUSB0")
w.add_observer(sensor_listener, adr=2)
w.start_reading(blocking=True)
