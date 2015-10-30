'''
Created on 2013-11-6

@author: Yang Jiao
'''
import urllib
from bs4 import BeautifulSoup

def getURLTitle(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """get title from given url, return the title as a string"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    return str(soup.title.get_text())

def getURLDoc(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """print the html doc from given url, formatted in BeautifulSoup"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    return (soup.prettify())
    
def getURLheader(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """get header from given url, return a list of string in order"""
    header_list = []
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    for header in soup.find_all('a', href = True,  attrs = { 'class' : 'wikilink'}):
        header_list.append(str(header.get_text()))
    return header_list

def getURLheaderAndHref(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """get header and href from given url, return a list of tuple which contains specific header and href in order"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    headerHref_list = []
    for link in soup.find_all('a', href = True,  attrs = { 'class' : 'wikilink' }):
        headerHref_list.append((link.get_text(), link['href']))
    return headerHref_list

def getURLSubtitle(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """subtitle is the bold line in the content of given url. 
    get subtitle from given url, return a list of string"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    content = soup.find('div',attrs = {'id' : 'wikitext'})
    subtitle = content.select('p > strong')
    subtitle_list = [str(subt1.next) for subt1 in subtitle]
    return subtitle_list

def getURLSubcontent(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """subcontent is the indented lines in the content.
    get subcontent from given url, return a list of string"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    content = soup.find('div',attrs = {'id' : 'wikitext'})
    subcontent = content.select('ul > li')
    subcontent_list = [str(subc1.get_text("", strip = True)) for subc1 in subcontent]
    return subcontent_list
    
def getURLcontent(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main"):
    """get content from given url, return a list of string"""
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    content = soup.find('div',attrs = {'id' : 'wikitext'})
    needed_tag = content.find_all(["p", "li"], attrs = {'class' : None})
    without_replace_newline = [str(item.get_text()).strip() for item in needed_tag]
    replaced_content = []
    for item in without_replace_newline:
        new_item = item.replace("\n", " ")
        replaced_content.append (new_item)
    return  replaced_content

def getFormattedURL(url = "http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main", stringOrList = 0):
    """get formatted title, header, content from given url, return a list or a string"""
    urlString = ""
    urlList = []
    title = "                    " + getURLTitle(url) + "                    "
    header = "|".join(getURLheader(url))
    subtitle = getURLSubtitle(url)
    subcontent = getURLSubcontent(url)
    urlList.append(title)
    urlList.append("\n  " + header + "\n")
    for item in getURLcontent(url):
        if item in subtitle:
            urlList.append("\n\n " + item + "\n----------------------------------------------\n")
        elif item in subcontent:
            urlList.append("    " + item)
        else:
            urlList.append(" " + item)
    urlString = "\n".join(urlList)
    if stringOrList:
        return urlList
    else:
        return urlString


if __name__ == "__main__":
    print (getFormattedURL("http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main", 0))
    header_href = getURLheaderAndHref()
    for header, href in header_href[1: 29]:
        print ("\n\n" + header + "\n===================================================================================\n")
        print (getFormattedURL(href, 0))
        print ("\n===================================================================================\n")
        
    with open ('1weekproject.txt', 'w') as f:
        for lists in getFormattedURL("http://www.davedraper.com/pmwiki/pmwiki.php/Main/Main", 1):
            f.write(lists)
        header_href = getURLheaderAndHref()
        for header, href in header_href[1: 29]:
            f.write ("\n\n" + header + "\n===================================================================================\n")
            for contentList in (getFormattedURL(href, 1)):
                f.write(contentList)
            f.write ("\n===================================================================================\n")
        
        

          