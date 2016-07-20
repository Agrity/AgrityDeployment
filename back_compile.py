import push, constants
import sys, getopt, subprocess, os

def compile(argv):
    __printStart()

    if not __checkActivatorPresent():
        __printWrongFolderArea()
        sys.exit(2)

    __compile()


def __checkActivatorPresent():
    return os.path.isfile('activator')

def __compile():
    os.system('./activator clean compile universal:package-zip-tarball')

def __printStart():
    print()
    print('+++ Start Compile')
    print('========================================')
    print()

def __printWrongFolderArea():
    print('Invalid Current Working Directory:')
    print('Should be called in base directory of play application.')

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity ' + constants.COMPILE_COMMAND)

