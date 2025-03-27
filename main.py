import re
import requests
import os
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

def extract_emails_from_text(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    return emails

def process_url(url):
    print(Fore.YELLOW + f"Processing URL: {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        emails = extract_emails_from_text(soup.get_text())
        return emails
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + f"Failed to retrieve the URL: {url}")
        return []

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        urls = f.read().splitlines()
    return urls

source = input("Enter website or file path: ")

if "," in source:
    urls = source.split(",")
    all_emails = []
    for url in urls:
        emails = process_url(url.strip())
        all_emails.extend(emails)
elif source.startswith("http"):
    all_emails = process_url(source)
else:
    urls = process_file(source)
    all_emails = []
    for url in urls:
        emails = process_url(url.strip())
        all_emails.extend(emails)

if all_emails:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Extracted Emails:")
    print("")
    for email in set(all_emails):
        print(Fore.GREEN + email)
    input("press enter to exit...")
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + "No emails found.")
    print("")
    input("press enter to exit...")