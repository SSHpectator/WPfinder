import requests

def WPdir(url):
    list = [
    "wp-admin.php",
    
     "wp-config.php",
    
     "wp-content/uploads",
    
     "Wp-load",
    
     "wp-signup.php",
    
     "Wp-JSON",
    
     "wp-includes [directory]",
    
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
    
     "Wp-signup.php",
    
     "/wp-json/wp/v2/users",
    
     "/wp-json/wp/v2/plugins",
    
     "/wp-json/wp/v2/themes",
    
       "/wp-json/wp/v2/comments",
    ]
    
    url = input("[+] INSERT A VALID URL [+]\n")
    check = 0

    tmp = url
    
    for i in list:
        url += i
        check_waf(url)
        x = requests.get(url)
        if(x.status_code == 200):
            check + 1
            print("[+] I've found a WP dir: " + url + " [+]\n")
        else:
            print("[!] I've received the following code: " + str(x.status_code) + " and the URL was: " + url + " [!]\n")
        url = tmp
    
    if(check == 0):
        print("[+]I DIDN'T FIND ANY WP DIRECTORY FOR YOU :( [+]\n")

def check_waf(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        print("[!] Possible presence of WAF, the request has been blocked. [!]\n")
    elif response.status_code == 200:
        print("[!] No presence of WAF. [!]\n")
    else:
        print("[!] It was not possible to determine if there is a WAF or not. [!]\n")

if __name__ == "__main__":
    url = input("[+] Insert a valid URL [+]\n")
    WPdir(url)
