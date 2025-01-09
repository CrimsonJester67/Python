#Accept a file name from user and print the extension 
fname=input('enter the file name:')
exten=fname.split('.')
print('extension is:',exten[-1])
