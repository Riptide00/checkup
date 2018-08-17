import os
import sys
import time
import argparse


column_width = 15
interval = 1
args = []


def main():
    ''' Main function. '''
    global hosts
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("hosts",
                        help=('Accepts a string of hosts seperated '
                              'by a ",", or a path to file with hosts'
                              ' seperated by a newline'))
    parser.add_argument("-w", "--width", type=int,
                        help="Width of the columns")
    parser.add_argument("-i", "--interval", type=int,
                        help="Interval at which pings are send.")
    parser.add_argument("-c", "--color",
                        help="Set to 'True' for colored output.")
    args = parser.parse_args()
    if args.interval:
        global interval
        interval = args.interval
    if args.width:
        global column_width
        column_width = args.width
    if os.path.exists(args.hosts) and os.path.isfile(args.hosts):
        f = open(args.hosts)
        content = f.readlines()
        for host in content:
            hosts.append(host.rstrip())
    else:
        hosts = args.hosts.split(',')
    while True:
        try:
            draw_screen()
        except KeyboardInterrupt:
            cleanup()
            print('Quitting checkup...')
            sys.exit(0)
        except Exception as e:
            cleanup()
            raise


def cleanup():
    ''' Cleanup artifacts. '''
    os.system('rm NUL')


def ping_host(host):
    ''' Ping host. '''
    # TODO: Make crossplatform, use subprocess instead of os.system
    return not os.system('ping %s -n 1 > NUL' % (host,))


def get_data():
    ''' Ping all hosts. '''
    results = []
    global hosts
    for host in hosts:
        results.append((host, ping_host(host)))
    return results


def draw_screen():
    ''' Display results. '''
    raw = '%-*s    %s'
    os.system('clear')
    print(raw % (column_width, '      HOST', 'STATUS'))
    for host, result in get_data():
        h = host[:column_width] if len(host) > column_width else host
        if args.color:
            if result:
                print(raw % (column_width, h, green('  UP')))
            else:
                print(raw % (column_width, h, red(' DOWN')))
        else:
            if result:
                print(raw % (column_width, h, '  UP'))
            else:
                print(raw % (column_width, h, ' DOWN'))
    time.sleep(interval)


def green(text):
    ''' Color text green. '''
    return ('\033[0;32m%s\033[0;0m' % text)


def red(text):
    ''' Color text red. '''
    return ('\033[1;31m%s\033[0;0m' % text)


if __name__ == '__main__':
    main()
