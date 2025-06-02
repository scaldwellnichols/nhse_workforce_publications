from src import parameters as params
from src.utilities import pre_processing


workforce_stats = pre_processing.NHSDigitalPublicationSeries(params.workforce_statistics_url)
workforce_stats.download_latest_publication_files()