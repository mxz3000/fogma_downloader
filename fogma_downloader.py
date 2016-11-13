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
    
    
#get filenames from fogma and format them

for line in f:
	if '"link":' in line:
		fname = line.strip()[9:-2]
		filenames.append(fname)
		
		
#go thru filenames and download the pdfs from fogma

print("downloading pdfs from fogma")

for filename in filenames:
    	full_url = "http://" + urllib2.quote(URL + filename)
    	print(filename)

    	with file(directory + "/" + filename, 'wb') as outfile:
       		response = session.get(full_url, headers=HEADERS)
       		if not response.ok:
      			break
        	outfile.write(response.content)
        	
f.close()


