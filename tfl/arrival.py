import tfl.constants
from colors import color

class Arrival(object):
    def __init__(self, json):
        self.name = json['lineName']
        self.id = json['id']
        self.timeToStation = json['timeToStation']
        self.destination = json['destinationName']
        self.mode = json['modeName']

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
        name = color(' {:18s} '.format(self.name), fg, bg)
        dest = ' {:40s}'.format(self.destination)
        return '{}{} {:2d} mins'.format(name, dest, self.timeToStation//60)

