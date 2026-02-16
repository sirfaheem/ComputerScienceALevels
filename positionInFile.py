#open a file
fo=open("foo.txt", "r+")
str=fo.read(10);
print("read string is: ",str)
#check current position
position=fo.tell();
print ("current position: ",position
#reposition pointer at the beginning
position=fo.seek(0,0);
str=fo.read(10);
print("again read string is : ",str)
#close opened file
fo.close()
