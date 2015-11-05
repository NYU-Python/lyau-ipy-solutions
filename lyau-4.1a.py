import time
import os
import sys

class Logger(object):
    priorities = {
        'DEBUG': 1,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4,
        'CRITICAL': 5
    }        
    
    log_line_spacer = '    '
    
    def __init__(self, filename, priority='DEBUG', datetime=True, scriptname=True):
        
        priorities = {
        'DEBUG': 1,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4,
        'CRITICAL': 5
    }  
        self.filename =filename
        if datetime:
            self.write_date = True
        if scriptname:
            self.write_scriptname = True
        try:
            fh = open(self.filename, 'a')
        except IOError:
            raise IOError("Cannot open specified file")
        self.handle = fh
        
        try:
            self.priority = priorities[priority]
        except KeyError:
	    raise KeyError('{0} is not a valid priority level.'.format(priority))
    

    def compose_prepend(self):
        if self.write_date:
            dt = time.ctime()
        if self.write_scriptname:
            f = os.path.basename(sys.argv[0])
        self.prependstr = str(dt)+self.log_line_spacer+str(f)+self.log_line_spacer
        return self.prependstr
        
    def write_log(self, msg, priority):
            self.compose_prepend()
            if self.priorities[priority] >= self.priorities[self.priority]:
                self.handle.write(self.prependstr+msg+'\n')
                    

    def debug(self, msg):
               self.write_log(msg,1)
               

    def info(self, msg):
               self.write_log(msg,2)
               

    def warning(self, msg):
               self.write_log(msg,3)
               
   
    def error(self, msg):
               self.write_log(msg,4)
               
   
    def critical(self, msg):
               self.write_log(msg,5)
