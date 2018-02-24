import requests
import textwrap

import tfl.constants
from colors import color

class Line(object):
    def __init__(self, json):
        self.name = json['name']
        self.id = json['id']
        self.mode = json['modeName']
        self.severity = json['lineStatuses'][0]['statusSeverity']
        self.severity_desc = json['lineStatuses'][0]['statusSeverityDescription']
        if 'disruption' in json['lineStatuses'][0]:
            self.disruption =  json['lineStatuses'][0]['disruption']['description']
        else:
            self.disruption = None

    def colours(self):
        try:
            return tfl.constants.line_colours[self.id]
        except KeyError:
            try:
                return tfl.constants.mode_colours[self.mode]
            except KeyError:
                return 'default', 'default'

    def __str__(self):
        fg, bg = self.colours()
        name = color(' {:26s} '.format(self.name), fg, bg)
        return '{} {}'.format(name, self.severity_desc)

def lines_for_modes(modes):
    url = 'https://api.tfl.gov.uk/line/mode/' + ','.join(modes) + '/status'
    r = requests.get(url)
    for line in r.json():
        yield Line(line)

def lines_for_ids(ids):
    url = 'https://api.tfl.gov.uk/line/' + ','.join(ids) + '/status'
    r = requests.get(url)
    for line in r.json():
        yield Line(line)

if __name__ == '__main__':
    dis = []

    for line in lines_for_modes(['tube']):
        print(line)
        if line.disruption is not None:
            dis.append(line.disruption)

    for line in lines_for_modes(['dlr', 'overground', 'tram', 'tflrail']):
        print(line)
        if line.disruption is not None:
            dis.append(line.disruption)

    for line in lines_for_ids(['122', '185']):
        print(line)
        if line.disruption is not None:
            dis.append(line.disruption)

    if len(dis) > 0:
        print('')
        print('\n\n'.join([textwrap.fill(d, 77) for d in dis]))

    print('')
