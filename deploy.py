import compiler, push, install
import sys, getopt, subprocess, os

def deployServer(argv):

    # Will exit if in incorrect working directory
    compiler.compile(argv)

    zippedServer = ''

    os.chdir('./target/universal')
    for file in os.listdir("./"):
        if file.endswith(".tgz"):
            zippedServer = os.path.realpath(file)


    argv.append('-f')
    argv.append(zippedServer)

    push.pushServer(argv)
    install.installServer(argv)

def __checkActivatorPresent():
    return os.path.isfile('activator')

def __compile():
    os.system('./activator clean compile universal:package-zip-tarball')


def __getDestinationAddress(prod):
    return constants.PROD_SERVER_URL if prod else constants.TEST_SERVER_URL

def __printWrongFolderArea():
    print 'Invalid Current Working Directory:'
    print 'Should be called in base directory of play application.'

def __printUseCase():
    print 'Invalid Arguments:'
    print '\texample: agrity ' + constants.LOGS_COMMAND + ' [-p]'

