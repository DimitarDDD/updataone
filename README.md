# updataone
updataone project
Website that cosnsumes Bundesliga api  http://www.openligadb.de/(see https://github.com/Dirrot/python-openligadb-api).
Using the json api.
Provided functionalities by the website:
- Next upcoming matches (following Gameday)
- All matches of the actual season
- Win/Loss Ratio of the actual season of each team
- Optimized for different resolutions through a type and layout of your choice
- A search functionality for a specific team displaying all the information above 

Tech stack:
Django 
check requirements.txt 

Run the application.  
1 install virtual env
-pip install virtualenv
2 create virtual enviroment 
- virtualenv <my_env_name>  
3 run virtualenv 
- <my_env_name>\Scripts\activate on Windows os 
4 install requiremnts txt 
- pip install requrements.txt  
5 run the project(website)
- python manage.py runserver 

Urls of the website. 
If you are using the default port :
http://127.0.0.1:8000/  
http://127.0.0.1:8000/ratio
http://127.0.0.1:8000/upcoming
http://127.0.0.1:8000/search_team?q=VfL+Bochum


