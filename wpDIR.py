import requests

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
        test_url = url + "/" + directory
        check_waf(test_url)
        try:
            response = requests.get(test_url)
            if response.status_code == 200:
                check += 1
                print("[+] Found accessible WP directory: " + test_url + " [+]\n")
            else:
                print("[!] Received status code: " + str(response.status_code) + " for URL: " + test_url + " [!]\n")
        except requests.exceptions.RequestException as e:
            print("[!] Error occurred while accessing URL: " + test_url + " - " + str(e) + " [!]\n")

    if check == 0:
        print("No WP directories found. :(\n")

def check_waf(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        print("[!] Possibly a WAF is present, the request was blocked. [!]\n")
    elif response.status_code == 200:
        print("[!] No signs of WAF. [!]\n")
    else:
        print("[!] Unable to determine if a WAF is present. [!]\n")

if __name__ == "__main__":
    url = input("[+] Enter a valid URL [+]\n")
    WPdir(url)
