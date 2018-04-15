import nextbus
import traceback

route_name = 'METRO Blue Line'
stop_name = 'Target Field Station Platform 1'
direction_name = 'south'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
        print(traceback.format_exc())
        print(exc)

route_name = 'Express - Target - Hwy 252 and 73rd Av P&R - Mpls'
stop_name = 'Target North Campus Building F'
direction_name = 'south'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)

route_name = 'METRO Green Line'
stop_name = 'Target Field Station Platform 2'
direction_name = 'east'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)

route_name = 'METRO Red Line'
stop_name = 'Mall of America Station'
direction_name = 'north'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)

route_name = '5 - Brklyn Center - Fremont - 26th Av - Chicago - MOA'
stop_name = 'Chicago Lake Transit Center'
direction_name = 'north'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)

route_name = '5 - Brklyn Center - Fremont - 26th Av - Chicago - MOA'
stop_name = 'Chicago Lake Transit Center'
direction_name = 'east'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)

route_name = '5 - Brklyn Center - Fremont - 26th Av - Chicago - MOA'
stop_name = 'Chicago Lake Transit Center'
direction_name = 'east'
print('Testing route "{0}" at stop "{1}" travelling "{2}"'.format(route_name, stop_name, direction_name))
try:
    nextbus.main(route_name, stop_name, direction_name)
    print("\n")
except RuntimeError as exc:
    print(traceback.format_exc())
    print(exc)