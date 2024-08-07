import threading
import time
import subprocess
import os

def run_ingest():
    while True:
        try:
           
            subprocess.run(['python', 'services/ingest.py'], check=True) 
            print('current data updated.')
        except subprocess.CalledProcessError as e:
            
            print(f"Error running ingest.py: {e}")
        time.sleep(60)  # Wait for 60 seconds before running again


def run_daily_task():
    while True:
        try:
            
            subprocess.run(['python', 'services/historical_ingestion.py'], check=True)
            print('historical data updated')
        except subprocess.CalledProcessError as e:
            
            print(f"Error running daily_task.py: {e}")
        time.sleep(900)  


# Define the function to start the background task
# def start_background_task():
#     # Create and start a daemon thread for the background task
#     thread = threading.Thread(target=run_ingest)
#     thread.daemon = True  # Ensure the thread exits when the main program exits
#     thread.start()

def start_background_task():
    # Create and start a daemon thread for the 60-second task
    ingest_thread = threading.Thread(target=run_ingest)
    ingest_thread.daemon = True  # Ensure the thread exits when the main program exits
    ingest_thread.start()

    # Create and start a daemon thread for the daily task
    daily_task_thread = threading.Thread(target=run_daily_task)
    daily_task_thread.daemon = True  # Ensure the thread exits when the main program exits
    daily_task_thread.start()
