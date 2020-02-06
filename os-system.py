import os

sysName = os.name

if sysName == 'nt':
    print ('Windows OS')
    
elif sysName == 'posix':
    print ('Xnix OS')
    
else:
    print ('Operating system not supported')
