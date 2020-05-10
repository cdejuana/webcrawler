CRAWLER ABOUT UEFA CHAMPIONS LEAGUE
Pequeños pollos.
---------------------

INTRODUCTION 🚀
-----
The project consists of developing a web crawler, it is a program or automated script to extract, store, analyze and present the information.

For doing the project we use:
    * Python coding
    * Selenium -> extract the information of the web
    * MongoDB -> store all information
    * Pandas library -> extract information from MongoDB
    * Jupyter Notebook -> present the information
    * Matplotlib library -> doing the graphs


REQUIREMENTS 📋
-----
This crawler can run in all operative systems.
In order to run this crawler you must have:
    * Python:
        -Windows:
            Dowload the installer in the next page:
                https://www.python.org/downloads/windows/
        -Linux
            You will probably have python installed.
            To check if you have it use:
                python --version
            If you don't have it use:
                sudo apt-get update
                sudo apt-get install python3.6
        -MacOS
            The best way to install python is to install Homebrew
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
            Once Homebrew has finished installing
                brew install python3
                
    * MongoDB:
        -Windows, Linux or MacOS 
            Go to the following page and download the installer:
                https://www.mongodb.com/download-center/community
            If you want, you can install Mongo Compass
                https://www.mongodb.com/download-center/compass

    * Web Driver
      To make the code work it is necessary to install a web driver, which depends on your browser and the version it has.
      It is most recommended to use google chrome or firefox.
      Almost everyone in the team who has developed this code have used Chrome, so it is the best browser to run this code on.
        - Google Chrome
            https://chromedriver.chromium.org/downloads
            Remember to dowload the web driver according to your version and put it in the same project folder.
            
        - Mozilla Firefox
            You don't need to dowload anything.    

    * Chromium (optional)
        - Window
            https://chromium.woolyss.com/download/es/
                
        - Linux
            sudo apt upgrade
            sudo apt install chromium-browser
            
        - MacOs
            https://chromium.woolyss.com/download/es/#mac
                    
For the following libraries we use python pip, for installing this you can use in your command console
  python get-pip.py

    * Jupyter NoteBook
      You can use Jupyter NoteBook from Anaconda programm.
      If you only want to install jupyter, you can use: 
        pip install jupyterlab
        pip install notebook
    
    * Selenium:
        pip install selenium
    
    * Pandas
        pip install pandas
        
    * Matplotlib
        pip install matplotlib
    
        
In order to install Anaconda you can dowload the installer from the following page:
    https://www.anaconda.com/products/individual#Downloads

If you use Anaconda, remember to add 'conda' before the previous commands. Example: conda pip intall pandas.
            

INSTALLATION 🔧
-----
LINK -> https://bitbucket.org/onetec/pacman2/src/master/
The previous link leads to the repository of the entire project, not just the crawler.

If you prefer to skip all the steps until step 8, you can use the file players.json, that already has all the information collected, 
only you can do the step 6 and...
    - Compass
      Click in ADD DATA and Import File to select json file.
      
      -Commands
       Write 'mongoimport --db=uefa --collection=players --file=players.json'
    
To run the crawler and collect the data you must:

    1. Dowload the repository 
    
    2. Open your Jupyter Notebook and navigate to the proyect folder
    
    3. Access Phase 2 folder
    
    4. Dowload the Web Driver if you are going to use Google Chrome 
        4.1. Include chromedriver.exe in your project folder
        4.2. If you are going to use Firefox, change line 11 to driver = webdriver.Firefox()

    5. Open uefa-statistics-final-V2.ipynb file with Jupyter Notebook
    
    6. For the crawler to work perfectly you must first create a database in MongoDB
        - Mongo Compass
            Click where it says "Create Database"
            6.1. DataBase Name = uefa
            6.2. Collection Name = players

        - Commands
            6.1. Write "use uefa" -> this command creates a DataBase whose name is uefa
            6.2. Write "db.player.insert({})" -> this other comand creates a collection and in this case it doesn't insert anything
            6.3. To verify that the database has been created correctly write "show dbs"

    7. Run the file, it will automatically show a browser page in the UEFA website, at this moment the crawler has started working. If you use another name in the step before, 
	remember to change line 223 and 224. 

        This crawler can take approximately 4 hours.
        
        ATENTION! WHILE THE CRAWLER IS RUNNING IT'S VERY IMPORTANT THAT THE COMPUTER DOESN'T GET TURNED OFF OR SUSPENDED.
        If what is mentioned previosly happens, then it will be necessary to restart the crawler.

    8. When the crawler has finished you will be able to see the data of the players on the database
        -Mongo Compass
          If you had compass open, close it and reopen it. You must have 2065 Documents.
          When you click in collection players you can see a list with first 20 players. In the right side you can view two arrows which allow you to see more.
        
        -Commands
          Write "use uefa" and later "db.players.find().pretty()" then you can view the 20 first players and you should write to continue seeing more.


Once you have all the data, to execute the files with the graphics you must:
    
    1. Enter into graph folder 
        1.1. In graph_red_cards.ipynb -> you can see the red cards graph of all teams.
        1.2. In graph_yellow_cards.ipynb -> you can see the yellow cards graph of all teams.
        1.3. In bargraph_best_teams.ipynb -> you can see the 10 teams that have scored the most goals.

Maintainers✒️
-----
    
    * Carlos de Juana (Spain)
    * Paula Blázquez (Spain)
    * Jan Kudláček (Czech Republic)
    * Dominik Benda (Czech Republic)
    * Tova Ohlson (Sweden)

SUPERVISION👩‍🏫
-----
    
    * Nuria García - Grupo OneTec (Madrid, Spain)
    * David Rodríguez - Grupo OneTec (Madrid, Spain)
    * Juan Antonio Mangudo - Grupo OneTec (Madrid, Spain)
    * IES. El Lago (Madrid, Spain)
    