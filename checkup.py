import os
import sys
import time
import argparse


column_width = 15
interval = 1
hosts = []


def main():
    ''' Main function. '''
    global hosts
    parser = argparse.ArgumentParser()
    parser.add_argument("hosts")
    args = parser.parse_args()
    if os.path.exists(args.hosts) and os.path.isfile(args.hosts):
        f = open(args.hosts)
        content = f.readlines()
        for host in content:
            hosts.append(host.rstrip())
    else:
        hosts = args.hosts.split(',')
    # TODO: Add arguments for column width, color and interval
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
        if result:
            print(raw % (column_width, h, green('  UP')))
        else:
            print(raw % (column_width, h, red(' DOWN')))
    time.sleep(interval)


def green(text):
    ''' Color text green. '''
    return ('\033[0;32m%s\033[0;0m' % text)


def red(text):
    ''' Color text red. '''
    return ('\033[1;31m%s\033[0;0m' % text)


if __name__ == '__main__':
    main()
