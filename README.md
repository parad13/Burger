## Steps to run the project
1. Clone the repository
2. Create a virtual env using `python -m venv venv`
3. Run `pip install -r requirements.txt`
4. add a .env file with the following variables: SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, DATABASE_URL, RATE_LIMIT_PER_MINUTE
5. Run `docker-compose up --build` (Need docker installed)