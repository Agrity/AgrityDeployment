import front_compile, front_deploy, front_push, front_install
import back_compile, back_deploy, back_push, back_install, logs, constants
import sys, getopt, subprocess

def main(argv):

    # Check arguments not empty
    if len(argv) < 2:
        __printUseCase();
        sys.exit(2);

    devArea = argv[0]

    if devArea == constants.FRONT_END:
        __processFront(argv[1:])

    elif devArea == constants.BACK_END:
        __processBack(argv[1:])

    else: # Invalid Second Command
        __printUseCase();
        sys.exit(2);



def __processFront(argv):
    command = argv[0]

    if command == constants.DEPLOY_COMMAND:
        front_deploy.deployApp(argv[1:])

    elif command == constants.COMPILE_COMMAND:
        front_compile.compile(argv[1:])

    elif command == constants.PUSH_COMMAND:
        front_push.pushApp(argv[1:])

    elif command == constants.INSTALL_COMMAND:
        front_install.installApp(argv[1:])

    elif command == constants.LOGS_COMMAND:
        logs.viewFrontLogs(argv[1:])

    elif command == constants.HELP_COMMAND:
        __printAvailableFrontCommands()

    else:
        print('Invalid Command: ' + command)
        __printAvailableFrontCommands()


def __processBack(argv):

    command = argv[0]


    if command == constants.DEPLOY_COMMAND:
        back_deploy.deployServer(argv[1:])
    
    elif command == constants.COMPILE_COMMAND:
        back_compiler.compile(argv[1:])

    elif command == constants.RUN_COMMAND:
        back_push.pushServer(argv[1:])
        back_install.installServer(argv[1:])

    elif command == constants.PUSH_COMMAND:
        back_push.pushServer(argv[1:])

    elif command == constants.INSTALL_COMMAND:
        back_install.installServer(argv[1:])

    elif command == constants.LOGS_COMMAND:
        logs.viewBackLogs(argv[1:])

    elif command == constants.HELP_COMMAND:
        __printAvailableBackCommands()

    else:
        print('Invalid Command: ' + command)
        __printAvailableBackCommands()



def __printUseCase():
    print('Invalid Agrity Arguments:')
    print('example: agrity [front|back] <command> ...')

def __printAvailableFrontCommands():
    print('Available Back Commands:')
    print('\t' + constants.DEPLOY_COMMAND)
    print('\t' + constants.COMPILE_COMMAND)
    print('\t' + constants.PUSH_COMMAND)
    print('\t' + constants.INSTALL_COMMAND)
    print('\t' + constants.LOGS_COMMAND)

def __printAvailableBackCommands():
    print('Available Back Commands:')
    print('\t' + constants.DEPLOY_COMMAND)
    print('\t' + constants.COMPILE_COMMAND)
    print('\t' + constants.RUN_COMMAND)
    print('\t' + constants.PUSH_COMMAND)
    print('\t' + constants.INSTALL_COMMAND)
    print('\t' + constants.LOGS_COMMAND)


if __name__ == "__main__":
       main(sys.argv[1:])




