import push, constants
import sys, getopt, os, tarfile

def compile(argv):
    __printStart()

    if not __checkGulpfilePresent():
        __printWrongFolderArea()
        sys.exit(2)

    __compile()

    __zip()


def __checkGulpfilePresent():
    return os.path.isfile('gulpfile.js')

def __compile():
    os.system('npm install && gulp build')

def __zip():
    print()
    print('Zipping...')
    with tarfile.open(constants.ZIPPED_APP_NAME, "w:gz") as tar:
        tar.add(constants.APP_DIST_FOLDER,
                arcname=os.path.basename(constants.APP_DIST_FOLDER))

def __printStart():
    print()
    print('+++ Start App Compile')
    print('========================================')
    print()

def __printWrongFolderArea():
    print('Invalid Current Working Directory:')
    print('Should be called in base directory of angular application.')

def __printUseCase():
    print('Invalid Arguments:')
    print('\texample: agrity front ' + constants.COMPILE_COMMAND)

