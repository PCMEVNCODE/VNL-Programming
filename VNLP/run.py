#### MAIN PROGRAMMING VNL
import os
import sys
from bytecode.manage import mange
from isys.sysw import welsys
from isys.info import system_info, develop
from libsys.color import BRIGHT_BLUE,BRIGHT_YELLOW,BRIGHT_RED, RESET
from libsys.delfilesys import clear_temp_folder
from libsys.sub import filename

def vnl():
    print(BRIGHT_BLUE + welsys + RESET)
    
def proc_cmd(cmd):
    content = cmd.strip()
    # Process command 
    if content.startswith('vnl '):
        global proc, filename
        proc = content[4:]
        try:
            with open(proc, "r", encoding="utf-8") as f:
                for text, line in enumerate(f, 1):
                    mange(line, text, proc)
        except FileNotFoundError:
            print(BRIGHT_RED + f"[ERROPEN] => No such file or dictory {proc}" + RESET)
    elif content == "show -inf":  
        print(BRIGHT_BLUE + welsys + RESET)
    elif content == "info -s":
        print(system_info)
    elif content == "info -t":
        print(develop)
    elif content == "out" \
        or content == "quit" \
            or content == "exit":
                sys.exit(0)
            
    else:
        if content == "":
            return
        else:
            print(BRIGHT_RED + f"[ERRCMD] => '{content}' is not a system command." + RESET)
        
    
if __name__ == "__main__":

    clear_temp_folder("temp") # Clear all file in temp
    vnl()
    try:
        while True:
            try:
                cmd = input(BRIGHT_YELLOW + ">>>" + RESET)
                proc_cmd(cmd)
            except (EOFError, KeyboardInterrupt):
                print(BRIGHT_RED + f"[ERRSYSTEM] => Error: EOF or KeyboardInterrupt" + RESET)
    finally:
        try:
            try:
                os.remove(f"temp/{proc}.vnlc")
            except NameError:
                pass
        except FileNotFoundError or FileExistsError:
            print(BRIGHT_RED + f"[ERRSYSTEM] => Do not found file {proc}.vnlc in temp. (ERRCODE: VNLER02)")