# Register Map Project
This project is for the development of a simple internal tool to keep track of registers in embedded development. Some embedded experience
may be required to understand field lengths, etc.

## Installation
- **Clone the repo**

  ```console 
    git clone git@github.com:aadee92/reg-map.git
  ```
 
 - **Copy content from ```env.sample.py``` file inside** ```config/settings/``` **folder and create ```env.py``` file in same location**.
 
 - ```env.py``` **will have environment variables in different stages like development, stage, production e.t.c**.
 
 - **Perform Database Migration**

    ```console
      python manage.py migrate
    ```
  
 - **Create Superuser using below command and fill up required informations.**

    ```console
      python manage.py createsuperuser
    ```
 
 - **Run development server**

    ```console
      python manage.py runserver
    ```
 
 - **Open ```http://localhost:8000/``` on browser.**

 - **To use django-admin dashboard open ```http://localhost:8000/admin``` on browser and provide required credentials.**
 
