# Metro
Metro transit bus arrival tracker written in Python3
This program was written on Ubuntu 16.04 and also includes a reference to the python library 'references', which you may have to install separately

##Running the main program

From bash shell:
args="'BUS ROUTE' 'BUS STOP NAME' 'DIRECTION'"
python3 nextbus.py $args
e.g.
args="'Express - Target - Hwy 252 and 73rd Av P&R - Mpls' 'Target North Campus Building F' 'south'"
python3 testnextbus.py $args

From python:
import nextbus
nextbus.main('BUS ROUTE', 'BUS STOP NAME', 'DIRECTION'
e.g.
route_name = 'METRO Blue Line'
stop_name = 'Target Field Station Platform 1'
direction_name = 'south'
nextbus.main(route\_name, stop\_name, direction\_name)


##Running test cases
From bash shell:
python3 testnextbus.py

from python:
import testnextbus.py
