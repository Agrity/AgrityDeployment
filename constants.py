# URLs and Locations
# ==================
TEST_APP_URL = 'ec2-user@ec2-54-183-211-225.us-west-1.compute.amazonaws.com';
PROD_APP_URL = 'ec2-user@ec2-54-183-160-86.us-west-1.compute.amazonaws.com';

TEST_SERVER_URL = 'ec2-user@ec2-54-193-71-252.us-west-1.compute.amazonaws.com';
PROD_SERVER_URL = 'ec2-user@ec2-52-53-232-44.us-west-1.compute.amazonaws.com';

DESINATION_FOLDER = '~/.'

# Remote Scripts
# ==============
REMOTE_SCRIPTS_LOCATION = '/Users/ryandavies/Development/AgrityDeployment/remote-scripts/'

INSTALL_SCRIPT_NAME = 'play-install.sh'
INSTALL_SCRIPT_LOCATION = REMOTE_SCRIPTS_LOCATION + INSTALL_SCRIPT_NAME


INSTALL_APP_SCRIPT_NAME = 'angular-install.sh'
INSTALL_APP_SCRIPT_LOCATION = REMOTE_SCRIPTS_LOCATION + INSTALL_APP_SCRIPT_NAME

PEM_LOCATION = '/Users/ryandavies/.pem/AngularKey.pem'

# Server Specific Constants
# =========================
TEST_RESOURCE = 'test.conf'
PROD_RESOURCE = 'prod.conf'

SERVER_NAME = 'test-app'

# App Specific Constants
# ======================
ZIPPED_APP_NAME = 'app.tgz'

APP_DIST_FOLDER = 'dist'

# Development Areas
# =================
FRONT_END = 'front'
BACK_END = 'back'

# COMMANDS
# ========
DEPLOY_COMMAND = 'deploy'
COMPILE_COMMAND = 'compile'
RUN_COMMAND = 'run'
PUSH_COMMAND = 'push'
INSTALL_COMMAND = 'install'
LOGS_COMMAND = 'logs'

HELP_COMMAND = 'help'

# Back Global Helpers
# ===================
def getDestinationAddress(prod):
    return PROD_SERVER_URL if prod else TEST_SERVER_URL

def getDestinationLocation(prod):
    destUrl = PROD_SERVER_URL if prod else TEST_SERVER_URL
    return destUrl + ':' + DESINATION_FOLDER

# Front Global Helpers
# ===================
def getFrontDestinationAddress(prod):
    return PROD_APP_URL if prod else TEST_APP_URL

def getFrontDestinationLocation(prod):
    destUrl = PROD_APP_URL if prod else TEST_APP_URL
    return destUrl + ':' + DESINATION_FOLDER
