import push, constants
import sys, getopt, subprocess, os, tarfile

def installServer(argv):
    __printStart()

    zippedServer = ''
    prod = False
    additionalConfig = ''

    try:
        opts, args = getopt.getopt(argv, 'f:pd', ['file=', 'prod', 'apply-downs'])
    except getopt.GetoptError:
        __printUseCase()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-f', '--file'):
            zippedServer = os.path.basename(arg)

        elif opt in ('-p', '--prod'):
            # Hacky Check. Fix to allow different additional config on prod
            if additionalConfig != '':
                __downsInProdError()
                sys.exit(2)
            prod = True

        elif opt in ('-d', '--apply-downs'):
            if prod: # Cannot run downs in prod
                __downsInProdError()
                sys.exit(2)
            additionalConfig = additionalConfig \
                + ' -Dplay.evolutions.db.default.autoApply=true' \
                + ' -Dplay.evolutions.db.default.autoApplyDowns=true'

    
    if zippedServer == '':
        __printUseCase()
        sys.exit(2)
    
    __sendInstallScript(prod)

    command = 'sh ' + constants.INSTALL_SCRIPT_NAME \
            + ' ' + zippedServer \
            + ' ' + constants.SERVER_NAME \
            + ' ' + __getConfigResource(prod) \
            + ' ' + additionalConfig

    ssh = subprocess.Popen(["ssh", '-i', constants.PEM_LOCATION,
                            constants.getDestinationAddress(prod), command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    for line in iter(ssh.stdout.readline, ''):
        sys.stdout.write(line.decode('utf-8'))

def __getConfigResource(prod):
    resource = constants.PROD_RESOURCE if prod else constants.TEST_RESOURCE
    return '-Dconfig.resource=' + resource

def __sendInstallScript(prod):
    push.pushAWSFile(
            constants.INSTALL_SCRIPT_LOCATION,
            constants.getDestinationLocation(prod))

def __downsInProdError():
    print('Error: Cannot use downs on production server')

def __printStart():
    print()
    print('+++ Start Install')
    print('========================================')
    print()

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity ' + constants.INSTALL_COMMAND \
            + ' -f <zipped-server-file> [-p]')
