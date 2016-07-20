import push, constants
import sys, getopt, subprocess, os, tarfile

def installApp(argv):
    __printStart()

    prod = False

    try:
        # Note -f and --folder= are unused.
        opts, args = getopt.getopt(argv, 'f:p', ['folder=', 'prod'])
    except getopt.GetoptError:
        __printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--prod'):
            prod = True

    
    __sendInstallScript(prod)

    command = 'sh ' + constants.INSTALL_APP_SCRIPT_NAME \
            + ' ' + constants.ZIPPED_APP_NAME \
            + ' ' + constants.APP_DIST_FOLDER

    ssh = subprocess.Popen(["ssh", '-i', constants.PEM_LOCATION,
                            constants.getFrontDestinationAddress(prod),
                            command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    for line in iter(ssh.stdout.readline, ''):
        sys.stdout.write(line.decode('utf-8'))

def __sendInstallScript(prod):
    push.pushAWSFile(
            constants.INSTALL_APP_SCRIPT_LOCATION,
            constants.getFrontDestinationLocation(prod))

def __printStart():
    print()
    print('+++ Start App Install')
    print('========================================')
    print()

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity ' + constants.INSTALL_COMMAND \
            + ' -f <zipped-server-file> [-p][-d]')
