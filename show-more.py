import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os

def CommentList(number_list,url):
    commentList=[]
    numberdic={}
    for number in number_list:
        url=url+number
        print(url)
        response=requests.get(url).text
        soup = BeautifulSoup(response,"html.parser")
        for comment in soup.find_all('div', class_='ai-comment-text'):
            # print(comment.get_text())
            commentList.append(comment.get_text())
            # print('\n')
        # print("number : ",number,"\t Comments : \t :",commentList)
        numberdic[number]=commentList
        commentList=[]
        url='https://www.telguarder.com/us/number/'
    return numberdic
def getStatus(number_list,url):
    StatusList=[]
    numberdic={}
    for number in number_list:
        url=url+number
        print(url)
        response=requests.get(url).text
        soup = BeautifulSoup(response,"html.parser")
        for status in soup.find_all('span', class_='ai-spam-reason ai-sr-telephone-seller'):
            # print(comment.get_text())
            StatusList.append(status.get_text())
            # print('\n')
        print("number : ",number,"\t StatusList : \t :",StatusList)
        numberdic[number]=StatusList
        StatusList=[]
        url='https://www.telguarder.com/us/number/'
    return numberdic
def numberList(driver,url,PAGES):
    number_list=[]
    status_list=[]
    driver.get(url)
    p=0
    driver.find_element_by_xpath("//*[@id='didomi-notice-agree-button']").click()
    for i in range(0,PAGES):
        driver.find_element_by_xpath("//*[@class='ai-button ai-button-rounded']").click()
        driver.implicitly_wait(30)
        print("Page No: ",i)
        listt=driver.find_elements_by_xpath("//td[@class='va']")
        print(listt)
        # for a in driver.find_elements_by_xpath("//td[@class='va']"):
        #     mynumbers=list(driver.find_elements_by_xpath("//td[@class='va']").text)
        #     print("Number: ",mynumbers[p])
        #     number_list.append(a.text)
        #     #print(a.text)
        #     p=p+1
        # for s in driver.find_elements_by_xpath("//*[@class='ai-spam-reason ']"):
        #     status_list.append(s.text)
        #     print(s.text)
    return number_list
def speedNumberList(driver,url,PAGES):
    driver.get(url)
    driver.find_element_by_xpath("//*[@id='didomi-notice-agree-button']").click()
    for i in range(0,PAGES):
        driver.find_element_by_xpath("//*[@class='ai-button ai-button-rounded']").click()
        driver.implicitly_wait(30)
        print("Page No: ",i)
        listt=driver.find_elements_by_xpath("//td[@class='va']")
    return listt
listOfCountry=[
        'us'
    ]
listOfCountPage=[1200]
for i in range(0,len(listOfCountry)):
    print('Processing country: ',listOfCountry[i])
    # lis of numbers
    url="https://www.telguarder.com/"+listOfCountry[i]
    print(url)
    # PAGES=int(input("Enter number of pages: "))
    PAGES=listOfCountPage[i]
    print("PAGES : \n",PAGES)
    driver = webdriver.Firefox()
    speedNumberListt=speedNumberList(driver,url,PAGES)
    file_name=listOfCountry[i]+".txt"
    textfile = open(file_name, "w")
    for a in speedNumberListt:
        print(a.text)
        textfile.write(a.text + "\n")
    textfile.close()
    # numberList_list=numberList(driver,url,PAGES)
    # print(numberList_list)
    # file_name=country+".txt"
    # textfile = open(file_name, "w")
    # for element in numberList_list:
    #     textfile.write(element + "\n")
    # textfile.close()

    # url_number="https://www.telguarder.com/"+country+"/number/"
    # getsta=getStatus(numberList_list,url_number)
    # file_name='telguarder_'+country+'.json'
    # a_file = open(file_name, "w")
    # json.dump(getsta, a_file)
    # a_file.close()



    # dic list with comments (json format)
    # url_number="https://www.telguarder.com/"+country+"/number/"
    # comment_list_dic=CommentList(numberList_list,url_number)
    # file_name='telguarder_'+country+'.json'
    # a_file = open(file_name, "w")
    # json.dump(comment_list_dic, a_file)
    # a_file.close()
    del driver
    # del numberList_list
    # del comment_list_dic
