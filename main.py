import compiler, deploy, push, install, logs, constants
import sys, getopt, subprocess

def main(argv):

    # Check arguments not empty
    if not argv:
        __printUseCase();
        sys.exit(2);

    command = argv[0]

    if command == constants.DEPLOY_COMMAND:
        deploy.deployServer(argv[1:])
    
    elif command == constants.COMPILE_COMMAND:
        compiler.compile(argv[1:])


    elif command == constants.RUN_COMMAND:
        push.pushServer(argv[1:])
        install.installServer(argv[1:])

    elif command == constants.PUSH_COMMAND:
        push.pushServer(argv[1:])

    elif command == constants.INSTALL_COMMAND:
        install.installServer(argv[1:])

    elif command == constants.LOGS_COMMAND:
        logs.viewLogs(argv[1:])

    elif command == constants.HELP_COMMAND:
        __printAvailableCommands()

    else:
        print 'Invalid Command: ' + command
        __printAvailableCommands()


def __printUseCase():
    print 'Invalid Agrity Arguments:'
    print 'example: agrity <command> ...'

def __printAvailableCommands():
    print 'Available Commands:'
    print '\t' + constants.COMPILE_COMMAND
    print '\t' + constants.RUN_COMMAND
    print '\t' + constants.PUSH_COMMAND
    print '\t' + constants.INSTALL_COMMAND


if __name__ == "__main__":
       main(sys.argv[1:])




