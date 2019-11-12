import os
#'Note-Edit the directory however you'd like'







# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)


Batch=input('enter batch')
RollNumber=input('enter roll num')


user=input('Enter the username of your Logged in windows account')
# define the name of the directory to be created
path = "C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)









try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)


path = os.getcwd()
print ("The current working directory is %s" % path)
i=1
print('List of files available are \n')
for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):
    print(filename)

for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):

    dst = 'C:/Users/{}/Desktop/{}_{}/Project Files/.format(user,Batch,RollNumber)'+"Exp " + str(i)+'_'+RollNumber+'.pdf'
    src = 'C:/Users/{}/Desktop/{}_{}/Project Files/.format(user,Batch,RollNumber)'+ filename

    os.rename(src, dst)
    i+=1
print('New List- \n')
for filename in os.listdir("C:/Users/{}/Desktop/{}_{}/Project Files".format(user,Batch,RollNumber)):
    print(filename)
