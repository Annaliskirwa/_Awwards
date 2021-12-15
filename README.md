# Ann_awwards  

#### 15/12/2021   
#### By **Annalis Kirwa**   

This is an application that will allow a user to post a project he/she has created and get it reviewed by his/her peers.
The project will be rated on 3 different criteria:  
* Usability  
* Content  
* Design 

Each day the project with the highest votes will be posted on the homepage  

## Features 
As a user of Ann-awwards web application, you will be able to:  
* View posted projects and their details
* Post a project to be rated/reviewed.
* Rate/ review other users' projects.
* Search for projects.
* View projects overall score.  
* View my profile page  


## Setup/Installation Requirements  
 ### To interact with the Ann-awwards web application:
 * Have the latest version of browser installed   
 * Click on this <a href = "https://ann-awwards.herokuapp.com/">link</a> to use Ann-awwards  
  ### To contribute to Ann-awwards web application:  
 #### Clone the Repo  
 * Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_Awwards" >link </a>
* Clone the repository
* Open the project cloned project
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE annawwards;  
    
#### Run initial Migration
    python3.8 manage.py makemigrations   
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000  
    
  ## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.8  
* HTML
* Bootstrap
* Django  
* Postgres 
* Restful Apis  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**


