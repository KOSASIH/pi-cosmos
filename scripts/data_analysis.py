import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up API keys and other configuration
API_KEY = os.getenv('PI_COSMOS_API_KEY')
API_URL = 'https://api.pi-cosmos.com/v1'

# Load data from the Pi Cosmos API
data_url = f'{API_URL}/data'
data_params = {
    'filters': 'location:New York,commodity:Gold',
    'sort': '-date',
    'limit': 1000,
}
data_headers = {
    'Authorization': f'Bearer {API_KEY}',
}
data_response = requests.get(data_url, params=data_params, headers=data_headers)
data_json = data_response.json()
data_df = pd.DataFrame(data_json['data'])

# Clean and preprocess the data
data_df['date'] = pd.to_datetime(data_df['date'])
data_df = data_df.set_index('date')
data_df = data_df.resample('D').interpolate()
data_df = data_df.dropna()

# Analyze the data
data_summary = data_df.describe()
data_corr = data_df.corr()
data_heatmap = sns.heatmap(data_corr, annot=True, cmap='coolwarm')
data_plot = data_df.plot(kind='line')

# Save the results
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
data_summary.to_csv(os.path.join(output_dir, 'data_summary.csv'))
data_corr.to_csv(os.path.join(output_dir, 'data_corr.csv'))
data_plot.get_figure().savefig(os.path.join(output_dir, 'data_plot.png'))
data_heatmap.get_figure().savefig(os.path.join(output_dir, 'data_heatmap.png'))

# Display the results
plt.show()
