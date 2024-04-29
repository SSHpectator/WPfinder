import requests


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

url = input("Inserisci un URL valido. \n")
check = 0

for i in list:
    url += i
    x = requests.get(url)
    if(x.status_code == 200):
        check + 1
        print(x.url)

if(check == 0):
    print("Nessuna directory WP trovata. :(\n")