import requests
import textwrap

import tfl.constants
import tfl.arrival
import tfl.line

from colors import color

class Stop(object):
    def __init__(self, id):
        self.id = id
        url = 'https://api.tfl.gov.uk/stoppoint/' + self.id
        json = requests.get(url).json()
        self.name = json['commonName']
        self.line_ids = [l['id'] for l in json['lines']]

    def __str__(self):
        return color(self.name, fg='white', style='bold')

    def lines(self, modes = None):
        for line in tfl.line.lines_for_ids(self.line_ids):
            if modes is not None and line.mode in modes:
                yield line

    def arrivals(self):
        url = 'https://api.tfl.gov.uk/stoppoint/' + self.id + '/arrivals'
        r = requests.get(url)
        try:
            arrivals = [tfl.arrival.Arrival(arr) for arr in r.json()]
            arrivals.sort(key = lambda x: x.timeToStation)
            yield from arrivals
        except TypeError:
            pass

if __name__ == '__main__':
    for stop_id, modes in [('910GCNDAW', ['overground', 'tube']), ('910GFORESTH',['overground', 'national-rail']), ('490006920W',['bus'])]:
        stop = Stop(stop_id)
        print(stop)
        print('')
        dis = []
        for line in stop.lines(modes=modes):
            print(line)
            if line.disruption is not None:
                dis.append(line.disruption)

        if len(dis) > 0:
            print('')
            print('\n\n'.join([textwrap.fill(d, 77) for d in dis]))
        print('')
        for a in stop.arrivals():
            print(a)
        print('')