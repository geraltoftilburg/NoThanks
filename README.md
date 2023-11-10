To run a competition, start the file Take5.py. If you do that from the command line, you can give command line parameters:
python –u NoThanks.py 10000 aifile1 aifile2 ...

The first command line parameter (10000 in the example above) is the number of games that should be played in the competition. After that you can specify a list of python files that contain AIs that you want to enter into the competition. If you do not specify any command line parameters, the number of games that will be played is 1000, and the AIs are loaded from the file NoThanksBeginners.py. If you want to run the competition from the editor, you can (temporarily) change the values for DEFAULTLENGTH and DEFAULTAIS at the top of the NoThanks.py file. 

DEFAULTLENGTH indicates how many games you want to run, and DEFAULTAIS is a list of all the AI files in the competition. If you change it, for
instance, to ['NoThanksBeginners','MyAI'], it will load all the AIs from NoThanksBeginners.py and from MyAI.py. 

At the end of the competition, the game prints an ordered list of all the AIs that entered, with a number that indicates in how many games they were, and their average score. The lower the average score, the better it is.





