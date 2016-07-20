import push, constants
import sys, getopt, subprocess, os, tarfile, pygame

def installServer(argv):
    __printStart()

    zippedServer = ''
    prod = False
    additionalConfig = ''

    try:
        opts, args = getopt.getopt(argv, 'f:pd', ['file=', 'prod', 'apply-downs'])
    except getopt.GetoptError:
        printUseCase()
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
        printUseCase()
        sys.exit(2)
    
    __sendInstallScript(prod)

    command = 'sh ' + constants.INSTALL_SCRIPT_NAME \
            + ' ' + zippedServer \
            + ' ' + constants.APP_NAME \
            + ' ' + __getConfigResource(prod) \
            + ' ' + additionalConfig

    ssh = subprocess.Popen(["ssh", '-i', constants.PEM_LOCATION,
                            __getDestinationAddress(prod), command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    #__initPygame()

    for line in iter(ssh.stdout.readline, ''):
        sys.stdout.write(line)
        

    #result = ssh.stdout.readlines()
    #if result == []:
    #    error = ssh.stderr.readlines()
    #    print >>sys.stderr, "ERROR: %s" % error
    #else:
    #    for line in result:
    #        print line

def __initPygame():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Agrity Server Install')
    pygame.mouse.set_visible(0)

def __getDestinationAddress(prod):
    return constants.PROD_SERVER_URL if prod else constants.TEST_SERVER_URL

def __getConfigResource(prod):
    resource = constants.PROD_RESOURCE if prod else constants.TEST_RESOURCE
    return '-Dconfig.resource=' + resource

def __sendInstallScript(prod):
    args = ['-f', constants.INSTALL_SCRIPT_LOCATION]
    if prod:
        args.append('-p')
    push.pushServer(args)

def __downsInProdError():
    print >>sys.stderr, 'Error: Cannot use downs on production server'

def __printStart():
    print
    print '+++ Start Install'
    print '========================================'
    print

def __printUseCase():
    print 'Invalid Arguments:'
    print '\texample: agrity ' + constants.INSTALL_COMMAND \
            + ' -f <zipped-server-file> [-p]'
