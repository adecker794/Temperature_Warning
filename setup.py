import os
import shutil
import glob


def copyAllFilesinDir(srcDir, dstDir):
    
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '/*'):
            # Move each file to destination Directory
            print(filePath)
            shutil.copy(filePath, dstDir)
    else:
        print("srcDir & dstDir should be Directories")
	
sourceDir = os.getcwd() + '/TempWarningService'
destDir =  '/usr/local/bin/TempWarningService'

print('Hello! This is the setup for the Temperature Warning Script')
print('Have you set up the config.ini file yet? Y\\N')
configInput = input("Please enter Y\\N:\n")
if (configInput.upper() == "Y"):
    packagesInput = input("Have you installed all the packages referenced in the github repo readme? Y\\N:\n")
    if (packagesInput.upper() == "Y"):
        print('I am going to now start the process of setting up the package as a service.')
        try:
            os.mkdir(destDir)
        except OSError:
            print ("Creation of the directory %s failed" % destDir)
        else:
            print ("Successfully created the directory %s " % destDir)
        copyAllFilesinDir(sourceDir,destDir)
        shutil.copy(os.getcwd() + '/TempWarningService.service', '/etc/systemd/system/TempWarningService.service')
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl start TempWarningService.service")
        #shutil.copy('./TempWarningService', '/usr/local/bin/TempWarningService')
        #shutil.move('./TempWarningService')

        #/usr/local
    else:
        print('Please install the packages referenced in the github repo readme')
        print('Those packages are:\n'
        'python3')

else:
    print('Please edit the config.ini to reflect your parameters')
