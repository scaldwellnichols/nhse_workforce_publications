import requests
import pathlib as Path
import zipfile
import os

def extract_zip(zip_file_path : str, remove_zip=False):
    """
    Extracts a given zip file to a folder with the same name as the zip file.

    Parameters
    ----------
    `zip_file_path` : str
        Path to the zip file
    `remove_zip` : bool
        Whether to remove the zip file after extraction

    Returns
    -------
    None
    """
    file_as_path = Path.Path(zip_file_path)
    extract_dir = file_as_path.parent / file_as_path.name.replace('.zip', '')
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    if remove_zip:
        os.remove(zip_file_path)

def download_file(url, download_dir):
    url_as_path = Path.Path(url)
    file_name = download_dir / url_as_path.name
    with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)