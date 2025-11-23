import requests
import os
import zipfile

def download_data():
    """Download project data files from Google Drive"""
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("Data download instructions:")
    print("1. Download data from: [YOUR_GOOGLE_DRIVE_LINK]")
    print("2. Extract the files into the 'data' folder")

    
if __name__ == "__main__":
    download_data()