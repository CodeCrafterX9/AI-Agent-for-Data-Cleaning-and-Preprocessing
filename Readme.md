# AI Agent for Data Cleaning and Preprocessing

An AI-powered data cleaning and preprocessing system that automates common data quality tasks such as handling missing values, detecting duplicates, data validation, transformation, and preparing datasets for downstream analytics or machine learning workflows.

---

## Project Setup

### Prerequisites

Before running the project, ensure you have:

- Docker installed
- Docker Desktop running
- Git installed

---

## Database Setup using Docker

The project uses a custom PostgreSQL Docker image to store and manage data.

### Step 1: Navigate to the Docker Directory

Open a terminal and move to the PostgreSQL Docker configuration folder:

```bash
cd my-custom-postgres
```

---

### Step 2: Build the Docker Image

Create the custom PostgreSQL image:

```bash
docker build -t my_postgres_db .
```

Verify that the image was created successfully:

```bash
docker images
```
Expected output should contain the image name

---

### Step 3: Create and Start the Docker Container

Run the PostgreSQL container:

```bash
docker run -d \
--name clean_agent_db \
-p 5432:5432 \
-v pgdata:/var/lib/postgresql/data \
my_postgres_db
```

### Command Breakdown

| Option | Purpose |
|----------|----------|
| `-d` | Runs the container in detached mode (background) |
| `--name clean_agent_db` | Assigns a fixed container name for easy reference |
| `-p 5432:5432` | Maps PostgreSQL port from container to local machine |
| `-v pgdata:/var/lib/postgresql/data` | Without Volume all database data would be lost when the container is deleted |
| `my_postgres_db` | Custom Docker image created in the previous step |

### Step 4: Verify the Container

Check whether the container is running:

```bash
docker ps -a
```

## Python Virtual Environment Setup

Move to the project root directory:

```bash
cd ..
```

Activate the virtual environment:

```bash
source ai_data_cleaning_agent/bin/activate
```

If the virtual environment does not already exist, create it first:

```bash
python -m venv ai_data_cleaning_agent
```

Then activate it and install the project dependencies:

```bash
pip install -r requirements.txt
```

---

## Verify PostgreSQL Connection

To verify that the application can connect to PostgreSQL, make sure you are in the project's root directory and run:

```bash
python scripts/test_postgres_connection.py
```

If everything is configured correctly and the Docker container is running, you should see a successful database connection message.

## Project Goal

This project aims to build an intelligent AI Agent capable of:

- Data Profiling
- Missing Value Handling
- Duplicate Detection
- Data Type Validation
- Automated Data Cleaning Recommendations
- Preparing Clean Data for Analytics and ML Pipelines

---

## Repository Structure

```text
AI-Agent-for-Data-Cleaning-and-Preprocessing/
│
├── ai_data_cleaning_agent/ (.venv)
|
├── my-custom-postgres/
│   ├── Dockerfile
│   └── init.sql
│
├── scripts/
│   ├── ai_agent.py
│   ├── backend.py
│   ├── data_cleaning.py
│   |── data_ingestion.py
|   |── main.py
|   |── preprocessing.py
|   └── test_postgres_connection.py
│
├── data/
|   └── sample_data.csv
├── ui/
|   └── .gitkeep
├── .gitignore
├── requirements.txt
└── README.md
```