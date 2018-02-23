''' Sample append to file '''
appendMe = '\nNew information'

appendFile = open('exampleFile.txt','a')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()
