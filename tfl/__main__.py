import argparse
import textwrap

import tfl.line
import tfl.stop

def main():
    parser = argparse.ArgumentParser(description='Display TfL service status.')

    parser.add_argument('-m', '--mode', type=str, action='append', default=[],
                        help='Display status for a mode.')
    parser.add_argument('-l', '--line', type=str, action='append', default=[],
                        help='Display status for a specific line.')
    parser.add_argument('-s', '--stop', type=str, action='append',  default=[],
                        nargs=2, metavar=('stop','modes'),
                        help='Display information for a specific stop and modes.')

    parser.add_argument('-D', '--details',
                       help='Display detailed information about disruptions.',
                       action='store_true')
    parser.add_argument('-a', '--arrivals',
                       help='Display arrivals for each stop.',
                       action='store_true')

    args = parser.parse_args()

    dis = []
    err = []

    for mode in args.mode:
        try:
            for line in tfl.line.lines_for_modes([mode]):
                print(line)
                if line.disruption is not None:
                    dis.append(line.disruption)
        except TypeError:
            err.append(mode)
        except KeyError:
            err.append(mode)


    for l in args.line:
        try:
            for line in tfl.line.lines_for_ids([l]):
                print(line)
                if line.disruption is not None:
                    dis.append(line.disruption)
        except TypeError:
            err.append(l)
        except KeyError:
            err.append(l)

    if args.details and len(dis) > 0:
        print('')
        print('\n\n'.join([textwrap.fill(d, 68) for d in dis]))

    for stop_id, modes in args.stop:
        try:
            stop = tfl.stop.Stop(stop_id)
            print('')
            print(stop)
            print('')
            dis = []
            for line in stop.lines(modes=modes):
                print(line)
                if line.disruption is not None:
                    dis.append(line.disruption)

            if args.details and len(dis) > 0:
                print('')
                print('\n\n'.join([textwrap.fill(d, 68) for d in dis]))

            if args.arrivals:
                print('')
                for a in stop.arrivals():
                    print(a)
        except TypeError:
            err.append(stop_id)
        except KeyError:
            err.append(stop_id)

    if len(err) > 0:
        print('Errors were encountered while processing the following items:', ' '.join(err))

if __name__ == '__main__':
    main()

