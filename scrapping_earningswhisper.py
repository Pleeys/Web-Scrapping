from bs4 import BeautifulSoup 
import requests
import re

source = requests.get('https://www.earningswhispers.com/calendar')
soup = BeautifulSoup(source.content, 'lxml')

espcalendar = soup.find('ul', id='epscalendar')

companies_html = soup.findAll('div', class_='company')
tickers_html = soup.findAll('div', class_='ticker')
times_html = soup.findAll('div', class_='time')
revenue_growths_html = soup.findAll('div', class_='revgrowthprint')
earnings_growths_html = soup.findAll('div', class_='growth')

companies = ['Company name']
tickers = ['Ticker']
times = ['Time']
revenue_growths = ['Expected Revenue Growth']
earnings_growths = ['Expected Earnings Growth']

for company in companies_html:
    companies.append(company.text)

for ticker in tickers_html:
    tickers.append(ticker.text)

for time in times_html:
    times.append(time.text)

for revenue_growth in revenue_growths_html:
    revenue_growths.append(revenue_growth.text)

for earning in earnings_growths_html:
    earning_script = earning.find('script', string=lambda text: text and 'showepsgrowth' in text)
    if earning_script:
        earning_text = re.search(r'showepsgrowth\("[^"]*",\s*"([^"]*)"\);', earning_script.string)
        if earning_text:
            earnings_growths.append(earning_text.group(1))

earnings_list = list(zip(companies, tickers, times, revenue_growths, earnings_growths))

print(earnings_list)

filename = 'earnings.csv'

with open(filename, 'w') as f:
    for item in earnings_list:
        line = ' | '.join(item)  
        f.write(line + '\n')