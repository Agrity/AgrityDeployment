import constants
import subprocess

def pushAWSFile(filePath, destination):
    subprocess.Popen(['scp', '-i', constants.PEM_LOCATION, filePath, destination]).wait()
