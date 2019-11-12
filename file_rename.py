import os
import sys
#Note-Edit the directory however you'd like




Batch = input('Enter your batch')
RollNumber = input('Enter your roll number')

user = input('Enter the username of your Logged in windows account')
def create():

    # detect the current working directory and print it
    path = os.getcwd()
    print ("The current working directory is %s" % path)




    # define the name of the directory to be created
    path = "C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)

    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)

def renamefiles():

    i=1
    print('List of files available are \n')
    for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):
        print(filename)

    for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):

        dst = 'C:/Users/{}/Desktop/{}_{}/Project Files/'.format(user,Batch,RollNumber) +"Exp " + str(i)+'_'+RollNumber+'.pdf'
        src = 'C:/Users/{}/Desktop/{}_{}/Project Files/'.format(user,Batch,RollNumber) + filename

        os.rename(src, dst)
        i+=1
    print('New List- \n')
    for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):
        print(filename)


while(1):
    x=int(input('''Option-1-Create folder with subfolder(s)\nOption-2-Rename files (once added to the created directory)\nOption-3-Exit\n'''))

    if x==2:
        renamefiles()
    elif x==1:
        create()
    else:
        sys.exit()
