# Burger Project

## **Setup Instructions**

Follow these steps to set up and run the Burger project:

---

### **1. Clone the Repository**
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/parad13/Burger
cd Burger
```

---

### **2. Create a Virtual Environment**
Create a virtual environment for the project:

```bash
python -m venv venv
```

---

### **3. Activate the Virtual Environment**
Activate the virtual environment based on your operating system:

- **For Windows (cmd/PowerShell):**
  ```bash
  venv\Scripts\activate
  ```

- **For Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

---

### **4. Install Dependencies**
Install the required dependencies:

```bash
pip install -r requirements.txt
```

---
# 5. Add a .env file with the following variables
Example .env content:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RATE_LIMIT_PER_MINUTE=60

### **5. Add a `.env` File**
Create a `.env` file in the root directory and add the following variables:

```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RATE_LIMIT_PER_MINUTE=60
```

---

### **6. Build and Run the Application Using Docker**
Build and start the application with Docker:

```bash
docker-compose up --build
```

---

### **Additional Notes**

- **Ensure Docker is Installed:**
  Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and ensure it is running before executing Docker commands.

- **Stopping the Application:**
  To stop the application, press `Ctrl + C` in the terminal. To clean up the containers, run:

  ```bash
  docker-compose down
  ```

---