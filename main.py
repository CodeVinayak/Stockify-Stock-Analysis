import requests
from bs4 import BeautifulSoup

# URL of the page with the download button
url = "https://www.chittorgarh.com/report/latest-buyback-issues-in-india/80/tender-and-open-market-buyback/"

# Step 1: Fetch the page content
response = requests.get(url,verify=False)

if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Find the download button using its class
    download_button = soup.find('a', class_='btn btn-xs btn-secondary mb-2')
    
    if download_button:
        # Extract the href attribute which contains the download URL
        file_url = download_button.get('href')
        
        if file_url:
            # Make the file URL absolute if it's a relative URL
            if not file_url.startswith('http'):
                file_url = 'https://www.chittorgarh.com' + file_url
            
            # Step 4: Download the file
            file_response = requests.get(file_url)
            
            # Check if the file was downloaded successfully
            if file_response.status_code == 200:
                with open('buyback_data.csv', 'wb') as file:
                    file.write(file_response.content)
                
                print("File downloaded successfully.")
            else:
                print(f"Failed to download file. Status code: {file_response.status_code}")
        else:
            print("Download URL not found.")
    else:
        print("Download button not found.")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
