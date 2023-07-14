import requests
from bs4 import BeautifulSoup
import re

def extract_pdf_links(url, session):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=re.compile(r'\.pdf$'))
    pdf_links = [link['href'] for link in links]
    return pdf_links

def scrape_website(url, email, password):
    session = requests.Session()
    
    # Login to the website
    login_data = {
        'email': email,
        'password': password
    }
    session.post('https://crm.tekkon.com.np/web/login', data=login_data)
    
    response = session.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # all_links = soup.find_all('a', href=True)
    # pdf_links = []
    
    # for link in all_links:
    #     href = link['href']
    #     if href.endswith('.pdf'):
    #         pdf_links.append(href)
    #     elif href.startswith('http') or href.startswith('https'):
    #         pdf_links.extend(extract_pdf_links(href, session))
    
    # return pdf_links

# Example usage
website_url = 'https://crm.tekkon.com.np/web#action=193&model=hr.job&view_type=kanban&cids=&menu_id=127'
login_email = 'peshal.nepal@tekkon.com.np'
login_password = 'Peshal@123'

pdf_links = scrape_website(website_url, login_email, login_password)
# for link in pdf_links:
#     print(link)