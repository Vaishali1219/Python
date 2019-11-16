from selenium import webdriver
import sys
import chilkat
import bs4
import time
import os

gzip = chilkat.CkGzip()
success = gzip.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(gzip.lastErrorText())
    sys.exit()

file = open('all_links_in_sitemap', 'w')


driver = webdriver.Firefox(executable_path=r'C:\Users\vaish\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
driver.get('https://www.naukri.com/sitemap.xml')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = bs4.BeautifulSoup(res,'xml')

count =1
for url in soup.find_all('loc'):
    tempurl = url.text
    tempstri = '>>>>>>>>>>>>>>    '+str(count)+'  >>>>>>>>>>'+'inside the following link'+tempurl+' <<<<<<<<<<<<<<<<<<<<we have ------------------\n'
    if count > 150:
        break




    file.write(tempstri)



    if tempurl.endswith('l'):



        driver = webdriver.Firefox(executable_path=r'C:\Users\vaish\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
        driver.get(tempurl)
        tempres = driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()
        tempsoup = bs4.BeautifulSoup(tempres,'xml')

        for tempourl in tempsoup.find_all('loc'):
            tempstri = str(count)+' >>>>'+tempourl.text+'\n'
            file.write(tempstri)
    else:


        dir = os.getcwd()

        dir = dir.replace('\\' , '/')
        dir = dir +'/'



        filename = tempurl.split("/")[-1]
        download_dir = dir
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Firefox(executable_path=r'C:\Users\vaish\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
        driver.get(tempurl)
        time.sleep(40)



        res1 = gzip.uncompressFileToString(filename,"utf-8")
        if (success != True):
            print(gzip.lastErrorText())
            sys.exit()




        soup3 = bs4.BeautifulSoup(res1,'xml')


        for url3 in soup3.find_all('loc'):
            tempstri = str(count)+' >>>>'+url3.text+'\n'
            file.write(tempstri)

        driver.quit()

    count+=1


file.close()
print("Done!!")
