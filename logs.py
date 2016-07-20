import push, constants
import sys, getopt, subprocess, os

def viewBackLogs(argv):
    prod = False

    try:
        opts, args = getopt.getopt(argv, 'p', ['prod'])
    except getopt.GetoptError:
        printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--prod'):
            prod = True


    command = 'tail -f screenlog.0'

    ssh = subprocess.Popen(["ssh", '-i', constants.PEM_LOCATION,
                            constants.getDestinationAddress(prod), command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    for line in iter(ssh.stdout.readline, ''):
        sys.stdout.write(line.decode('utf-8'))

def viewFrontLogs(argv):
    prod = False

    try:
        opts, args = getopt.getopt(argv, 'p', ['prod'])
    except getopt.GetoptError:
        printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--prod'):
            prod = True


    command = 'tail -f screenlog.0'

    ssh = subprocess.Popen(["ssh", '-i', constants.PEM_LOCATION,
                            constants.getFrontDestinationAddress(prod), command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    for line in iter(ssh.stdout.readline, ''):
        sys.stdout.write(line.decode('utf-8'))

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity ' + constants.LOGS_COMMAND + ' [-p]')

