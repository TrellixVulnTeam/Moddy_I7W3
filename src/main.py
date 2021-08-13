####Start Date: 2021.08.02
####Author: Lainey 'Lain' Tubbs
####Usage: This is a commandline mod manager for Bethesda games called 'Moddy'. It is mesnt for linux and other 
#### unix based operating systems. 


from pathlib import Path
from pyunpack import Archive
import os, sys, shutil, subprocess, lzma, py7zr


modDirectory = ''
gameDirectory = ''
downloadDirectory = ''
mod = ''
fileName = ''
settingYN = ''
homeBase = os.getcwd()



class directions:                                                                                                               
    def __init__(self, modDirectory, gameDirectory, downloadDirectory, mod):                                                    
        self.modDirectory = modDirectory                                                                                        
        self.gameDirectory = gameDirectory                                                                                      
        self.downloadDirectory = downloadDirectory                                                                              
        self.mod = mod                                                                                                          
                                                                                                                                   
   

    def makemodDirect(self):
        if os.path.isdir(modDirectory):
            print(f"{modDirectory} already exists!")
            print(f"Setting mod directory to {modDirectory}")
            os.chdir(modDirectory)
        elif os.path.isdir(modDirectory) == False:
            print(f"Creating {modDirectory}")
            os.mkdir(modDirectory)
            print(modDirectory, "has been created!")

        else:
            print("Something went wrong")


    def setGameDirectory(self):
        gameDirectory = input("Enter in the game directory: ")
        if os.path.isdir(gameDirectory):
            print(f"{gameDirectory} exists!!")
            print(os.system("ls | grep .exe"))
        elif os.path.isdir(gameDirectory) == False:
            print("This game directory doesn't exist")
            gameDirectory = input("Enter in the game directory: ")
            while os.isdir(gameDirectory) == False :
                gameDirectory = input("Enter in the game directory: ")
        else:
            print("Something went wrong")




    def setDownloadDirectory(self):
        if os.path.isdir(downloadDirectory):
            print(downloadDirectory, "exists!!")
        else:
            print(downloadDirectory, "doesn't exist!!")
            downloadDirectory = input("Please enter in your downloads directory: ")





        
    def loadMods(self, modDirectory, downloadDirectory,gameDirectory):
        mods = []
        os.chdir(modDirectory)
         #os.chdir(modDirectory)


        modpackerlist = input("Please list the names of the files you'd like to load up. Please separate them with spaces: ")
        mods = str(modpackerlist).split(" ")
        for mod in mods:
            print(mod)
            os.chdir(modDirectory)
            while os.path.isfile(mod) == False:
                print(f"The mod {mod} doesn't exist")
                mod = input("Please re-enter the name of the file!")
    	    # mods.append(mod)
    	    #print(f"Now loading {0}", mod)
            print(f"Now loading {mod}")
            #mods.append(mod)
            if os.path.isdir(modDirectory):
                os.chdir(modDirectory)
                changeName = str(input("Would you like to rename this mod?(y or n)"))
                print(changeName)
                if changeName == 'y':
                    modName = input("Enter the new mod name:")
                    print(modName)
                    os.system(f"mv {mod} {modName}")
                elif changeName == 'n':
                    modName = mod
                    print(modName)
                else:
                    break
            else:
                sys.exit("Mod directory doesn't exist!!")
            # with (Archive(mod).extractall(f'{str(gameDirectory)}/Data')) as modData:
            modData = Archive(mod)
            modUnpack = modData.extractall(f'{str(gameDirectory)}/Data')
            # print(modData)
            # os.path.join(modData, f'{gameDirectory}/Data')

            os.chdir(f'{gameDirectory}/Data/')
            directoriesInData = os.listdir(f'{gameDirectory}/Data')
            #print(directoriesInData)
            dirrs = []
            for dirr in modDirectory:
                dirrs += dirr
            for dataDirectory in directoriesInData:
                if dataDirectory == 'Data':
                    os.system(f'cd {gameDirectory}/Data/Data; mv * {gameDirectory}/Data/')
                    # os.path.join(dataDirectory, f'{gameDirectory}/Data')
                    os.system(f'rm -r {gameDirectory}/Data/Data')
                elif dataDirectory == dirr:
                    os.path.join(dataDirectory,dirr)
                else:
                    print(f"None of the files for the mod {mod} are the same as any files in the game directory")
                    pass
            print(f"The mod {modName} has been loaded!")

    def unpackModFolder(self, modDirectory, downloadDirectory, gameDirectory):
        os.chdir(modDirectory)
        for mod in os.path.listdir(modDirectory):
            print(mod)
            while os.path.isfile(mod):
                print(f"Now loading {mod}!!")
                modData = Archive(mod)
                with modData.extractall(f'{str(gameDirectory)}/Data') as modUnpack:
                    modUnpack
                    for modFile in modUnpack:
                        modFilesLists += modFile


            directoriesInData = os.listdir(f'{gameDirectory}/Data')
            for directory in directoriesInData:
                if directory == 'Data':
                    os.system(f'cd {gameDirectory}/Data/Data; mv * {gameDirectory}/Data/')
                    # os.path.join(dataDirectory, f'{gameDirectory}/Data')
                    os.system(f'rm -r {gameDirectory}/Data/Data')
                elif directory == modFile:
                    os.path.join(directory, modFile)
                else:
                    print(f"{modFile} doesn't exist in {gameDirectory}/Data ! Nothing will be overwritten")
                while directory == modFile:
                    pass 









    




          


    def modList(self, modDirectory):
        os.listdir(modDirectory)

    def quit(self):
        quit = input("Would you like to quit?")
        while quit == 'y' or 'Y' or 'yes' or 'Yes':
            sys.exit("Exiting the program")
        pass




if __name__ == "__main__":
    intialAnswer = (input("Well hello there, would you like to mod a game [y/n?]"))
    if intialAnswer == 'y':
        direct = directions(modDirectory, gameDirectory, downloadDirectory, mod)
        # direct.readSettings(modDirectory, gameDirectory, downloadDirectory)
        settingYN = input(str('Would you like to load a settings file?: [y/n]'))
        # while settingYN != 'y' or 'n':
        #     settingYN = input(str('Would you like to load a settings file?: [y/n]'))
        if settingYN == 'y':
            fileName = input("Enter in the name of the settings file you made: ")
            while os.path.isfile(fileName) == False:
                print("Oh No! Your file doesn't exist!")
                fileName = input("Enter in the name of tthe settinfs file you made: ")
            file = open(fileName , 'r')
           
            modDirectory      = str(file.readline().strip("\n"))
            print(modDirectory)
            
            gameDirectory     = str (file.readline().strip("\n"))
           
            gameName          = str(file.readline().strip("\n"))
            
            downloadDirectory = str(file.readline().strip("\n"))
            print("Mod Directory: ", modDirectory)
            print("Game Directory: ", gameDirectory)
            print("Game Name: ", gameName)
            print("Download Directory: ", downloadDirectory)
        elif settingYN == 'n':
            fileName = input("What would you like to call your settings file (needs to be a .txt file): ")
            while fileName == '':
                 fileName = input("What would you like to call your settings file (needs to be a .txt file): ")
            print("Your settings file is gonna be called:", fileName)
            file = open(fileName, 'w')
            #file = write(fileName, 'rw')
            modDirectory = input("Please enter your mod directory:")
            while isinstance(modDirectory,int) == True or isinstance(modDirectory,float) == True:
                modDirectory = input("Please enter your mod directory:")
            direct.makemodDirect()
            # with open(fileName, 'a') as writeFile:
            #     writeFile.write(modDirectory)
            file.write(modDirectory)
            file.write("\n")
            print(modDirectory)
            # gameDirectory = input("Enter in the game directory: ")
            #print(gameDirectory)
            direct.setGameDirectory()
            print(gameDirectory)
            # with open(fileName, 'a') as writeFile:
            #     writeFile.write(gameDirectory)
            file.write(gameDirectory)
            file.write("\n")
            gameName = input("Enter in the name of your game: ")
            while gameName == '':
                gameName = input("Enter in the name of your game: ")
            # with open(fileName, 'a') as writeFile:
            #     writeFile.write(gameName)
            file.write(gameName)
            file.write("\n")
            downloadDirectory = input("Please enter in your downloads directory: ")
            #direct.setDownloadDirectory()""
            # with open(fileName, 'a') as writeFile:
            #     writeFile.write(downloadDirectory)
            file.write(downloadDirectory)
            file.write("\n")
            print(downloadDirectory)
            file.close()
            os.chdir(homeBase)
            shutil.copyfile(fileName, modDirectory)
            #fileRead = open(fileName, 'r')
            file = open(fileName, 'r')
            file.readlines()
            print("Mod Directory: ", modDirectory)
            print("Game Directory: ", gameDirectory)
            print("Game Name: ", gameName)
            print("Download Directory: ", downloadDirectory)

        else:
             sys.exit("Invalid input, closing program")
        modDirectory
        gameDirectory
        downloadDirectory
        listMods = input("Would you like to list your current mods associated with this game: [y/n]")
        if listMods == 'y':
            print(os.listdir(modDirectory))
        elif listMods =='n' :
            pass
        else:
            direct.quit()
        chooseLoadMods = input("Do you want to load up some mods: [y/n]")
        if chooseLoadMods == 'y':
            print("Below, you will list all of the mods you would like to load.")
            direct.loadMods(modDirectory, downloadDirectory,gameDirectory)
        elif chooseLoadMods == 'n':
           pass
        else:
            sys.exit("Invalid input, exiting program")
        # else:
        #     direct.quit()

        nextAnswer = input("Please, let me know what you wanna do next: Load mods [l], Load from Folder [lf], list mods [list], or exit")
        while  nextAnswer == Null:
           nextAnswer = input("Please, let me know what you wanna do next: Load mods [l], Load from Folder [lf], list mods [list], or exit")
        if nextAnswer == 'l':
           direct.loadMods(modDirectory, downloadDirectory,gameDirectory)
        elif nextAnswer == 'lf':
            direct.unpackModFolder(modDirectory, downloadDirectory, gameDirectory)
        elif nextAnswer == 'list':
            print(os.listdir(modDirectory))
        elif nextAnswer == 'q':
            sys.exit("Quitting now")
        else:
            pass




        # print('')
        # print('')
        # print('')
        # print('')
        # listMods = input("Would you like to list your current mods associated with this game: [y/n]")
        # if listMods == 'y':
        #     print(os.listdir(modDirectory))
        # elif listMods =='n' :
        #     chooseLoadMods = input("Do you want to load up some mods: [y/n]")
        #     if chooseLoadMods == 'y':
        #         print("Below, you will list all of the mods you would like to load.")
        #         direct.loadMods(modDirectory, downloadDirectory,gameDirectory)
        #     elif chooseLoadMods == 'n':
        #         pass
        #     else:

        #         sys.exit("Invalid input, exiting program")


    else:
        sys.exit("You don't wanna do nothing so...bye!")




    				

    				








          		

