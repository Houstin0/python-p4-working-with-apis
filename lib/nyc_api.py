
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    program_list=[]
    programs=json.loads(self.get_programs())
    for program in programs:
      program_list.append(program["agency"])

      return program_list


# programs = GetPrograms().get_programs()
# print(programs)

programs=GetPrograms()
programs_schools=programs.program_school()

for school in set(programs_schools):
  print(school)


#for any url

class JSONLoader:
  
  def __init__(self,url):
    self.url=url

  def get_response_body(self):
    response=requests.get(self.url)
    return response.content

  def load_json(self):
    response_body=self.get_response_body()
    return json.loads(response_body)

url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
loader = JSONLoader(url)
programs_schools = loader.load_json() 
for program in programs_schools:
  print(program.get("agency"))