# -*- coding: utf-8 -*-

"""
# load and reload it with %reload_ext luri.luri_displaytools for development

based on https://github.com/cknoll/ipydex

"""

import types
#import IPython
#from IPython.display import display


def load_ipython_extension(ip):
    print('xxx1 load ext entry point')

    def new_run_cell(self, raw_cell, *args, **kwargs):
        print('xxx2 override function to run each cell')

        # noinspection PyBroadException
        try:
            new_raw_cell = raw_cell
            pass
            #new_raw_cell = insert_disp_lines(raw_cell)
        except Exception as e:
            #msg = "There was an error in the displaytools extension (probably due to unsupported syntax).\n"
                  #"This is the error message:\n\n{}\n\n"
                  #"We leave this cell unchanged."
            #print(msg.format(e))
            new_raw_cell = raw_cell

        q = 0
        if q:
            # debug
            print("cell:")
            print(raw_cell)
            print("new_cell:")
            print(new_raw_cell)
            print('-'*5)

        return ip.old_run_cell(new_raw_cell, *args, **kwargs)

    # prevent unwanted overwriting when the extension is reloaded
    if 'new_run_cell' not in str(ip.run_cell):
        ip.old_run_cell = ip.run_cell

    ip.run_cell = types.MethodType(new_run_cell, ip) #override here
    ip.user_ns['xxx'] = 999 #display #mess with user namespace
    #ip.user_ns['custom_display'] = custom_display
    #ip.user_ns['_ipydex__info'] = info
    return

 
