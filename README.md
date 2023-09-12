# HNG_BACKEND_TASK_@

## Task Objective
Build a simple REST API capable of CRUD operations on a resource, say, a "person". The chosen programming language should interface with any chosen database of your choice.

## Implementation Requirements
1. REST API Development:
* Develop an API with endpoints for:
* CREATE: Adding a new person.  =>/api
* READ: Fetching details of a person.  => /api/user_id
* UPDATE: Modifying details of an existing person => /api/user_id
* DELETE: Removing a person => /api/user_id
* Ensure all interactions with the database are secure and free from common vulnerabilities (e.g., SQL injections).
2. Database Modelling: (Bonus)
* UML Diagram: Design and present a UML (Unified Modeling Language) diagram that represents the structure and relationships of your API's classes and models.
3. Testing:
* Using tools like Postman or (scripts written in Python using the requests library) that tests each CRUD operation in your API.
This  should:
* Add a new person (e.g., "Mark Essien").
* Fetch details of a person
* Modify the details of an existing person.
* Remove a person
4. Dynamic Parameter Handling:
* Your API should be flexible enough to handle dynamic input. If we provide a name (or other details), your backend should be able to process operations using that name.
Example: If we pass "Mark Essien", we should be able to perform all CRUD operations on "Mark Essien".
Add validation – field should only be strings; integers or any other data type should not be allowed.
5. GitHub Repository:
Create a GitHub repository for this project.
Ensure the repository contains:
A detailed README.md file explaining how to set up, run, and use the API.
The source code for the API.
UML diagrams (or links to view them).
6. Documentation:
Provide a documentation file (e.g., DOCUMENTATION.md in your GitHub repo) that outlines:
Standard formats for requests and responses for each endpoint.
Sample usage of the API, including example requests and expected responses.
Any known limitations or assumptions made during development.
Instructions for setting up and deploying the API locally or on a server.
7. Hosting
Using the same Server used in the Stage One task (or another server, if possible), modify it accordingly to  host your endpoint with a URL like this https://theirdomain.com/api
Test extensively with various testing tools to make sure it is accessible before submitting

## Solution and Implementation
Upon my appointment as the ISEC Chairman for the 2021/22 SEEES elections on June 20th, 2023, 
I recognized the need for reforms to ensure transparency and rectify the previously highlighted issues. 
Our refined approach encompassed the following:

## Technologies Used
1. FastApi
2. Postgres database
3. SqlAlchemy
5. Render (deployment)

## Postgres Database Schema
![election_schema_table](https://github.com/chimaobi-okite/election_api/assets/70687495/d5045fbe-5a70-4586-8c93-5d21e56598f7)

## Running the FastAPI Project on Your Computer

### Prerequisites:
  * Python == 3.10.10 installed on your system.
  * PostgreSQL installed and running on your system.

### Steps:
1. **Clone the GitHub Repository:**

    *bash*
    ```
    git clone https://github.com/chimaobi-okite/election_api.git
    cd HNG_TASK_2
    ```

2. **Set up a Virtual Environment:**

    *bash*
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Dependencies:**

    *bash*
    ```
    pip install -r requirements.txt
    ```
4. **Configure PostgreSQL:**

    Start PostgreSQL and create a new database for your project.
    * Create a .env file in the project root directory
    * Update your project's database connection configuration in a .env file. Check the app.config file for the required configurations

    Also create a test_database and modify the *SQLALCHEMY_DATABASE_URL* @ app.test_main.py file with your database info

5. **Run Tests:**
    
    *bash*
    ```
    pytest
    ```
6. **Start the FastAPI Application:**

    *bash*
    ```
    uvicorn app.main:app --reload
    ```

7. **Access the API:**

    Open your browser and navigate to http://localhost:8000/. 
    You should see the FastAPI default page. 
    You can also access the auto-generated docs by visiting http://localhost:8000/docs.
