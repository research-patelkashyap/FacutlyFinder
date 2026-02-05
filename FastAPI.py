from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from dbConnection.db_connection import SQLConnection as sc
from dbOperations.get_data import GetData
from contextlib import closing
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def run_system_tasks():
    try:
        print("Running scraper...")
        subprocess.run(["python", "-m", "scrape.dau.main"], check=True)
        print("Tasks completed successfully!")

        print("Initializing database...")
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during tasks: {e}")

@app.get("/run-tasks")
def trigger_tasks(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_system_tasks)
    return {"status": "Database init and Scraper started in the background."}

@app.get("/faculty")
def get_faculty_data():
    data = {}
    connection = sc().getConnection()
    connection_status = connection[1]
    if connection_status != 1:
        data = {"error":"Database connection failed"}
    else:
        with closing(sc().getConnection()[0]) as conn:
            data_getter = GetData(conn)
            data = data_getter.get_data()
    return {"data": data}
