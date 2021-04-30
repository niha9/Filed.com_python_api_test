# Python_web_API 

A Django Web API that simulates the behavior of an audio file
server while using SQL database.
Requirements: You have one of three audio files which structures are defined below
Audio file type can be one of the following:
    1 – Song
    2 – Podcast
    3 – Audiobook

Song file fields:
        - ID – (mandatory, integer, unique)
        - Name of the song – (mandatory, string, cannot be larger than 100
        characters)
        - Duration in number of seconds – (mandatory, integer, positive)
        - Uploaded time – (mandatory, Datetime, cannot be in the past)
        
Podcast file fields:
        - ID – (mandatory, integer, unique)
        - Name of the podcast – (mandatory, string, cannot be larger than 100
        characters)
        - Duration in number of seconds – (mandatory, integer, positive)
        - Uploaded time – (mandatory, Datetime, cannot be in the past)
        - Host – (mandatory, string, cannot be larger than 100 characters)
        - Participants – (optional, list of strings, each string cannot be larger than
        100 characters, maximum of 10 participants possible)
        
Audiobook file fields:
        - ID – (mandatory, integer, unique)
        - Title of the audiobook – (mandatory, string, cannot be larger than 100
        characters)
        - Author of the title (mandatory, string, cannot be larger than 100
        characters)
        - Narrator - (mandatory, string, cannot be larger than 100 characters)
        - Duration in number of seconds – (mandatory, integer, positive)
        - Uploaded time – (mandatory, Datetime, cannot be in the past)


#How to Run the project
    1. env\Scripts\activate
    2.pip install -r requirements.txt
    3. Python manage.py migrate
    4.python manage.py runserver

# How to TEST APIS
Test api structure is given in documentation, it is postman exported one.

# Apis end point

#### 1. create
    Song:
        url = http://127.0.0.1:8000/api/audio/?type=song
        method = Post
        content-type=json
        Body:
            For Example:
                 {
                    "name": "Red",
                    "duration": 5,
                    "uploaded": "2021-04-30T17:24:38.003343Z"
                 }
    Podcast:
        url = http://127.0.0.1:8000/api/audio/?type=podcast
        method = Post
        content-type=json
        Body:
            For example:
                {    
                    "name": "Post_get",
                    "duration": 2,
                    "uploaded": "2021-04-30T17:24:12.737942Z",
                     "host_id": 3,
                     "participants_id": [3,4,5]
                }
    Audiobook:
        url = http://127.0.0.1:8000/api/audio/?type=audiobook
        method = Post
        content-type=json
        Body:
            For example:
                {
                    "name": "Martian",
                    "duration": 5,
                    "uploaded": "2021-04-30T17:22:34.925820Z",
                    "author_id": 2,
                    "narrator_id": 5
            }
        
#### 2. Update
    Song:
        url = http://127.0.0.1:8000/api/audio/<song_id>/?type=song
        method = Patch
        content-type=json
        Body:
            For Example:
                 {
                    "name": "Red-one",
                    "duration": 7,
                   
                 }
            
    Podcast:
        url = http://127.0.0.1:8000/api/audio/<audio_id>/?type=podcast
        method = Patch
        content-type=json
        Body:
            For example:
                {    
                    "name": "update_Post_get",
                    "duration": 2,
                     "host_id": 2,
                     "participants_id": [3,4,5]
                }
            
    Audiobook:
        url = http://127.0.0.1:8000/api/audio/<audiobook_id>?type=audiobook
        method = Patch
        content-type=json
        Body:
            For example:
                {
                    "name": "Updated_Martian",
                    "duration": 100,
                    "author_id": 3
                    "narrator_id": 2
            }
            
#### 3. Delete
    Song:
        url = http://127.0.0.1:8000/api/audio/<song_id>/?type=song
        method = Delete
        content-type=json
            
    Podcast:
        url = http://127.0.0.1:8000/api/audio/<podcast_id>/?type=podcast
        method = Delete
        content-type = json
        
    Audiobook:
        url = http://127.0.0.1:8000/api/audio/<audiobook_id>?type=audiobook
        method = Delete
        content-type = json

#### 4.GET

    Song:
        url = http://127.0.0.1:8000/api/audio/?type=song
        method = Get
        content-type = json
        
     Podcast:
        url = http://127.0.0.1:8000/api/audio/?type=podcast
        method = Get
        content-type = json
        
    Audiobook:
        url = http://127.0.0.1:8000/api/audio/?type=audiobook
        method = Get
        content-type = json
              
    
    
### Return from REQUEST

    - Action is successful: 200 OK
    - The request is invalid: 400 bad request
    - Any error: 500 internal server error



