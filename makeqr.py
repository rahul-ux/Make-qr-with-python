# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:36:53 2020

@author: Kapil Kumar
"""

import qrcode

data = "hello world"

qr = qrcode.make(data)

qr.save("web.png")
