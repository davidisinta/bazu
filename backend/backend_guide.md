## To run the App

1. **Navigate to the directory containing `requirements.txt`:**
   Open a terminal or command prompt and use the `cd` command to change to backend directory, where `requirements.txt` is located.
   
2. Run the requirements.txt file to have all the requirements before running the app:
    - pip install -r requirements.txt
    - `pipenv install `(if you're using pipenv) and `pipenv shell` to activate the virtualenv
   

3. Run the App:
   - python3 main.py
   - uvicorn main:app --reload