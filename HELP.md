
# Poetry - dependencies manager
see pyproject.tml

## NOT A PACKAGE
add the following in the pyproject.tml so that it won't complain at you when you install

[tool.poetry]
package-mode = false

## install all dependencies
poetry install

## add dependency
poetry add DEPENDENCY

## add group dependency
poetry add --group test DEPENDENCY

## check virtual env 
poetry env info

# START PROJECT
## start the app and reload on changes. main is module, app is instance. in main.py
poetry run uvicorn app.main:app --reload
## start with choosing port
poetry run uvicorn main:app --port 8000

# DOCS by default for API
## /docs gives you an interactive documentation on your API. You can even click "try it out" for each endpoint
http://localhost:8000/docs

## /redoc gives you an API documentation. NOT interactive
http://localhost:8000/redoc

# Load ENV variables
## Add load_dotenv() in the following files
database.py
  load_dotenv()
main.py
  load_dotenv()
alembic/env.py
  load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
security.py
  load_dotenv()
