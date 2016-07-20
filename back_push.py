import constants, push
import sys, getopt, subprocess

def pushServer(argv):

    __printStart()

    filePath = ''
    prod = False

    try:
        opts, args = getopt.getopt(argv, 'f:p', ['file=', 'prod'])
    except getopt.GetoptError:
        __printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-f', '--file'):
            filePath = arg

        elif opt in ('-p', '--prod'):
            prod = True
    
    if filePath == '':
        __printUseCase()
        sys.exit(2)

    push.pushAWSFile(filePath, constants.getDestinationLocation(prod))


def __printStart():
    print()
    print('+++ Start Push')
    print('========================================')
    print()

def __printUseCase():
    print('Invalid Push Arguments:')
    print('\texample: agrity push -f <zipped-server-file> [-p]')
