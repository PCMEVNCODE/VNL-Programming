import os
from libsys.color import BRIGHT_RED, RESET
## Void clear file in temp
def clear_temp_folder(folder): ## call: clear_temp_folder("<name folder>")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(BRIGHT_RED + f"[ERROPEN] => Error to delete {file_path} (ERRCODE: VNLER03)" + RESET)