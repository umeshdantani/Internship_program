from bs4 import BeautifulSoup
import requests
import time

print('put some skill that you are not familiar with')
unfamiliar_skills=input('>')
print('filtering out')
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    #print(html_text)
    soap = BeautifulSoup(html_text,'lxml')
    jobs=soap.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #print(jobs)
    #job=soap.find('li',class_='clearfix job-bx wht-shd-bx')
    #print(job)
    for index,job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').span.text
        if'today' in date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ',"")
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            #print(company_name)
            #print(skills)
            more_info=job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"company Name: {company_name.strip()}")
                    f.write(f"Required Skills:{skills.strip()} ")
                    f.write(f'more Info: {more_info}')
                    f.write(date)
                print(f'File saved: {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*600)
