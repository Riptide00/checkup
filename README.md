## Checkup

Simple script to check if hosts are responding.
Pings at an interval and displayes hosts status.
Written in Python3.7, tested in a Cygwin enviroment on Windows.

## Usage

```
    python checkup host1,host2

```
or
```
    python checkup filepath.txt
```
```
checkup.py [-h] [-w WIDTH] [-i INTERVAL] [-c COLOR] hosts

positional arguments:
  hosts                 Accepts a string of hosts seperated by a ",", or a
                        path to file with hosts seperated by a newline

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width of the columns
  -i INTERVAL, --interval INTERVAL
                        Interval at which pings are send.
  -c COLOR, --color COLOR
                        Set to 'True' for colored output.
```