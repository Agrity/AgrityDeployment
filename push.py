import constants
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

    __sendFile(filePath, __getDestinationAddress(prod))

def __sendFile(filePath, destination):
    subprocess.Popen(['scp', '-i', constants.PEM_LOCATION, filePath, destination]).wait()
    
    
def __getDestinationAddress(prod):
    destUrl = constants.PROD_SERVER_URL if prod else constants.TEST_SERVER_URL
    return destUrl + ':' + constants.DESINATION_FOLDER

def __printStart():
    print
    print '+++ Start Push'
    print '========================================'
    print

def __printUseCase():
    print 'Invalid Push Arguments:'
    print '\texample: agrity push -f <zipped-server-file> [-p]'
