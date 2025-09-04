ACEestFitness and Gym – Flask Web Application
=============================================

This project is a Flask-based fitness tracker web application with unit tests.
It allows users to log workouts and view them directly in the browser.
The application was adapted from a desktop Tkinter version to a Flask web app.
NOTE: MASTER Branch is used for deployment 


Project Structure
-----------------
D:\DevOps\GMY_APP\
│
├── Application.py        -> Main Flask application
├── test_application.py   -> Unit tests using pytest
├── requirements.txt      -> Python dependencies
├── Dockerfile            -> Docker build file
└── readme.txt            -> Project documentation



Features
--------
- Add a workout with a name and duration (in minutes).
- View all logged workouts on the homepage.
- Validation ensures only numeric durations are accepted.
- Includes test cases for endpoints and validation.


Setup Instructions
------------------
1. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate     (On Windows)

2. Install dependencies:
   pip install -r requirements.txt


Running the Application
-----------------------
Start the Flask server:
   python Application.py

Open the app in your browser:
   http://127.0.0.1:5000/


Running Tests
-------------
Run the test suite with:
   pytest -v test_application.py

The tests cover:
- Homepage loading.
- Adding a workout.
- Validation for invalid durations.
- Multiple workout entries.

Running with Docker
-------------------
1. Build the Docker image:
   docker build -t fitness-app .

2. Run the container:
   docker run -p 5000:5000 fitness-app

3. Open the app in your browser:
   http://127.0.0.1:5000/

Example Usage
-------------
1. Open the app in a browser.
2. Enter a workout name (e.g., Pushups).
3. Enter duration (e.g., 15).
4. Click "Add Workout".
5. See logged workouts appear in the list.


Future Enhancements
-------------------
- Store workouts in an SQLite database instead of in-memory.
- Add user accounts for personalized tracking.
- Provide analytics and charts for workout progress.
- Deploy the app using Docker or cloud hosting.
------------------------------------------------------------------------

-   Tests in test_application.py are executed automatically on every
    push to GitHub via GitHub Actions.

-   The workflow file is located at:

        .github/workflows/CI_CDPipeline.yml

-   If tests fail, the pipeline will stop and prevent deployment.

------------------------------------------------------------------------

