
## Updataone project
## Website that cosnsumes Bundesliga api  http://www.openligadb.de/(see https://github.com/Dirrot/python-openligadb-api). Using the json api.
<br/><br/> 
## Provided functionalities by the website:
- Next upcoming matches (following Gameday)
- All matches of the actual season
- Win/Loss Ratio of the actual season of each team
- Optimized for different resolutions through a type and layout of your choice
- A search functionality for a specific team displaying all the information above 
<br/><br/> 
## Tech stack:
Django 
check requirements.txt 
<br/><br/> 

## Run the application.  
1 install virtual env <br/><br/>
pip install virtualenv <br/><br/>
2 create virtual enviroment <br/><br/>
 virtualenv <my_env_name>  <br/><br/>
3 run virtualenv <br/><br/>
 <my_env_name>\Scripts\activate on Windows os  <br/><br/>
4 install requiremnts txt <br/><br/>
 pip install requrements.txt  <br/><br/>
5 run the project(website)<br/><br/>
 python manage.py runserver <br/><br/>

## Urls of the website. 
If you are using the default port :
http://127.0.0.1:8000/  
http://127.0.0.1:8000/ratio
http://127.0.0.1:8000/upcoming
http://127.0.0.1:8000/search_team?q=VfL+Bochum


