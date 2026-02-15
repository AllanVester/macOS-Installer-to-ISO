import argparse
import sys
import os
import subprocess

























location = (os.path.dirname(os.path.realpath(__file__))).replace('\\', '/') + '/'
os.chdir(location)

if sys.platform.startswith('linux'): # could be 'linux', 'linux2', 'linux3', ...
    
    pass

elif os.name == 'nt': # Windows, Cygwin, etc. (either 32-bit or 64-bit)

    pass

elif sys.platform == 'darwin': # MAC OS X
    
    pass

























def splitFiles(file, size, branch):

    try:

        os.makedirs("split", exist_ok = True)

        process = subprocess.run(
            f'split -d -b {size}m {file} split/{file}.part', 
            shell = True, 
            check = True, 
            text = True, 
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE,
        )

        if process.returncode != 0:

            print(f"Error in executing command, output: {process.stderr}.")

            return False

        return True

    except Exception as e:

        print(f"An error occurred in splitFiles() for {branch}-branch: {str(e)}.")

























def downloadISO(version, filePath):
    
    try:
        
        if version == 'cheetah':
            
            pass
        
        if version == 'puma':
            
            pass
        
        if version == 'jaguar':
            
            pass
        
        if version == 'panther':
            
            pass
        
        if version == 'tiger':
            
            pass
        
        if version == 'leopard':
            
            pass
        
        if version == 'snowleopard':
            
            pass

        if version == 'lion':

            process = subprocess.run(
                f'curl -L -o {filePath}/Lion.dmg "https://archive.org/download/install-mac-os-x-lion.app/Install%20Mac%20OS%20X%20Lion.app.zip/Install%20Mac%20OS%20X%20Lion.app%2FContents%2FSharedSupport%2FInstallESD.dmg"',
                shell = True,
                check = True,
                text = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
            )
            
            if process.returncode != 0:

                print(f"Could not download Lion.dmg: {process.stderr}.")

        if version == 'mountainlion':

            pass
        
        if version == 'mavericks':

            pass
        
        if version == 'yosemite':
            
            pass
        
        if version == 'elcapitan':

            pass
        
        if version == 'sierra':
            
            pass
        
        if version == 'highsierra':
            
            pass
        
        if version == 'mojave':
            
            pass
        
        if version == 'catalina':
            
            pass
        
        if version == 'bigsur':
            
            pass
        
        if version == 'monterey':
            
            pass
        
        if version == 'ventura':
            
            pass
        
        if version == 'sonoma':
            
            pass
        
        if version == 'sequoia':
            
            pass
        
        if version == 'tahoe':
            
            pass

    except Exception as e:

        print(f"An error occurred in downloadISO() for {version}-branch: {str(e)}.")

def createISO(version, filePath):

    try:

        if version == 'cheetah':
            
            pass
        
        if version == 'puma':
            
            pass
        
        if version == 'jaguar':
            
            pass
        
        if version == 'panther':
            
            pass
        
        if version == 'tiger':
            
            pass
        
        if version == 'leopard':
            
            pass
        
        if version == 'snowleopard':
            
            pass

        if version == 'lion':

            process = subprocess.run(
                f'hdiutil convert ./Lion.dmg -format UDTO -o ./Lion.cdr',
                shell = True,
                check = True,
                text = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
            )
            
            if process.returncode != 0:

                print(f"Could not convert Lion.dmg to Lion.cdr: {process.stderr}.")
                
            process = subprocess.run(
                f'mv ./Lion.cdr ./Lion.iso',
                shell = True,
                check = True,
                text = True,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
            )
            
            if process.returncode != 0:

                print(f"Could not rename Lion.cdr to Lion.iso: {process.stderr}.")

        if version == 'mountainlion':

            pass
        
        if version == 'mavericks':

            pass
        
        if version == 'yosemite':
            
            pass
        
        if version == 'elcapitan':

            pass
        
        if version == 'sierra':
            
            pass
        
        if version == 'highsierra':
            
            pass
        
        if version == 'mojave':
            
            pass
        
        if version == 'catalina':
            
            pass
        
        if version == 'bigsur':
            
            pass
        
        if version == 'monterey':
            
            pass
        
        if version == 'ventura':
            
            pass
        
        if version == 'sonoma':
            
            pass
        
        if version == 'sequoia':
            
            pass
        
        if version == 'tahoe':
            
            pass

    except Exception as e:

        print(f"An error occurred in downloadISO() for {version}: {str(e)}.")

























if __name__ == '__main__':

    try:

        parser = argparse.ArgumentParser(description = "argparser")
        parser.add_argument(
            "version",
            choices = ["cheetah", "puma", "jaguar", "panther", "tiger", "leopard", "snowleopard", "lion", "mountainlion", "mavericks", "yosemite", "elcapitan", "sierra", "highsierra", "mojave", "catalina", "bigsur", "monterey", "ventura", "sonoma", "sequoia", "tahoe"],
            help = "Which macOS version"
        )
        args = parser.parse_args()
        
        filePath = os.getenv("FILEPATH", None)

        downloadISO(args.version, filePath)
        createISO(args.version, filePath)

    except Exception as e:
        
        print(f'Error occurred: {e}')