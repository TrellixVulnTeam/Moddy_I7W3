from pathlib import Path
import os, argparse 


parser = argparse.ArgumentParser(description='An open source mod organizer in the CLI!')
parser.add_argument('-m',  help='set your Mod Directory')
parser.add_argument('-M',   help='make and set your mod directory')
parser.add_argument('-g',   help='set your game directory')
parser.add_argument('-d',  help='Set your download directory')
parser.add_argument('-u',  help='List the mods you would like to load')
parser.add_argument('-l', help=' lists mods in the mod directory')
args = vars(parser.parse_args())
class directions:                                                                                                               
    def __init__(self, modDirectory, gameDirectory, downloadDirectory, mod):                                                    
        self.modDirectory = modDirectory                                                                                        
        self.gameDirectory = gameDirectory                                                                                      
        self.downloadDirectory = downloadDirectory                                                                              
        self.mod = mod                                                                                                          
                                                                                                                                   
    def setmodDirect(self, args):                                                                                                     
                                                                                                               
        if os.path.isdir(args['-m']):
            try:
            	modDirectory = string(args['-m'])
            	os.chdir(modDirectory)
            except:  print("This doesn't exist")
            finally: print(f"Your modDirectory is {0}",modDirectory)
       	
       			


        else:
          	print("Use '-M' to create the directory")


    def makemodDirect(self,args):
        if os.path.isdir(args['-M']):
            print(f"{args['-M']} Already exists!")
            print(f"Setting mod directory to {0}", args['-M'])
            modDirectory = args['-M']
            os.chdir(modDirectory)
        elif os.path.isdidr(args['-M']) == False:
            print(f"Creating {0}", modDirectory)
            os.mkdir(modDirectory)
            print(modDirectory, "has been created!")

        else:
            print("Something went wrong")


    def setGameDirectory(self, args):
        gameDirectory = args['-g']

    def setDownloadDirectory(self, args):
        downloadDirectory = args['-d']

    def loadMods(self, args, modDirectory, downloadDirectory, gameDirectory):
        mods = []
        os.chdir(downloadDirectory)
        for mod in args['-mod']:
            mods += mod
            print(f"Now loading {0}", mod)
            if os.path.isdir(downloadDirectoryDirectory):
                os.chdir(downloadDirectory)
                changeName = string(input("Would you like to rename this mod?(y or n)"))
                print(changeName)
                if changeName == 'y' or 'Y':
                    modName = input("Enter the new mod name:")
                    print(modName)
                    os.mkdir(modName)
                elif changeName == 'n' or 'N':
                    modName = mod
                    print(modName)
                    os.mkdir(modName)
                else:
                    print("Something went wrong!?")
            else:
                break
            os.system(f'mv {mod} {modDirectory}/ ')
            os.chdir(modDirectoru)
            os.link(f'{mod} {gameDirectory}/data/{mod}')
            print(f"mod {0} has been loaded",modName)



        
    # def loadMods(self, args, modDirectory, downloadDirectory,gameDirectory):
    # 	mods = []
    # 	os.chdir(downloadDirectory)
    # 	for mod in args['-mod']:
    # 		mods += mod
    # 		print(f"Now loading {0}", mod)
    # 		if os.path.isdir(downloadDirectoryDirectory):
    # 			os.chdir(downloadDirectory)
    # 			changeName = string(input("Would you like to rename this mod?(y or n)"))
    # 			print(changeName)
    # 			if changeName == 'y' or 'Y':
    # 				modName = input("Enter the new mod name:")
    # 				print(modName)
    # 				os.mkdir(modName)
    # 			elif changeName == 'n' or 'N':
    # 				modName = mod
    # 				print(modName)
    # 				os.mkdir(modName)
    # 			else:
    # 				print("Something went wrong!?")
    # 		else:
    # 			break
    # 		os.system(f'mv {mod} {modDirectory}/ ')
    #         os.chdir(modDirectoru)
    #         os.link(f'{mod} {gameDirectory}/data/{mod}')
    # 		print(f"mod {0} has been loaded",modName)

    def modList(self, modDirectory):
        os.listdir(modDirectory)



    				

    				




if __name__ == "__main__":
 for arg in args:
    directions.makemodDirect()
    directions.setmodDirect(args)
    directions.setGameDirectory(args)
    directions.setDownloadDirectory(args)
    directions.loadMods( args, modDirectory, downloadDirectory, gameDirectory)

        # while arg = args[-M]:
        #      directions.makemodDirect()
        # while arg = args[-m]:
        #     directions.setmodDirect()
        # while arg = args[-g]:
        #     directions.setGameDirectory()
        # while arg = args[-d]:
        #     directions.setDownloadDirectory()
        # while arg = args[-mod]:
        #     directions.loadMods()







          		

