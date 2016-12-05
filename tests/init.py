import os, sys
#load common module 
#setting priority
#lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
#sys.path.insert(0, lib_path)
lib_path = os.path.abspath(os.path.join('..', 'app'))
sys.path.append(lib_path)

from util.path import get_current_path
#print(sys.path)
print(get_current_path())
