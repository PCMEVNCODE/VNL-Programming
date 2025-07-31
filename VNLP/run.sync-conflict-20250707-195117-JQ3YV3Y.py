#### MAIN PROGRAMMING VNL
import os
from isys.sysw import welsys
from isys.info import system_info, develop
from bytecode.manage import mange, filename
from libsys.color import BRIGHT_BLUE,BRIGHT_YELLOW,BRIGHT_RED, RESET
def vnl():
    print(BRIGHT_BLUE + welsys + RESET)
    
def proc_cmd(cmd):
    content = cmd.strip()
    # Process command 
    if content.startswith('vnl '):
        global proc, filename
        proc = content[4:]
        filename = proc
        try:
            with open(proc, "r", encoding="utf-8") as f:
                for text, line in enumerate(f, 1):
                    mange(line, text)
        except FileNotFoundError:
            print(BRIGHT_RED + f"No such file or dictory {proc}" + RESET)
    elif content == "show -inf":
        print(BRIGHT_BLUE + welsys + RESET)
    elif content == "info -s":
        print(system_info)
    elif content == "info -t":
        print(develop)
    else:
        if content == "":
            return
        else:
            print(BRIGHT_RED + f"'{content}' is not a system command." + RESET)
        
    
if __name__ == "__main__":
    vnl()
    try:
        while True:
            cmd = input(BRIGHT_YELLOW + ">>>" + RESET)
            proc_cmd(cmd)
    finally:
        try:
            os.remove(f"temp/{proc}.vnlc")
        except FileNotFoundError or FileExistsError:
            print(BRIGHT_RED + f"ERRSYSTEM: Do not found file {proc}.vnlc in temp.")