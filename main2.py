import urllib.request
import urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

# URL for the export request
export_url = "https://www.chittorgarh.com/report/export_report_csv.php"

# Prepare the payload for the POST request
payload = {
    "report_id": "80",
    "report_name": "latest-buyback-issues-in-india"
}

# Encode the payload
data = urllib.parse.urlencode(payload).encode('ascii')

# Set up headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.chittorgarh.com/report/latest-buyback-issues-in-india/80/tender-and-open-market-buyback/"
}

# Create a request object
req = urllib.request.Request(export_url, data=data, headers=headers, method='POST')

try:
    # Send the request and get the response
    with urllib.request.urlopen(req) as response:
        # Check if the request was successful
        if response.status == 200:
            # Get the filename from the response headers
            content_disposition = response.headers.get('Content-Disposition')
            filename = content_disposition.split('filename=')[1].strip('"') if content_disposition else "buyback_data.csv"

            # Read the response content
            content = response.read()

            # Save the CSV file
            with open(filename, 'wb') as file:
                file.write(content)
            print(f"CSV file '{filename}' has been downloaded successfully.")
        else:
            print(f"Failed to download CSV. Status code: {response.status}")

except urllib.error.URLError as e:
    print(f"Error occurred: {e.reason}")