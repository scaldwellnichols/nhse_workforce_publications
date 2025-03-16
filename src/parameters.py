import pathlib as Path

BASE_DIR = Path.Path('.')
DATA_DIR = BASE_DIR / 'data'
OUTPUT_DIR = BASE_DIR / 'output'

current_time_period = '2024-11'

nhs_digital_url = 'https://digital.nhs.uk'
workforce_statistics_url = f'{nhs_digital_url}/data-and-information/publications/statistical/nhs-workforce-statistics'
gp_workforce_statistics_url = F'{nhs_digital_url}/data-and-information/publications/statistical/general-and-personal-medical-services'
