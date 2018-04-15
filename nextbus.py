import sys
import requests
import argparse
import time
import urllib.request

DEBUG = False
BASEURL = 'http://svc.metrotransit.org/NexTrip/{0}?format=json'


# finds first element corresponding to key <key_in> and containing value <name> then
# returns the value corresponding to key <key_out>
def get(path, name, key_in, key_out):
    url = BASEURL.format(path)
    code = urllib.request.urlopen(url).getcode()
    if code != 200:
        raise RuntimeError('URL {0} is unreachable. Error code {1}'.format(url, code))
    request = requests.get(url)
    data = request.json()
    if data is None:
        raise RuntimeError('No data found at URL: {0}'.format(url))
    for element in data:
        if name in element[key_in]:
            return element[key_out]
    return None


def get_route_num(route_name):
    route_num = get('Routes', route_name, 'Description', 'Route')
    return route_num


# checks if route_num travels in given direction
# if so it returns the corresponding direction number
def get_direction_num(direction_name, route_num):
    url = 'Directions/{0}'.format(route_num)
    direction_num = get(url, '{0}'.format(direction_name.upper()), 'Text', 'Value')
    return direction_num


def get_stop_id(stop_name, route_num, direction_num):
    url = 'Stops/{0}/{1}'.format(route_num, direction_num)
    stop_id = get(url, stop_name, 'Text', 'Value')
    return stop_id


# return a string of time information on the next coming departure
def get_mins_left(route_name, stop_name, direction_name):
    route_num = get_route_num(route_name)
    if DEBUG:
        print('route number = {0}'.format(route_num))
    if route_num is None:
        return '{0} has no remaining departures listed for the day'.format(route_name)
    direction_num = get_direction_num(direction_name, route_num)
    if DEBUG:
        print('direction number = {0}'.format(direction_num))
    if direction_num is None:
        return 'Route {0} does not travel {1}'.format(route_num, direction_name)
    stop_id = get_stop_id(stop_name, route_num, direction_num)
    if DEBUG:
        print('stop ID = {0}'.format(stop_id))
    if stop_id is None:
        return('Route {0} travelling {1} has no remaining departures listed for the '
               'day'.format(route_num, direction_name))
    url = '{0}/{1}/{2}'.format(route_num, direction_num, stop_id)
    next_timestamp = get(url, 'Date', 'DepartureTime', 'DepartureTime')
    if next_timestamp is None:
        return ('Route {0} travelling {1} has no remaining departures listed for '
                'stop {2} for the day'.format(route_num, direction_name, stop_id))
    next_arrival_time = float(next_timestamp[6:16])  # #seconds until next arrival
    if next_arrival_time is None or next_arrival_time == 0:
        raise RuntimeError('Next arrival time was not found')
    mins_remaining = int(next_arrival_time - time.time()) // 60
    if mins_remaining >= 1:
        return '{0} minutes remaining until the next departure'.format(mins_remaining)
    return 'The next departure is due'


def main(route_name, stop_name, direction_name):
    next_departure = get_mins_left(route_name, stop_name, direction_name)
    if next_departure is not None:
        print(next_departure)
        return 0
    else:
        raise RuntimeError('Could not find the remaining time until the next departure')  # #probably can't get here


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('route')
    parser.add_argument('stop')
    parser.add_argument('direction')
    args = parser.parse_args()
    sys.exit(main(args.route, args.stop, args.direction))