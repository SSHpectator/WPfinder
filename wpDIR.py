import argparse
import requests
from bs4 import BeautifulSoup

# Definizione della classe per i colori del testo
class tcolor:
    yellow = '\33[33m'
    red = '\33[31m'
    green = '\33[32m'
    end = '\33[0m'  # Per riportare il colore al valore predefinito

def check_wordpress(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_generator = soup.find('meta', attrs={'name': 'generator'})
            if meta_generator and 'WordPress' in meta_generator['content']:
                return True
            else:
                return False
        else:
            print(tcolor.red + "[-]Error during the retrieving of the site. Status code:", response.status_code + tcolor.end)
            return False
    except requests.RequestException as e:
        print(tcolor.red + "[-]Error during the HTTP request:", e + tcolor.end)
        return False

def check_waf(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        print(tcolor.red + "[!] A Web Application Firewall (WAF) is possibly present, the request was blocked. [!]\n" + tcolor.end)
    elif response.status_code != 200:
        print(tcolor.yellow + "[!] Unable to determine if a WAF is present. Received status code:", response.status_code, "[!]\n" + tcolor.end)
    else:
        print(tcolor.green + "[!] No signs of WAF detected. [!]\n" + tcolor.end)

def WPdir(url):
    directories = [
        "wp-admin.php",
        "wp-config.php",
        "wp-content/uploads",
        "wp-load",
        "wp-signup.php",
        "wp-JSON",
        "wp-includes",
        "index.php",
        "wp-login.php",
        "wp-links-opml.php",
        "wp-activate.php",
        "wp-blog-header.php",
        "wp-cron.php",
        "wp-links.php",
        "wp-mail.php",
        "xmlrpc.php",
        "wp-settings.php",
        "wp-trackback.php",
        "wp-signup.php",
        "/wp-json/wp/v2/users",
        "/wp-json/wp/v2/plugins",
        "/wp-json/wp/v2/themes",
        "/wp-json/wp/v2/comments"
    ]

    check = 0
    for directory in directories:
        test_url = url.rstrip('/') + '/' + directory
        check_waf(test_url)
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                check += 1
                print(tcolor.green + "[+] Found accessible WP directory:", test_url, "[+]\n" + tcolor.end)
            else:
                print(tcolor.yellow + "[!] Received status code:", response.status_code, "for URL:", test_url, "[!]\n" + tcolor.end)
        except requests.exceptions.RequestException as e:
            print(tcolor.red + "[!] Error occurred while accessing URL:", test_url, "-", e, "[!]\n" + tcolor.end)

    if check == 0:
        print("No WP directories found. :(\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect WordPress directories")
    parser.add_argument('url', help='URL of the website to check')
    args = parser.parse_args()
    
    url = args.url

    if check_wordpress(url):
        WPdir(url)
    else:
        print(tcolor.red + "[-] This website is not a WordPress website ! [-]\n" + tcolor.end)
