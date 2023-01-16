# Discord_Bot_Scrapper---A-Selenium-Discord-Bots-Webscrapper
A Selenium webscraper for Discord that scraps discord bots details like tags, votes, name, description, server count for your data projects.

This is a Python Selenium webscraper that grabs information on Discord bots from the website "top.gg" based on the user's input. The user can also stipulate how many pages of each search term they want to scrape.

You can see an example of the results of a scrape in the discord_bots.csv file. Note that the script is designed to extract 37,000 bots data but due to website restrictions like bot protection and IP bans the script might stop running at some point.

Running the Webscraper
Pre-Requisites
*Python Version: 3.9
*Package Requirements: Selenium

The script uses one main file : main.py runs the actual scraper. Note that in the main.py file there's a line of code to handle exceptions when the script is blocked or stopped, you can take this out if you want to.

Once you've made these adjustments, simply run the script - you'll see printouts for each bot that's scraped, as well as an overall summary for each page load.


Data Schema
There are 6 columns pulled by this webscraper:

| Column | Description | Data Type|
| --- | --- | --- |
| Name | name of the bot | string |
| Tags | tags of the bot | list |
| Votes | votes of the bot  | int |
| Description | Description of bot | string |
| Average Score |  average score of bot | if exist None otherwise float |
| Server Count | number of servers the bot is on | if exist None otherwise int |



Please feel free to use this webscraper as a starting point for your exploration and make adjustments to improve it!


Have fun and please feel free to reach out if you have any questions!
