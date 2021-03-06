import os
import sys
import subprocess
import datetime

cmd = 'py.test -v --capture=no test.py'

def test():
    log = subprocess.run(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    writelog(log)

def testtype(subject):
    log = subprocess.run(cmd + ' -k ' + subject, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    writelog(log)

def writelog(log):
    name = 'log_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
    content = log.stdout.decode('utf8').strip()
    logfile = open(name, 'w')
    logfile.write(content)
    logfile.close()

    file = open(name, 'r')
    data = file.readlines()
    file.close()

    count = 0
    for i in data:
        if 'FAILED' in i:
            count += 1
    print(name)
    print('>>> ' + str(count) + ' FAILED')

if __name__ == '__main__':
    args = sys.argv
    i = 0
    while i < 10:
        if len(args) == 1:
            test()
            i += 1
        elif len(args) == 2:
            testtype(args[1])
            i += 1
        else:
            print('ERROR')
            sys.exit()
