# 1. Clone the repository
- git clone <repository-url>
- cd <repository-directory>

# 2. Create a virtual environment
- python -m venv venv

# 3. Activate the virtual environment
# Windows:
- venv\Scripts\activate
# Linux/Mac:
- source venv/bin/activate

# 4. Install dependencies
- pip install -r requirements.txt

# 5. Add a .env file with the following variables
- Example .env content:
- SECRET_KEY=your-secret-key
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- DATABASE_URL=postgresql://user:password@localhost:5432/dbname
- ALGORITHM=HS256
- ACCESS_TOKEN_EXPIRE_MINUTES=30
- RATE_LIMIT_PER_MINUTE=60

# 6. Build and run the application using Docker
- docker-compose up --build
