import matplotlib.pyplot as plt
import pandas as pd
import json 


# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Read the json data into a pandas dataframe 
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)

# Remove missing values
eva_df.dropna(axis=0, inplace=True)

# Sort data by date
eva_df.sort_values('date', inplace=True)

# Write the data to a csv file
eva_df.to_csv(output_file, index=False)

# Calculate cumulative time spent in space
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Plot the results
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()