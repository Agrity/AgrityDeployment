import front_compile, front_push, front_install, constants
import sys, getopt, subprocess, os

def deployApp(argv):
    # Will exit if in incorrect working directory
    front_compile.compile(argv)

    argv.append('-f')
    argv.append(constants.ZIPPED_APP_NAME)

    front_push.pushApp(argv)
    front_install.installApp(argv)

def __checkActivatorPresent():
    return os.path.isfile('activator')

def __compile():
    os.system('./activator clean compile universal:package-zip-tarball')


def __getDestinationAddress(prod):
    return constants.PROD_SERVER_URL if prod else constants.TEST_SERVER_URL

def __printWrongFolderArea():
    print('Invalid Current Working Directory:')
    print('Should be called in base directory of play application.')

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity ' + constants.LOGS_COMMAND + ' [-p]')

