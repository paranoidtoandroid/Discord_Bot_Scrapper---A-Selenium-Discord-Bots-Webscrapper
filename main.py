import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Write the headers to the CSV file
with open("discord_bots.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Tags", "Votes", "Description", "Average Score", "Server Count"])

# Create a webdriver instance
driver = webdriver.Chrome(options=chrome_options)


page_num = 1  # Initialize the page number

# Keep scraping data until we have at least 100 bots
bot_count = 0  # Initialize the counter
while bot_count < 37000:
    # Navigate to the Discord Bot List website
    driver.get(f"https://top.gg/list/top?page={page_num}")

    # Scroll down to the bottom of the page to load more data
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    # Wait for the data to load
    driver.implicitly_wait(5)  # Wait for up to 5 seconds

    # Extract the data from the page
    data = driver.execute_script("return window.__NEXT_DATA__")

    # Parse the JSON data to access the information about the Discord bots
    for entity in data["props"]["pageProps"]["initialResults"]["results"]:
        name = entity["name"]
        tags = [tag["displayName"] for tag in entity["tags"]]
        votes = entity["votes"]
        description = entity["description"]
        try:
          rating = entity["reviewStats"]["averageScore"]
        except (KeyError, TypeError):
          rating = None
        server_count = entity["socialCount"] if "socialCount" in entity else None

        
        # Print the extracted information
        print(f"Name: {name}")
        print(f"Tags: {tags}")
        print(f"Votes: {votes}")
        print(f"Description: {description}")
        print(f"Average Score: {rating}")
        print(f"Server Count: {server_count}")
        print()

       # Write the extracted data to a CSV file
        with open("discord_bots.csv", "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name, tags, votes, description , rating, server_count])

        # Increment the counter
        bot_count += 1
  
    # Move to the next page
    page_num += 1

# Close the webdriver
driver.close()





