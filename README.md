# gofundMEEPLE

gofundMEEPLE* connects boardgame creators and boardgame enthusiasts together to bring boardgames to life. Creators will be able to launch their projects on gofundMEEPLE and enthusiasts can back the project by making pledges. Pledgers will be able to submit fan-based ideas for the final stretch goal**, and once/if the final stretch goal is reached creators must choose one (or more) fan-based idea and make it come to life! 

*Meeple: small figures used as a playing piece in boardgames and have a similar appearance to human figures
**Stretch goals: additional features the boardgame creators include within the boardgame once a certain amount of funding has been reached. It may differ based on pledge levels

This project has been created in Django as part of the She Codes Plus bootcamp REST API module. It involved creating the endpoints and API for a crowdfunding website. THe frontend will be built out as part of the JavaScript & React module. 

## Features 
```
  1. User Accounts
      i. POST: creating user accounts by providing username, email and password
      ii. GET: retrieving list of users, including their IDs, username, email and is_active status
      iii. PUT: modifying user information. Only works if user provides correct token authentication
      iv. DEL: deleting user profile. Only works if user provides correct token authentication
      
  2. Projects (ie. when boardgame creators create a crowdfunding project for their boardgame idea) 
      i. POST: creating projects by providing title, description, goal, status etc. 
      ii. GET: retrieving list of projects. This provides a summary view of all projects on the website
      iii. GET: retrieving detailed view of a project. This provides all information available for the project, including pledges that have been made to the project
      iv. PUT: modifying project details. Only works if user provides correct token authentication
      v. DEL: deleting project and all pledges for the project
  
  3. Pledges
      i. POST: creating pledges by providing amount pledged, comment, which project to pledge to
      ii. GET: retrieving list of pledges that have been made throughout the whole website
      iii. GET: retrieving list of pledges that have been made for a particular project
      iv. PUT: modifying pledge. Only works if user provides correct token authentication
      v. DEL: deleting pledge. Only works if user provides correct token authentication. Will automatically recount the total pledged amount for a project
  
  4. Stretch goals 
      i. POST: Adding 'fan based stretch goal comment'. If Statement included to limit users to adding 1x comment per project if they have made a pledge to that project
      ii. GET: retrieving list of stretch goals that have been made throughout the whole website
      iii. GET: retrieving list of stretch goals that have been made for a particular project
      iv. PUT: modifying 'fan based stretch goal comment'. Only works if user provides correct token authentication
      v. DEL: deleting comment. Only works if user provides correct token authentication
  
  5. Total pledged
      i. GET: retrieving total amount pledged. Django will automatically calculate this total amount 
  
  6. Status codes
      i. Get returns 200
      ii. Create returns 201
      iii. Not found returns 404. A customised page will allow user to go back to the homepage. 
  
  
  7. Use token authentication
      i. POST: users gain their token authentication by providing correct username and password
```
  
# Project submission
```
  Overview: Create the endpoints and APIs for a crowdfunding website. 
  
  Submission requirements:
      i. Screenshot of Insomnia, demonstrating a successful GET method for any endpoint
      ii. Screenshot of Insomnia, demonstrating a successful POST method for any endpoint
      iii. Screenshot of Insomnia, demonstrating a token being returned
      iv. Step by step instructions for how to register a new user and create a new project (i.e.endpoints and body data)
      v. API specification and database schema
```
