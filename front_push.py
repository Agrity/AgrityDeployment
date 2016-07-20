import constants, push
import sys, getopt, subprocess

def pushApp(argv):

    __printStart()

    folderPath = ''
    prod = False

    try:
        opts, args = getopt.getopt(argv, 'f:p', ['folder=', 'prod'])
    except getopt.GetoptError:
        __printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-f', '--folder'):
            folderPath = arg

        elif opt in ('-p', '--prod'):
            prod = True
    
    if folderPath == '':
        __printUseCase()
        sys.exit(2)

    push.pushAWSFolder(folderPath, constants.getFrontDestinationLocation(prod))


def __printStart():
    print()
    print('+++ Start App Push')
    print('========================================')
    print()

def __printUseCase():
    print('Invalid Push Arguments:')
    print('\texample: agrity front push -f <app-folder> [-p]')
