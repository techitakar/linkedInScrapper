from bs4 import BeautifulSoup
import requests

def listJobs(keyword,page):
    url=f'https://in.linkedin.com/jobs/search?keywords={keyword}&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum={page}'
    req=requests.get(url)
    print("Status code:",req.status_code,"\n")
    soup=BeautifulSoup(req.content,'html.parser')
    companies=soup.find_all('div',class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
    for comp in companies:
        title=comp.find('h3',class_="base-search-card__title").text.strip()
        compName=comp.find('h4',class_="base-search-card__subtitle").a.text.strip()
        jobLink=comp.find('a',class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]").get("href")
        print(f'Position: {title}')
        print(f'Company Name: {compName}')
        print(f'Job Desc Link: {jobLink} ')
        print()

def main():
    uinput=input("Enter a keyword for Jobs: ")
    pageNo=0
    listJobs(uinput,pageNo)
    while True:
        promt=input("Do you want to move to next page(y/n):")
        if promt=="y":
            pageNo += 1
            listJobs(uinput,pageNo)
        elif promt=='n':
            break
        else:
            print('Enter (y/n):')

if __name__=="__main__":
    main()