# The Library

- ### Installation
- create a directory and clone projects in it.
    - create a virtual environment and activate it.
        ```
        - virtualenv -p python3 venv
        - source venv/bin/activate
        ```
    - and after all the changes in models.py files you should run the following commands:
       ```
        pip3 install -r requirements.txt
        Create your secrets file using settings/secrets.py.template file and write your credentials into it.(* if you are using prod.py file configure your postgres settings)
        python3 manage.py makemigrations book & python3 manage.py migrate
        python3 manage.py runserver
       ```
- To create an admin user:
    ``` 
    python3 manage.py createsuperuser 
    ```
    
- To run in the localhost:
    ```
    python3 manage.py runserver
    ```
- ## API
    - To list all the books:
        - `books/`

    - To get the detail of a books:
        - `books/{{id}}/`
    - To add the detail of a books:
        - `books/add/`
        - parameters as name,author,publisher,etc.
    - To delete the detail of a books:
        - `books/delete/{{id}}`
     
    - To see all others api, documentation:
        - `docs/`
        
