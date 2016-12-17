import requests
import urllib2
import os

HEADERS = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
URL = "www.fogma.co.uk/exampapers/"
f = urllib2.urlopen("http://www.fogma.co.uk/exam_papers/")
session = requests.session()
filenames = []

#check if fogma dir to store pdfs exists, create it if it does not

directory = "fogma"

if not os.path.exists(directory):
    os.makedirs(directory)
    
    
#get html from fogma and extract filenames
#build folder path for each filename 
curdir = ""
curclass = ""
dirs = []

for line in f:
	if ' Year": [{' in line:
		curdir = line.strip()[1:-5]
		if not os.path.exists(directory + '/' + curdir):
			os.makedirs(directory + '/' + curdir)
		
	if '"title": ' in line:
		curclass = line.strip()[10:-2]
		if not os.path.exists(directory + '/' + curdir + '/' + curclass):
			os.makedirs(directory + '/' + curdir + '/' + curclass)
		
	if '"link":' in line:
		fname = line.strip()[9:-2]
		filenames.append(fname)
		dirs.append(directory + '/' + curdir + '/' + curclass + '/')
		
		
#go thru filenames and download the pdfs from fogma

print("downloading pdfs from fogma")

for filename, path in zip(filenames,dirs):
    	full_url = "http://" + urllib2.quote(URL + filename)
    	print(filename)

    	with file(path + filename, 'wb') as outfile:
       		response = session.get(full_url, headers=HEADERS)
       		if not response.ok:
      			break
        	outfile.write(response.content)
        	
f.close()


