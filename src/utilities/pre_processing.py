import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os
import pathlib as Path
import datetime

from src import parameters as params
from src.utilities import file_utils, helpers

class NHSDigitalPublicationSeries():
    """
    Class to represent a series of publications on the NHS Digital website.
    
    The class is initialised with a URL to the series of publications.
    
    URLs to specific NHS Digital Workforce related publication can be found 
    in the parameters file of this repository.

    Parameters
    ----------------
    - `url` : str
        The URL to the NHS Digital publication series

    Attributes
    ----------------
    - `url` : Path.Path object
        The URL to the series of publications
    - `name` : str
        The name of the series of publications
    - `req` : requests.models.Response object
        The request object for the URL
    - `soup` : BeautifulSoup object
        The BeautifulSoup object for the URL
    - `publications` : list
        A list of the URLs for the publications in the series

    Methods
    ----------------
    - `get_files_in_publication` : Get the files in a publication
    - `download_files_in_publication` : Download the files in a publication
    - `download_all_publication_series` : Download all the files in the series of publications
    """
    def __init__(self, url):
        self.url = Path.Path(url)
        self.name = Path.Path(self.url).name
        self.req = requests.get(url)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
        self.publications = [link.get('href') for link in self.soup.find_all('a') if 'statistical' in link.get('href')]

    def get_files_in_publication(self, publication_url):
        req = requests.get(f'{params.nhs_digital_url}/{publication_url}')
        soup = BeautifulSoup(req.text, 'html.parser')

        file_extensions = ['zip', 'csv'
                           #, 'xls', 'xlsx'
                           ]
        files = [link.get('href') for link in soup.find_all('a') if any(extension in link.get('href') for extension in file_extensions)]

        return files
    
    def download_files_in_publication(self, publication_url):
        files = self.get_files_in_publication(publication_url)
        time_period = helpers.extract_month_year(publication_url)
        time_period = datetime.datetime.strptime(time_period, '%B-%Y').strftime('%Y-%m')
        download_dir = params.DATA_DIR / self.name / time_period
        os.makedirs(download_dir, exist_ok=True)
        # Download each file in the links list
        for file in files:
            file_utils.download_file(file, download_dir)
            file_as_path = Path.Path(file)
            if file_as_path.suffix == '.zip':
                file_utils.extract_zip(download_dir / file_as_path.name, remove_zip=True)
    
    def download_all_publication_series(self):
        """
        Downloads all files in the publication series.

        WARNING: This method will take a while to run and downloads a vast amount of data.
        """
        for publication in self.publications:
            self.download_files_in_publication(publication)

    def download_latest_publication_files(self):
        """
        Downloads the files in the latest publication in the series.
        """
        latest_publication = self.publications[0]
        self.download_files_in_publication(latest_publication)
        