import requests
from Godtool import check_subdomain
from dir_finder import dir_searcher
from os import system
from time import sleep
import subprocess

RED = "\033[31m"
GREEN = "\033[32m"
Blue = "\033[1;36;40m"
RESET = "\033[0m"
system("cls||clear")
print(f"""
{RED}
 @@@@@@   @@@       @@@@@@@@@@   @@@@@@        @@@  @@@@@@@@  @@@  @@@  
@@@@@@@@  @@@       @@@@@@@@@@@  @@@@@@@       @@@  @@@@@@@@  @@@  @@@  
@@!  @@@  @@!       @@! @@! @@!      @@@       @@!       @@!  @@!  @@@  
!@!  @!@  !@!       !@! !@! !@!      @!@       !@!      !@!   !@!  @!@  
@!@!@!@!  @!!       @!! !!@ @!@  @!@!!@        !!@     @!!    @!@!@!@!  
!!!@!!!!  !!!       !@!   ! !@!  !!@!@!        !!!    !!!     !!!@!!!!  
!!:  !!!  !!:       !!:     !!:      !!:       !!:   !!:      !!:  !!!  
:!:  !:!   :!:      :!:     :!:      :!:  !!:  :!:  :!:       :!:  !:!  
::   :::   :: ::::  :::     ::   :: ::::  ::: : ::   :: ::::  ::   :::  
 :   : :  : :: : :   :      :     : : :    : :::    : :: : :   :   : :                                                                                                                            
{RESET}
""")

def check_parameter(domain, param):
    url = f"https://{domain}/{param}"
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN} {response.status_code} : [+] Found Parameter {param} In Domain {url} - Accessible{RESET}")
        elif response.status_code == 301:
            print(f"{Blue} {response.status_code} : [!] Found Parameter {param} But It Has A Redirect {url}{RESET}")
        elif response.status_code == 404:
            print(f"{RED} {response.status_code} : [-] Nothing Here {url}{RESET}")
        else:
            print(f"[-] {RED} {response.status_code} : Unexpected Status Code for Parameter {param} in Domain {domain}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error occurred while checking {url}: {str(e)}{RESET}")

    '''except requests.exceptions.RequestException as e:
        print(f"{RED}[-] Error occurred while checking {url}: {str(e)}{RESET}")'''
def main():
    choose = input(f"""
        {GREEN}
        1- SubDomain Finder
        2- Parameter Finder
        3- Directory Finder
        4- Sql Finder With Sqlmap
        5- Quit
        : {RESET}""")
    

    
    if choose == "1":
        domain = input(f"{Blue}[+] Please Enter Your Target Domain... - > : {RESET}")
        subdomains = domain.split('.')
        main_domain = subdomains[-2] + "." + subdomains[-1]

        found_subdomains = []

        choice = input(f"""
        {GREEN}
        1- Bruteforce
        2- Your Wordlist
        : {RESET}""")
        wordlist = [
            "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk", "ns2",
            "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test", "ns", "blog", "pop3", 
            "dev", "www2", "admin", "forum", "news", "vpn", "ns3", "mail2", "new", "mysql", "old", 
            "lists", "support", "mobile", "mx", "static", "docs", "beta", "shop", "sql", "secure", 
            "demo", "cp", "calendar", "wiki", "web", "media", "email", "images", "img", "www1", 
            "intranet", "portal", "video", "sip", "dns2", "api", "cdn", "stats", "dns1", "ns4", 
            "www3", "dns", "search", "staging", "server", "mx1", "chat", "wap", "my", "svn", "mail1", 
            "sites", "proxy", "ads", "host", "crm", "cms", "backup", "mx2", "lyncdiscover", "info", 
            "apps", "download", "remote", "db", "forums", "store", "relay", "files", "newsletter", 
            "app", "live", "owa", "en", "start", "sms", "office", "exchange", "ipv4", "mail3", 
            "help", "blogs", "helpdesk", "web1", "home", "library", "ftp2", "ntp", "monitor", 
            "login", "service", "correo", "www4", "moodle", "it", "gateway", "gw", "i", "stat", 
            "stage", "ldap", "tv", "ssl", "web2", "ns5", "upload", "nagios", "smtp2", "online", 
            "ad", "survey", "data", "radio", "extranet", "test2", "mssql", "dns3", "jobs", "services", 
            "panel", "irc", "hosting", "cloud", "de", "gmail", "s", "bbs", "cs", "ww", "mrtg", 
            "git", "image", "members", "poczta", "s1", "meet", "preview", "fr", "cloudflare-resolve-to", 
            "dev2", "photo", "jabber", "legacy", "go", "es", "ssh", "redmine", "partner", "vps", 
        ]
        found_subdomains = []
        if choice == '1':
            for subdomain in wordlist:
                result = check_subdomain(subdomain, domain)
                if result:
                    found_subdomains.append(result)
        elif choice == '2':
            custom_wordlist = input(f"{GREEN}[+] Please enter your custom wordlist (comma-separated): {RESET}")
            custom_wordlist = custom_wordlist.split(',')
            for subdomain in custom_wordlist:
                result = check_subdomain(subdomain.strip(), domain)
                if result:
                    found_subdomains.append(result)
        else:
            print("Invalid choice. Please enter 1 for Bruteforce or 2 for a custom wordlist.")
        if found_subdomains:
            print(f"{GREEN}[+] Found Subdomains:{RESET}")
            for subdomain in found_subdomains:
                print(subdomain)
        else:
            print(f"{RESET}[+] No subdomains were found.{RESET}")

    elif choose == '2':
        domain = input("Enter the target domain: ")
        param_list =  ["about.php?cartID=", "accinfo.php?cartId=", "acclogin.php?cartID=", "add.php?bookid=", "add_cart.php?num=", "addcart.php?", "addItem.php", "add-to-cart.php?ID=", "addToCart.php?idProduct=", "addtomylist.php?ProdId=", "adminEditProductFields.php?intProdID=", "advSearch_h.php?idCategory=", "affiliate.php?ID=", "affiliate-agreement.cfm?storeid=", "affiliates.php?id=", "ancillary.php?ID=", "archive.php?id=", "article.php?id=", "phpx?PageID", "basket.php?id=", "Book.php?bookID=", "book_list.php?bookid=", "book_view.php?bookid=", "BookDetails.php?ID=", "browse.php?catid=", "browse_item_details.php", "Browse_Item_Details.php?Store_Id=", "buy.php?", "buy.php?bookid=", "bycategory.php?id=", "cardinfo.php?card=", "cart.php?action=", "cart.php?cart_id=", "cart.php?id=", "cart_additem.php?id=", "cart_validate.php?id=", "cartadd.php?id=", "cat.php?iCat=", "catalog.php", "catalog.php?CatalogID=", "catalog_item.php?ID=", "catalog_main.php?catid=", "category.php", "category.php?catid=", "category_list.php?id=", "categorydisplay.php?catid=", "checkout.php?cartid=", "checkout.php?UserID=", "checkout_confirmed.php?order_id=", "checkout1.php?cartid=", "comersus_listCategoriesAndProducts.php?idCategory=", "comersus_optEmailToFriendForm.php?idProduct=", "comersus_optReviewReadExec.php?idProduct=", "comersus_viewItem.php?idProduct=", "comments_form.php?ID=", "contact.php?cartId=", "content.php?id=", "customerService.php?ID1=", "default.php?catID=", "description.php?bookid=", "details.php?BookID=", "details.php?Press_Release_ID=", "details.php?Product_ID=", "details.php?Service_ID=", "display_item.php?id=", "displayproducts.php", "downloadTrial.php?intProdID=", "emailproduct.php?itemid=", "emailToFriend.php?idProduct=", "events.php?ID=", "faq.php?cartID=", "faq_list.php?id=", "faqs.php?id=", "feedback.php?title=", "freedownload.php?bookid=", "fullDisplay.php?item=", "getbook.php?bookid=", "GetItems.php?itemid=", "giftDetail.php?id=", "help.php?CartId=", "home.php?id=", "index.php?cart=", "index.php?cartID=", "index.php?ID=", "info.php?ID=", "item.php?eid=", "item.php?item_id=", "item.php?itemid=", "item.php?model=", "item.php?prodtype=", "item.php?shopcd=", "item_details.php?catid=", "item_list.php?maingroup", "item_show.php?code_no=", "itemDesc.php?CartId=", "itemdetail.php?item=", "itemdetails.php?catalogid=", "learnmore.php?cartID=", "links.php?catid=", "list.php?bookid=", "List.php?CatID=", "listcategoriesandproducts.php?idCategory=", "modline.php?id=", "myaccount.php?catid=", "news.php?id=", "order.php?BookID=", "order.php?id=", "order.php?item_ID=", "OrderForm.php?Cart=", "page.php?PartID=", "payment.php?CartID=", "pdetail.php?item_id=", "powersearch.php?CartId=", "price.php", "privacy.php?cartID=", "prodbycat.php?intCatalogID=", "prodetails.php?prodid=", "prodlist.php?catid=", "product.php?bookID=", "product.php?intProdID=", "product_info.php?item_id=", "productDetails.php?idProduct=", "productDisplay.php", "productinfo.php?item=", "productlist.php?ViewType=Category&CategoryID=", "productpage.php", "products.php?ID=", "products.php?keyword=", "products_category.php?CategoryID=", "products_detail.php?CategoryID=", "productsByCategory.php?intCatalogID=", "prodView.php?idProduct=", "promo.php?id=", "promotion.php?catid=", "pview.php?Item=", "resellers.php?idCategory=", "results.php?cat=", "savecart.php?CartId=", "search.php?CartID=", "searchcat.php?search_id=", "Select_Item.php?id=", "Services.php?ID=", "shippinginfo.php?CartId=", "shop.php?a=", "shop.php?action=", "shop.php?bookid=", "shop.php?cartID=", "shop_details.php?prodid=", "shopaddtocart.php", "shopaddtocart.php?catalogid=", "shopbasket.php?bookid=", "shopbycategory.php?catid=", "shopcart.php?title=", "shopcreatorder.php", "shopcurrency.php?cid=", "shopdc.php?bookid=", "shopdisplaycategories.php", "shopdisplayproduct.php?catalogid=", "shopdisplayproducts.php", "shopexd.php", "shopexd.php?catalogid=", "shopping_basket.php?cartID=", "shopprojectlogin.php", "shopquery.php?catalogid=", "shopremoveitem.php?cartid=", "shopreviewadd.php?id=", "shopreviewlist.php?id=", "ShopSearch.php?CategoryID=", "shoptellafriend.php?id=", "shopthanks.php", "shopwelcome.php?w=", "ShowItem.php?id=", "showproduct.php?cat=", "site.php?id=", "staff.php?cartId=", "store.php?catID=", "store.php?catid=", "store_bycat.php?catid=", "store_details.php?catid=", "store_listing.php?catid=", "store_results.php?cat_id=", "storecat.php?cat_id=", "storefront.php?id=", "storefront.php?storeid=", "storeitem.php?item=", "storesearch.php?storeID=", "StoreSummary.php?Title=", "support.php?=", "team.php?cartId=", "tellafriend.php?id=", "thankyou.php?cartid=", "top10.php?cat=", "updatebasket.php?book=", "updates.php?ID=", "view.php?Item=", "view_cart.php?userID=", "View_Shop.php?ID=", "view_product.php?product=", "viewitem.php?recor=", "Viewitem.php?recor=", "viewitems.php?Category=", "vq2-catalog_category_view.php?cPath=", "waf.php?id=", "webpage.php?id=", "website.php?id=", "whatsnew.php?id=", "productList.php?category=", "window.php?BookID=", "yourdomain.com/catalog.php?", "zoom.php?cartID=", "addevent.php?intEventID=", "affiche.php?no=", "index1.php?link=", "event.php?EventID=", "product_ranges_view.php?ID=", "productDisplay.php?ProductID=", "index1.php?link=", "hosting_info.php?ID=", "zhanka?bookid=", "proddetail.php?prod=", "big.php?item=", "newsid=", "faq2.php?id=", "productinfo.php?id=", "productinfo.php?item=", "inc_product_detail.php?id=", "viewprod.php?idProduct=", "db.php?id=", "Show_Items.php?id=", "page.php?PartID=", "theme.php?cat=", "clubpage.php?cid=", "viewevent.php?EventID=", "articles.php?id=", "collectibles.php?ID=", "page.php?PartID=", "products_id=", "collectionitem.php?id=", "document.php?id=", "product.php?pro_id=", "collection.php?id=", "productitem.php?cat=", "productpage.php?id=", "team.php?cartId=", "products_id=", "productlist.php?id=", "ecom.php?prodID=", "products.php?page=", "productdetail.php?item=", "product_list.php?Item=", "viewcategory.php?id=", "view_products.php?category=", "productlist.php?CAT=", "pr.php?catid=", "productlist.php?catid=", "productlist.php?AdId=", "productdetail.php?CAT=", "productdetail.php?PID=", "commerce.php?dept=", "products.php?cat=", "product.php?ItemID=", "index.php?cat=", "ViewProduct.php?ref=", "Event.php?ID=", "productdetail.php?sku=", "view_product.php?code=", "news-detail.php?id=", "preview.php?id=", "eventDetails.php?id=", "productinfo.php?item_id=", "product_details.php?item_id=", "ProductDetails.php?ID=", "page.php?PartID=", "itemDetail.php?item=", "default.php?cPath=", "products.php?page=", "product.php?ID=", "productinfo.php?id=", "product-detail.php?id=", "product-list.php?item=", "productlisting.php?item=", "productinfo.php?catalog=", "productinfo.php?cat=", "product_info.php?item=", "product.php?product=", "ProductDetails.php?ID=", "item.php?ID=", "productinfo.php?prodID=", "productdetails.php?ref=", "ProductDetails.php?cat=", "products.php?id=", "bookDetails.php?ID=", "productDetail.php?ItemID=", "item.php?ID=", "products.php?id=", "products.php?ID=", "show_item.php?item=", "view_product.php?num=", "productinfo.php?pid=", "productinfo.php?cat=", "product.php?item=", "show_product.php?item=", "products.php?id=", "index.php?Itemid=", "shop.php?c=", "product_list.php?CategoryID=", "products.php?Cat=", "product_details.php?prodid=", "products.php?ID=", "product_info.php?cPath=", "item.php?catid=", "product.php?cPath=", "products.php?cPath=", "storepage.php?ID=", "show_product.php?id=", "products.php?ref=", "product.php?item=", "product.php?sku=", "productinfo.php?CartId=", "productinfo.php?item=", "product.php?product_id=", "storepage.php?pid=", "productdetails.php?cat=", "product.php?cPath=", "viewitem.php?PID=", "products.php?cPath=", "productDetails.php?item=", "itemDetail.php?item=", "default.php?CategoryID=", "product_list.php?category=", "ProductDetails.php?ID=", "index.php?cart=", "product_detail.php?id=", "product.php?cat=", "page.php?PartID=", ]
        for param in param_list:
            check_parameter(domain, param)

    elif choose == "3":
        my_list = [
        "index", "images", "download", "2006", "news", "crack", "serial",
        "warez", "full", "12", "contact", "about", "search", "spacer", "privacy",
        "11", "logo", "blog", "new", "10", "cgi-bin", "faq", "rss", "home", "img",
        "default", "2005", "products", "sitemap", "archives", "google", "bullet",
        "about_us", "service", "faculty", "special", "folder", "book", "report", "50",
        "servlet", "java", "38", "world", "issues", "microsoft", "m", "f", "guide", "e",
        "memberlist", "es", "art", "show", "pubs", "section", "47", "43", "buy", "lg",
        "title", "topic", "opinion", "management", "headers", "add", "icon", "redirect", "60",
        "enterprise", "results", "all", "tag", "authors", "54", "53", "code", "pl", "consumer",
        "57", "61", "h", "63", "52", "whatsnew", "details", "affiliate", "pictures", "password",
        "sp", "56", "policies", "more", "mp3", "wp-login", "1999", "back", "smilies", "personal",
        "poll", "skins", "storage", "bin", "mac", "albums", "author", "counter", "64", "printer",
        "display", "howto", "conferences", "66", "radio", "apple", "Products", "58", "maps",
        "advisories", "webapp", "l", "guides", "group", "97", "forumdisplay", "96", "70", "shared",
        "ftp", "w", "magazine", "62", "columns", "traffic", "65", "thumbs", "69", "72", "plugins",
        "89", "n", "groups", "impressum", "ad", "Search", "food", "73", "python", "id", "press_releases",
        "75", "hosting", "77", "sites", "review", "feature", "99", "100", "68", "67", "87", "v",
        "specials", "81", "91", "unix", "money", "71", "courses", "css", "rss2", "80", "project",
        "programming", "78", "delicious", "accessibility", "85", "76", "90", "mission", "purchase",
        "Software", "marketing", "information", "alerts", "law", "bio", "template", "84", "customers",
        "82", "74", "presentations", "server", "icom_includes", "ajax", "government", "rules", "corrections",
        "tr", "mirrors", "pc", "footers", "right", "computers", "wordpress", "79", "cat", "spyware", "88",
        "Contact", "95", "98", "my", "About", "ss", "Security", "86", "schedule", "devx_foot2", "icom_foot",
        "grcom_foot", "ruledivide_foot", "out", "earthweb_foot2", "u", "team", "ca", "bottom", "test", "newsroom",
        "networking", "edit", "92", "Privacy", "classifieds", "virus", "humor", "z", "imgs", "tos", "webcasts",
        "read", "journal", "family", "crypto", "event", "updates", "credits", "pipermail", "icon_smile", "students",
        "101", "survey", "93", "europe", "includes", "log", "used-cars", "yahoo", "interviews", "reference", "program",
        "irc", "83", "pdfs", "pic", "headlines", "1998", "source", "transparent", "rss20", "tutorial", "hp", "finance",
        "toc", "development", "Index", "q", "Music", "94", "contents", "layout", "membership", "digg", "soft", "benefits",
        "game", "entry", "engine", "mediakit", "editorial", "Articles", "j", "clients", "reg", "reklama", "license", "tags",
        "navigation",
        ]
        website = input("Enter the target website (e.g., http://example.com): ")
        dir_searcher(website, my_list)
    elif choose == '4':
        def site_url():
            target_site = input(f"""{RED}[+] Enter Your Target Site

            example

            {RED}https://alm3jzh.com/php?=example{RESET}

            - > :  """)
            sleep(2)
            print((f"{GREEN}[!] The Site Is Under Reconnaissance And In Danger !!!!"))
            sleep(2)
            print(f"{RED}[!] {RESET}The Site Is Well Done ........")
            subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs'])

            error = f"{Blue}[*] {RESET}ending @ 17:27:41 /2023-10-18/"

            print(f"Do you want to Upgrade The Scan ? {Blue}[Y/n]{RESET} : ")
            user_input = input().strip().lower()  # Get user input and convert to lowercase

            if user_input == 'y':
                subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs', '--tamper=space2comment', '--level=3'])
                # Add your installation logic here
            elif user_input == 'n':
                print(f"{RED}[+]Bey!!")
                sleep(5)
                return  # Return from the function to exit it
            else:
                print(f"{RED}Invalid input. Please enter 'Y' or 'n.{RESET}")

        site_url()

    

if __name__ == "__main__":
    main()