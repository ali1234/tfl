line_colours = {
    'bakerloo': ('#ffffff', '#996633'),
    'central': ('#ffffff', '#cc3333'),
    'circle': ('#000000', '#ffcc00'),
    'district': ('#ffffff', '#006633'),
    'hammersmith-city': ('#000000', '#cc9999'),
    'jubilee': ('#ffffff', '#868f98'),
    'metropolitan': ('#ffffff', '#660066'),
    'northern': ('#ffffff', '#000000'),
    'piccadilly': ('#ffffff', '#0019a8'),
    'victoria': ('#000000', '#0099cc'),
    'waterloo-city': ('#000000', '#66cccc'),
}

mode_colours = {
    'bus': ('#ffffff', '#cc3333'),
    'dlr': ('#000000', '#009999'),
    'tram': ('#ffffff', '#66cc00'),
    'overground': ('#000000', '#e86a10'),
    'tflrail': ('#ffffff', '#0019a8'),
}

if __name__ == '__main__':
    from colors import color

    for k,v in line_colours.items():
        print(color(' {:20s} '.format(k), v[0], v[1]))

    for k,v in mode_colours.items():
        print(color(' {:20s} '.format(k), v[0], v[1]))

