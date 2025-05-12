import requests
import csv

# Change the data here
file = 'Data/Dataset1/birds.csv'
page = 10
records = 5000
api_url = f"https://xeno-canto.org/api/3/recordings?query=grp:birds+cnt:Netherlands&per_page={records}&page={page}&key=952c49c88325d578539da1ea57554f057de58293"
fieldnames = [
        'gen', 'sp', 'ssp', 'grp', 'en', 'rec', 'cnt', 'loc',
        'lat', 'lon', 'alt', 'type', 'sex', 'stage', 'method',
        'url', 'file', 'file-name', 'length', 'date', 'uploaded',
        'animal-seen', 'playback-used', 'q'
    ]

# Make the API request
response = requests.get(api_url)
data = response.json()

# Open a CSV file to write to 
with open(file, mode='w', newline='', encoding='utf-8') as csv_file:
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate over recordings
    for recording in data['recordings']:
        # Write only the fields we care about
        row = {key: recording.get(key, '') for key in fieldnames}
        writer.writerow(row)

print("Data saved to bird_recordings.csv")