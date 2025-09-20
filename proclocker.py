import psutil
import sys
#for proc in psutil.process_iter():
#    print(proc.name(), proc.pid)

#for proc in psutil.process_iter():
#    if proc.name()=='chrome.exe':
#        print('Chrome Detectado')
        
#for proc in psutil.process_iter():
#    if proc.name().lower()=='chrome.exe':
#        print('Chrome Detectado')
def check_arguments():
    if len(sys.argv)==1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)

#target = sys.argv[1]
def get_targets():
    targets = sys.argv[1:]

    i=0
    while i < len(targets):
        if not targets[i].endswith('.exe'):
            targets[i]=targets[i]+'.exe'
        i += 1
    
    return targets

def lock(target):
    for proc in psutil.process_iter():
        if proc.name().lower()==target.lower():
            proc.kill()
            print(f'{target} Detenido')
#           print(f'{target} Detectado')
        
if __name__=='__main__':
    check_arguments()
    targets=sys.argv[1:]
    
    while True:
        for target in targets:
            lock(target)


