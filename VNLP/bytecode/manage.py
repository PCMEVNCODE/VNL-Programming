from libsys.color import BRIGHT_BLUE,RESET
from bytecode.basic import basic
from libsys.sub import filename
import base64, os

def mange(text, line, proc):
    global file
    file = proc
    print(file)
    print(BRIGHT_BLUE + "CONVERT | START" + RESET)
    text.strip()
    
    bytecode(
        "\n".join([
            basic(text, line)
        ])
    )
    
    

def bytecode(code): 
    output_folder = "temp"
    path = os.path.join(output_folder, f"{file}.vnlb")
    os.makedirs(output_folder, exist_ok=True)
    
    # Bước 1: Mã hóa Base64
    base64_encoded = base64.b64encode(code.encode('utf-8'))
    
    # Bước 2: Chuyển thành bit string
    binary_str = ''.join(format(byte, '08b') for byte in base64_encoded)
    
    # Bước 3: Gom lại từng byte (8 bit → byte thực sự)
    bytecode_data = bytearray()
    for i in range(0, len(binary_str), 8):
        byte_segment = binary_str[i:i+8]
        if len(byte_segment) == 8:
            bytecode_data.append(int(byte_segment, 2))

    # Ghi vào file
    with open(path, "ab") as f:
        f.write(bytecode_data + b'\n')

    return path
