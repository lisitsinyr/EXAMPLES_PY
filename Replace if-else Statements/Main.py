"""TEST_LUos.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     Main.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import LULog
import LUConst
from LUDoc import *
import LUos

urlParsed_netloc = ''

def default_handler(parsed_url):
    pass
def youtube_handler(parsed_url):
    pass
def hulu_handler(parsed_url):
    pass
handlers = {
    'www.youtube.com': youtube_handler,
    'hulu.com':        hulu_handler,
}

def urlParsed(parsed_url):
    pass

def TEST_01 ():
    """TEST_01"""
#beginfunction
    PrintInfoObject('---------TEST_01----------')
    PrintInfoObject(TEST_01)

    handler = handlers.get(urlParsed_netloc, default_handler)
    handler(urlParsed)

#endfunction

#------------------------------------------
def main ():
#beginfunction
    TEST_01 ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule

