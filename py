import requests
from selenium import webdriver
from collections import OrderedDict
import json
import numpy as np
#import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from git import Repo
import autoit
from selenium.webdriver.remote.webelement import WebElement
import os.path
import time
from operator import itemgetter


JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []
    
    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))
    
    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

WebElement.drop_files = drop_files




driver = webdriver.Chrome('chromedriver')

link = "https://www.worldometers.info/coronavirus/"
f = requests.get(link)
#print(f.text)

x = f.text
#str.find(sub,start,end)
pocetak = f.text.find('<table')
kraj = f.text.find('</table>')
#print(pocetak)
#print(kraj);

tabela = (x[pocetak:kraj+20])
#print(tabela)
#test = "testing"

f = open('htmlcorona.txt','w')
f.write(tabela)  # python will convert \n to os.linesep
f.close()


driver.get("https://www.convertjson.com/html-table-to-json.htm")
driver.find_element_by_id("f1").send_keys(r"C:\Users\PC\htmlcorona.txt")

jsonn = driver.find_element_by_id("txta").get_attribute("value")
jsonn = jsonn.replace('\\n','').replace("Country,Other", "Country").replace("Serious,Critical","Serious").replace("null","0").replace('""','"0"')


#print(sorted(jsonn, key=lambda d: d["Country"]))

#jsonnn = sorted(jsonn, key=itemgetter('Country')) 











f = open('jsonunsorted.txt','w')
f.write(jsonn)
f.close()


####################
#driver.get("https://codeshack.io/json-sorter/")


#dropzone = driver.find_element_by_class_name("CodeMirror-scroll")

# drop a single file
#dropzone.drop_files("C:\\Users\PC\jsonunsorted.txt")
#driver.find_element_by_id('submit-file').click()


#driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div[1]/select/option[2]").click()
#time.sleep(3)
#jsonn = driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[3]/div[6]").text
#print(jsonn)


#/html/body/div[3]/main/div[2]/div[3]/div[3]/div[6]
#f = open('jsonsorted.txt','w')
#f.write(jsonn)
#f.close()

######################



#print(jsonn)



driver.get("https://github.com/urosmlade/korona/blob/master/test")
driver.find_element_by_link_text('Sign in').click()
driver.find_element_by_id("login_field").send_keys("mladenko96@gmail.com")
driver.find_element_by_id("password").send_keys("YiHaoUrOsMlAdEnOvIC29041996")
driver.find_element_by_name('commit').click()

driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div[3]/div[1]/div[2]/div[2]/form[1]/button").click()

#driver.find_element_by_class_name("CodeMirror-scroll").click().send_keys(Keys.CONTROL + "a");
#driver.find_element_by_class_name("CodeMirror-scroll").send_keys(Keys.DELETE);
driver.find_element_by_class_name("CodeMirror-scroll").clear();






dropzone = driver.find_element_by_class_name("CodeMirror-scroll")

# drop a single file
dropzone.drop_files("C:\\Users\PC\jsonunsorted.txt")
driver.find_element_by_id('submit-file').click()



#f = open('jsonunsorted.txt','r').read()
#driver.find_element_by_class_name('CodeMirror-code').send_keys(f)
#f.close()



#driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div[3]/div[1]/div[2]/div[2]/form[1]/button").send_keys(r"C:\Users\PC\jsonunsorted.txt")






#Country,\nOther
#driver.get("https://codeshack.io/json-sorter/")
#driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/a[1]").send_keys(r"C:\Users\PC\jsonunsorted.txt")
#print('mrs')

