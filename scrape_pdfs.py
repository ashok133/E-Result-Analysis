# Code below will download all the PDFs from Mumbai University's page fr distance learning. 
# The code should be modified to download PDF from result website. Change the url at line 21 and appropriately strip link names at lines 51 and 52
# Conversion from PDF to Excel is done using PDFTables API, in separate code file

# mechanize is the library used here to crawl and scrape the source website
import mechanize
# urllib2 is the library used to download the PDF binary data from links
import urllib2
from time import sleep

# Simulating a browser using mechanize
br = mechanize.Browser()

# In case the user is required to login to a form before viewing results, refer http://stackoverflow.com/questions/14722309/filling-up-a-login-form-using-mechanize-python

# Some global structures 
i = 0
urls = []

# Opening the website using simulated browser 'br'.
# It creates a 'source.html' in the same directory before crawling the website for PDFs
br.open("http://mu.ac.in/portal/distance-open-learning/b-a-study-material/")

# Open the source HTML with pointer 'f'
f=open("source.html","w")
# Write the HTML source code of the website into our file
f.write(br.response().read()) 

# A list of file types to be scraped from the website, here only PDFs. 
# Additional files such as .txt and .zip can be downloaded as well. 
# Just append the extensions to the list
filetypes=[".pdf"] #you will need to do some kind of pattern matching on your files

# A list to store the urls of scraped PDF 
myfiles=[]

# The scraping magic begins. 

# For every link on the website (identified using 'href' tag in HTML)
for l in br.links():
    # For the link containing file types defined in 'filetypes' list on line 26 
    for t in filetypes:
        # If this link has the file extension we want i.e. if it is a PDF, then do the following
        if t in str(l):
            
            # Append the link of PDF into the list 'myfiles' 
            myfiles.append(l)
            
            #The link of PDF also includes other fields such as base url. We need to strip the link to get exact name of PDF. 
            # This is what happens when we click on a link and the PDF opens in a new window. 
            # We need the url that appears in the address bar of that new window.
            part1 = str(l).split(', url=\'',1)[1] 
            part2 = part1.rsplit('\', text',1)[0]

            # Add the url to 'urls' list
            urls.append(str(part2))

            # Storing all the urls retrieved in a separate text file named 'list_of_pdfs.txt'
            with open("list_of_pdfs.txt","a") as fp:
                fp.write(str(part2)+"\n")

# For debugging, ignore
print urls

def main():
    for l in urls:
        #part1 = str(l).split(', url=\'',1)[1] 
        #part2 = part1.rsplit('\', text',1)[0]
        download_file(str(l))

def download_file(download_url):
    global i
    i+=1
    # Downloading binary data of the PDF and storing it in 'response'
    response = urllib2.urlopen(download_url)
    
    # Opening a blank PDF
    file = open("PDF_no."+str(i)+".pdf", 'wb')
    
    # Writing the binary data into newly created PDF
    file.write(response.read())
    file.close()
    print ("Completed downloading PDF_no."+str(i))

'''
Ignore the block, used to debug link downloads

def downloadlink(l):
    f=open(l.text,"w") 
    br.click_link(l)
    f.write(br.response().read())
    print l.text," has been downloaded"
'''

if __name__ == "__main__":
    main()
