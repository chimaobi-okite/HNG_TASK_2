# HNG_BACKEND_TASK_2

## Task Objective
Build a simple REST API capable of CRUD operations on a resource, say, a "person". The chosen programming language should interface with any chosen database of your choice.

## Solution and Implementation
Implemented the requirements. Tested the API exhaustively using Postman and also wrote Python scripts that test the API endpoints locally as specified.
View the test script at app.test_main.py

## Technologies Used
1. FastApi
2. Postgres database
3. SqlAlchemy
5. Render (deployment)

## UML Database Class Diagram
![PersonUMLDiagram](https://github.com/chimaobi-okite/HNG_TASK_2/assets/70687495/cab0f52c-4a5c-4db2-9855-c5230670cc46)

## Running the FastAPI Project on Your Computer

### Prerequisites:
  * Python == 3.10.10 installed on your system.
  * PostgreSQL installed and running on your system.

### Steps:
1. **Clone the GitHub Repository:**

    *bash*
    ```
    git clone https://github.com/chimaobi-okite/HNG_TASK_2.git
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

8. **Access the API on Web**
   Open your browser and navigate to [https://hng-task-2-i3l2.onrender.com/docs](https://hng-task-2-i3l2.onrender.com/docs) to view swagger docs
   for redoc nagivate to [https://hng-task-2-i3l2.onrender.com/redoc](https://hng-task-2-i3l2.onrender.com/redoc)
    
