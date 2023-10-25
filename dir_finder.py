import requests

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def dir_searcher(website, my_list):
    for i in my_list:
        res = requests.get(f"{website}/{i}")
        print(f"{RED}[+] {res.status_code} {RESET} : {RED} {res.url} {RESET}")
        if res.status_code == 200:
            print(f"{GREEN}[+] {res.url} {RESET} : {GREEN} [+] {res.status_code} {RESET}")

def main():
    choice = int(input("""
    [1/2]
    1- Your Wordlists
    2- BruteForce
    Enter your choice: """))

    my_list = [
        "index", "images", "download", "2006", "news", "crack", "serial",
        "warez", "full", "12", "contact", "about", "search", "spacer", "privacy",
        "11", "logo", "blog", "new", "10", "cgi-bin", "faq", "rss", "home", "img",
        "default", "2005", "products", "sitemap", "archives", "google", "bullet",
        "about_us", "service", "faculty", "special", "folder", "book", "report", "50",
        "servlet", "java", "38", "world", "issues", "microsoft", "m", "f", "guide", "e",
        "memberlist", "es", "art", "show", "pubs", "section", "47", "43", "buy", "lg",
        "photo", "international", "employment", "partner", "trans", "demo", "gfx", "45",
        "tv", "cart", "local", "board", "documentation", "podcast", "44", "flags", "cs",
        "images01", "videos", "51", "perl", "46", "posts", "cgi", "current", "pix", "49",
        "shopping", "lists", "start", "multimedia", "g", "promo", "site_map", "55", "59",
        "title", "topic", "opinion", "management", "headers", "add", "icon", "redirect", "60",
        "enterprise", "results", "all", "tag", "authors", "54", "53", "code", "pl", "consumer",
        "57", "61", "h", "63", "52", "whatsnew", "details", "affiliate", "pictures", "password",
        "sp", "56", "policies", "more", "mp3", "click", "tests", "free", "wp-login", "1999", "back",
        "smilies", "personal", "poll", "skins", "storage", "bin", "mac", "albums", "author",
        "counter", "64", "printer", "display", "howto", "conferences", "66", "radio", "apple",
        "Products", "58", "maps", "advisories", "webapp", "l", "guides", "group", "97", "forumdisplay",
        "96", "70", "shared", "ftp", "w", "magazine", "62", "columns", "traffic", "65", "thumbs",
        "69", "72", "plugins", "89", "n", "groups", "impressum", "ad", "Search", "food", "73", "python",
        "id", "press_releases", "75", "hosting", "77", "sites", "review", "feature", "99", "100", "68",
        "67", "87", "v", "specials", "81", "91", "unix", "money", "71", "courses", "css", "rss2", "80",
        "project", "programming", "78", "delicious", "accessibility", "85", "76", "90", "mission",
        "purchase", "Software", "marketing", "information", "alerts", "law", "bio", "template", "84",
        "customers", "82", "74", "presentations", "server", "icom_includes", "ajax", "government",
        "rules", "corrections", "tr", "mirrors", "pc", "footers", "right", "computers", "wordpress", "79",
        "cat", "spyware", "88", "Contact", "95", "98", "my", "About", "ss", "Security", "86", "schedule",
        "devx_foot2", "icom_foot", "grcom_foot", "ruledivide_foot", "out", "earthweb_foot2", "u", "team",
        "ca", "bottom", "test", "newsroom", "networking", "edit", "92", "Privacy", "classifieds", "virus",
        "humor", "z", "imgs", "tos", "webcasts", "read", "journal", "family", "crypto", "event", "updates",
        "credits", "pipermail", "icon_smile", "students", "101", "survey", "93", "europe", "includes", "log",
        "used-cars", "yahoo", "interviews", "reference", "program", "irc", "83", "pdfs", "pic", "headlines",
        "1998", "source", "transparent", "rss20", "tutorial", "hp", "finance", "toc", "development", "Index", "q",
        "Music", "94", "contents", "layout", "membership", "digg", "soft", "benefits", "game", "entry", "engine",
        "mediakit", "editorial", "Articles", "j", "clients", "reg", "reklama", "license", "tags", "navigation",
        "k", "loading", "traceroute", "core", "applications", "quotes", "logo2", "line", "college", "ws", "friends",
        "sections", "item", "tracker", "1x1", "live", "sport", "Business", "reprints", "computer", "privacy-policy",
        "desktop", "groupcp", "action", "system", "108", "contact-us", "104", "bios", "viewonline", "forward", "00",
        "sales", "install", "cover", "letters", "shim", "small", "empty", "lib", "mt", "110", "pressreleases", "developer",
        "gif", "ru", "opensource", "105", "manual", "lastpost", "Help", "net", "columnists", "privmsg", "smile", "tour", "up",
        "thread", "get", "release", "cc", "hr", "do", "announcements", "document", "trackback", "form", "Games", "access", "o",
        "arts", "109", "firefox", "whosonline", "subscriptions", "utilities", "188", "file", "fun", "dvd", "103", "pressroom",
        "status", "Internet", "conference", "index1", "phone", "111", "iraq", "left", "Members", "pricing", "backend", "find",
        "office", "pda", "date", "ecommerce", "magazines", "agenda", "kids", "src", "150", "voip", "wp-includes", "profiles", "work",
        "star", "portfolio", "house", "component", "wp", "update", "standards", "auto", "golf", "dl", "Main_Page", "thumbnails",
        "avatars", "usa", "114", "br", "125", "cars", "realestate", "redir", "reply", "toolbar", "problems", "Downloads", "site-map",
        "pt", "123", "computing", "Education", "Sports", "galleries", "linktous", "database", "folder_big", "insurance", "sponsor", "Login",
        "quote", "daily", "next", "102", "155", "corp", "bloggers", "120", "dev", "106", "C", "alumni", "frontpage", "107", "cms", "football",
        "latest", "count", "uncategorized", "client", "Resources", "Download", "db", "black", "state", "ContactUs", "phishing", "secure",
        "151", "gifs", "PrivacyPolicy", "polls", "121", "licensing", "custom", "life", "intl", "vote", "sub", "113", "asp", "white", "webmaster",
        "adv", "language", "115", "servers", "112", "packages", "156", "donations", "termsofuse", "jp", "resource", "142", "firewall", "130",
        "aboutUs", "168", "plus", "down", "144", "speakers", "browser", "commentary", "126", "ipod", "tuning", "popular", "admin"
        ]

    if choice == 1:
        file_path = input("Enter the path to the wordlist file: ")
        try:
            with open(file_path) as wrd:
                wordlist = wrd.read().split()  # Split the wordlist into separate words
                website = input("Enter the target website (e.g., http://example.com): ")
                dir_searcher(website, wordlist)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    elif choice == 2:
        website = input("Enter the target website (e.g., http://example.com): ")
        dir_searcher(website, my_list)

if __name__ == "__main__":
    main()
