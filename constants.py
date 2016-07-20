TEST_SERVER_URL = 'ec2-user@ec2-54-193-71-252.us-west-1.compute.amazonaws.com';
PROD_SERVER_URL = 'ec2-user@ec2-52-53-232-44.us-west-1.compute.amazonaws.com';

TEST_RESOURCE = 'test.conf'
PROD_RESOURCE = 'prod.conf'

DESINATION_FOLDER = '~/.'

INSTALL_SCRIPT_LOCATION = '/Users/ryandavies/Development/AgrityDeployment/remote-scripts/play-install.sh'
INSTALL_SCRIPT_NAME = 'play-install.sh'

PEM_LOCATION = '/Users/ryandavies/.pem/AngularKey.pem'

APP_NAME = 'test-app'

# Development Areas
FRONT_END = 'front'
BACK_END = 'back'

# COMMANDS
DEPLOY_COMMAND = 'deploy'
COMPILE_COMMAND = 'compile'
RUN_COMMAND = 'run'
PUSH_COMMAND = 'push'
INSTALL_COMMAND = 'install'
LOGS_COMMAND = 'logs'

HELP_COMMAND = 'help'

# Global Helpers

def getDestinationAddress(prod):
    return PROD_SERVER_URL if prod else TEST_SERVER_URL


def getDestinationLocation(prod):
    destUrl = PROD_SERVER_URL if prod else TEST_SERVER_URL
    return destUrl + ':' + DESINATION_FOLDER
