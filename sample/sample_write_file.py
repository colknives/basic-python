''' Sample write to file '''
text = 'Sample Text to Save \nnew line!'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()
