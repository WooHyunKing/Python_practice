# Hello, this is my website scrapper !

from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    results=[]
    soup = BeautifulSoup(request.text, "html.parser")
    companys=soup.find_all("td",class_="company")
    companys.pop(0)
    for company in companys:
      links=company.find("a")
      titles = company.find_all("h3")
      positions = company.find_all("h2")
      regions,pays=company.find_all("div",class_="location")

      job_data={
      }

      link=links['href']
      job_data['link']=f"https://remoteok.com{link}"
      
      for span in titles:
        job_data['company']=span.string[1:]
      for position in positions:
        job_data['position']=position.string[1:-1]

      for region in regions:
        job_data['region']=region.string
      for pay in pays:
        job_data['pay']=pay.string

      results.append(job_data)

  for result in results:
    print(result)
    print("")
    print("////////")
    print("")
    
         
    # write your ✨magical✨ code here
  else:
    print("Can't get jobs.")

extract_jobs("rust")