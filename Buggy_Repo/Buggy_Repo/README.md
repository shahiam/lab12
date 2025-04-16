### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies  

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Arjun Dingankar: 20241113024
- Haaris Iqbal: 2024101045
- Sahishnu Pawan Kumar: 2024113016
- Rushil Grover: 2024101137
- Aaryan Shah: 2024113014

### Table to keep track

| ID  | Issue Description                                                                               | Identified By | Fixed By     |
|-----|-------------------------------------------------------------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                                                                         |      -        | Whole Team   |
| 2   | in index.html, the meTa charset should be UTF-8 encoded, not ISO-8859-1                         |    Haaris     |   Arjun      |
| 3   | in profile.html, the script tag should contain scripts/profile.js, not styles/profile.js        |    Arjun      |   Sahishnu   |
| 4   | there should be a navigation bar in analytics.html                                              |    Arjun      |   Arjun      |
| 5   | in items.js, line 41 should be headers: { "Content-Type": "application/json" }                  |    Haaris     |   Haaris     |
| 6   | in items.html, an entire container needed to be made                                            |    Sahishnu   |   Arjun      |
| 7   | quiz.html has not been included in any navigation bar                                           |    Aaryan     |   Arjun      |
| 8   | in items.js, lines 37 and 38 have been corrected, where "name" and "description" were changed   |    Rushil     |   Haaris     |
|     | to "itemName" and "itemDescription".                                                            |    Arjun      |              |
| 9   | in analytics.js, the baseURL should be "http://localhost:8000", not "http://localhost:8001"     |    Arjun      |   Arjun      |
| 10  | in analytics.py, unnecessary initialisation of users list, should be empty                      |    Aaryan     |   Aaryan     |
| 11  | in profile.js, in deleteBtn, method is supposed to be 'DELETE', not 'PATCH' (line 43)           |    Haaris     |   Arjun      |
| 12  | in quiz.py, change line 44 to display a random question                                         |    Rushil     |              |
| 13  | in users.py, there are two instances of @router.post("/") - change symbol/word for one of them  |    Sahishnu   |   Sahishnu   |
| 14  | in analytics.py, was only saving the histogram; fix is to return the histogram                  |    Aaryan     |   Aaryan     |
| 15  | in items.py, router is defined as empty dictionary; fix is to make it a router API function     |    Rushil     |   Aaryan     |
| 16  | in items.py, there are two instances of @router.post("/") - change symbol/word for one of them  |    Haaris     |              |
| 17  | in main.py, there was unnecessary block of code starting with @app.get("/home"); commented out  |    Aaryan     |   Haaris     |
| 18  | in items.py, delete_one() called twice w/ different IDs; fix - delete 1 item per request        |    Sahishnu   |              |
| 19  | in analytics.js, line 15, plot changed to hist since hist is being returned in the file         |    Aaryan     |   Aaryan     |
| 20  | in quiz.py, GET with body(data:dict) is invalid, so fix is to to convert to POST                |    Rushil     |              |
| 21  | in models.py, in item: name should be defined as 'str', NOT 'int'                               |    Rushil     |              |
| 22  | in users.py, line 30: .delete_one({"_id": ObjectId(user_id)}) corrected from .delete_all()      |   Sahishnu    |   Sahishnu   |
| 23  | deleted home.js                                                                                 |    Haaris     |    Haaris    |
| 24  | added id in class item in models.py                                                             |    Arjun      |    Aaryan    |
| 25  | added class QuizAnswer to models.py so that i dont have to raise hand                           |   Aaryan      |   Aaryan     |
| 26  | fixed items.py                                                                                  |     Arjun     |    Arjun     |
| 27  |                                                                                                 |               |              |
| 28  |                                                                                                 |               |              |
| 29  |                                                                                                 |               |              |
| 30  |                                                                                                 |               |              |
| 31  |                                                                                                 |               |              |
