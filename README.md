The program works as follows:

Imports the required modules: BeautifulSoup, requests, and re.
Uses the requests module to retrieve the webpage content from the URL https://www.earningswhispers.com/calendar.
Processes the retrieved HTML code into a soup object using the BeautifulSoup module.
Uses the find() method with the id parameter to locate the first <ul> element with an id attribute equal to epscalendar.
Finds all the <div> elements with a class attribute equal to company, ticker, time, revgrowthprint, and growth using the findAll() method and stores them in separate lists.
Initializes five separate lists to store the data for each company.
Iterates over each of the <div> elements in the revenue_growths_html and earnings_growths_html lists using a for loop.
Uses the find() method to locate a <script> element containing the showepsgrowth text and the re module to extract the expected earnings growth data from the script.
Adds the extracted data to the relevant list.
Combines the five lists for each company using the zip() function to create a list of tuples.
Prints the resulting earnings_list to the console.
Saves the data to a CSV file called earnings.csv using the open() function and with statement.
