import os, base64
from pystyle import Colorate, Colors

def desobfuscate(content):
    clean_content = (content[:content.rfind('\n')]).replace('__NO_NO',"").replace('"',"").replace("+=","")
    code = base64.b64decode(bytes((clean_content[2:]).replace("\n","").replace(' ',''), 'utf-8').decode('unicode-escape').encode('utf-8')).decode("utf-8")
    return code

def main():
    banner = Colorate.Horizontal(Colors.cyan_to_green,"""
    ███████ ██ ███    ███ ██████  ██      ███████ 
    ██      ██ ████  ████ ██   ██ ██      ██      
    ███████ ██ ██ ████ ██ ██████  ██      █████   
         ██ ██ ██  ██  ██ ██      ██      ██      
    ███████ ██ ██      ██ ██      ███████ ███████ 
                desobfuscator                                 
    """)
    print(banner)
    try:
        path = argv[1]
    except:
        path = input(Colors.cyan+"Drag your file here and press enter : "+ Colors.reset)
    if not os.path.exists(path):
        print(Colors.red+'[-] File not found'+ Colors.reset)
        exit()
    if not os.path.isfile(path) or not path.endswith('.py'):
        print(Colors.red+'[-] Invalid file'+ Colors.reset)
        exit()
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        file_content = file.read()
    obfuscated_content = desobfuscate(file_content)

    with open(f'{path.split(".")[0]}_desobfuscated.py', 'w') as file:
        file.write(obfuscated_content)

        print(Colors.green+'[+] Script has been desobfuscated'+ Colors.reset)

if __name__ == '__main__':
    main()