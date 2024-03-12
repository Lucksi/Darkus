# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023-2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import requests
import os
from bs4 import BeautifulSoup as soup
import json
from time import sleep
import base64
import hashlib


class Utils:
    YELLOW = "\033[0;93m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"

    @staticmethod
    def Clear_Screen():
        os.system("cls" if os.name == "nt" else "clear")

class Engine:
    proxy = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    headers = {
        "Useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    }
    count = 1

    @staticmethod
    def encoding(report,name):
        quest = int(input(Utils.BLUE + "\n[?]" + Utils.WHITE + "Do you want to encode the {} report(1)Yes(2)No?".format(name) + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
        if quest == 1:
            EncodedFile = report.replace(".txt", ".Dk")
            f = open(report, "r+")
            reader = f.read()
            f.close()
            print(Utils.GREEN + "\n[+]" +
                      Utils.WHITE + "Encoding report...")
            sleep(3)
            encodingString = reader.encode("utf-8")
            Base64_Byte = base64.b64encode(encodingString)
            FinalString = Base64_Byte.decode("utf-8")
            f = open(EncodedFile, "w+", encoding="ascii")
            f.write(FinalString)
            f.close()
            print(Utils.YELLOW + "[v]" + Utils.WHITE +
                      "Report Encoded: {}".format(Utils.GREEN + EncodedFile.replace("output/","")))
            os.remove(report)
            print(Utils.GREEN + "\n[+]" + Utils.WHITE + "Report saved in: {}".format(
                Utils.GREEN + EncodedFile))
        else:
            print(Utils.GREEN + "\n[+]" + Utils.WHITE + "Report saved in: {}".format(
                Utils.GREEN + report))
    @staticmethod
    def HtmlReport(report,name):
        content = """
        <!--This Report has been created with Darkus
Download link:https://github.com/Lucksi/Darkus-->
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=0.9">
                <title>Darkus Report</title>
                <style>
                    body{
                        background-color: rgba(0, 0, 0, 0.836);
                    }

                    h1{
                        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                        color:red
                    }

                    p,h3,h4{
                        color:white;
                        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;

                    }

                    p{
                        font-size: 15px;
                    }

                    h3{
                        font-size: 25px;
                        font-weight: bold;
                    }

                    h4{
                        font-size: 18px;
                        font-weight: bold;
                    }

                    .results{
                        display: block;
                        height: fit-content;
                        width:fit-content;
                        border: 3px solid white;
                        border-radius: 20px;
                        background-color: black;
                    }

                     .results p,h4{
                        margin-left:10px;
                        margin-top:-10px;

                    }

                    .results h4{
                         margin-top:-5px;
                    }

                    a{
                        text-decoration:none;
                        color: #2779F6;
                    }
               </style>
            </head>
            <body>
                <h3>Onion Links found</h3>
                <h3>Report Generated with <a href = 'https://github.com/Lucksi/Darkus' target = 'blank'>Darkus</a></h4>
                <div class = 'results'>"

        """
        htmlrep = report.replace(".txt",".html")
        f = open(htmlrep,"w")
        f.write(content)
        f.close()
        return htmlrep
    
    @staticmethod
    def HashCheck(url):
        report = "output/Banned.txt"
        md5url = hashlib.md5(url.encode('utf-8')).hexdigest()
        print(Utils.GREEN + "\n[+]" + Utils.WHITE + "Url Hashed: {}".format(Utils.GREEN + md5url + Utils.WHITE))
        CheckUrl = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/blacklist/banned/"
        try:
            req = requests.get(url = CheckUrl, proxies = Engine.proxy,headers=Engine.headers)
            if md5url in req.text:
                print(Utils.RED + "\n[!]" + Utils.WHITE + "Url: {} Have been Banned it may be a dangerous link".format(Utils.GREEN + url + Utils.WHITE))
                f = open(report,"a")
                f.write(url + "\r\n")
            else:
                print(Utils.YELLOW + "\n[v]" + Utils.WHITE + "Url: {} Have not been Banned".format(Utils.GREEN + url + Utils.WHITE))
        except Exception as e:
            CheckUrl = "https://ahmia.fi/blacklist/banned/"
            try:
                req = requests.get(url = CheckUrl, proxies = Engine.proxy,headers=Engine.headers)
                if md5url in req.text:
                    print(Utils.RED + "[!]" + Utils.WHITE + "Url: {} Have been Banned it may be a dangerous link".format(Utils.GREEN + url + Utils.WHITE))
                    f = open(report,"a")
                    f.write(url + "\r\n")
                else:
                    print(Utils.YELLOW + "[v]" + Utils.WHITE + "Url: {} Have not been Banned".format(Utils.GREEN + url + Utils.WHITE))
            except Exception as e:
                print(Utils.RED + "[!]" + Utils.WHITE + "Something went wrong...\n")

    @staticmethod
    def Agreement():
        Utils.Clear_Screen()
        print(Utils.BLUE + "[I]" + Utils.WHITE + "Checking Usage Agreement")
        sleep(3)
        if os.path.exists("Agreement.txt"):
            sleep(3)
            f = open("Agreement.txt", "r", newline=None)
            content = f.read()
            f.close()
            if content != "Agreement Accepted":
                sleep(4)
                Utils.Clear_Screen()
                f = open("Banner/Banner.txt", "r", newline=None)
                for line in f:
                    sleep(0.3)
                    print(Utils.RED + line.replace("\n", ""))
                f.close()
                sleep(0.3)
                try:
                    choice = str(input(Utils.WHITE + "\nThis tool is intented only for research and educational purposes only. I do not assume any liability for any bad/illegal usage of this tool.\n\nPress" +
                                       Utils.GREEN + "(Y)" + Utils.WHITE + "To accept" + Utils.RED + "(N)" + Utils.WHITE + "To decline\n\n" + Utils.RED + "[:DARKUS:]" + Utils.WHITE + "-->"))
                    if choice == "Y" or choice == "y":
                        f = open("Agreement.txt", "w")
                        f.write("Agreement Accepted")
                        f.close()
                        Utils.Clear_Screen()
                        print(Utils.YELLOW +
                              "[v]" + Utils.WHITE + "Agreement Accepted")
                        sleep(2)
                    elif choice == "N" or choice == "n":
                        print(
                            Utils.RED + "Agreement refused You cannot use this tool if you do not accept this condition...\nExit")
                        exit()
                    else:
                        Engine.Agreement()
                except ValueError:
                    Engine.Agreement()
                except KeyboardInterrupt:
                    print("\n")
                    exit()
            else:
                print(Utils.YELLOW + "\n[v]" +
                      Utils.WHITE + "Usage Agreement found")
                sleep(2)
        else:
            Utils.Clear_Screen()
            f = open("Banner/Banner.txt", "r", newline=None)
            for line in f:
                sleep(0.3)
                print(Utils.RED + line.replace("\n", ""))
            f.close()
            sleep(0.3)
            try:
                choice = str(input(Utils.WHITE + "\nThis tool is intented only for research and educational purposes only. I do not assume any liability for any bad/illegal usage of this tool.\n\nPress" +
                                       Utils.GREEN + "(Y)" + Utils.WHITE + "To accept" + Utils.RED + "(N)" + Utils.WHITE + "To decline\n\n" + Utils.RED + "[:DARKUS:]" + Utils.WHITE + "-->"))
                if choice == "Y" or choice == "y":
                    f = open("Agreement.txt", "w")
                    f.write("Agreement Accepted")
                    f.close()
                    Utils.Clear_Screen()
                    print(Utils.YELLOW + "[v]" +
                          Utils.WHITE + "Agreement Accepted")
                    sleep(2)
                elif choice == "N" or choice == "n":
                    print(
                        Utils.RED + "Agreement refused You cannot use this tool if you do not accept this condition...\nExit\n")
                    exit()
                else:
                    Engine.Agreement()
            except ValueError:
                Engine.Agreement()
            except KeyboardInterrupt:
                print("\n")
                exit()

    @staticmethod
    def Banner():
        Utils.Clear_Screen()
        f = open("Banner/Banner.txt", "r", newline=None)
        for line in f:
            sleep(0.3)
            print(Utils.RED + line.replace("\n", ""))
        f.close()
        sleep(0.3)
        print(Utils.WHITE + "\nA Onion Websites Searcher\t  Coded by Lucksi")
        print(Utils.RED + "____________________________________________________")
        print(Utils.RED + "|" + Utils.WHITE + " Instagram:lucks_022" +
              Utils.RED + "                              |")
        print(Utils.RED + "|" + Utils.WHITE + " Email:lukege287@gmail.com" +
              Utils.RED + "                        |")
        print(Utils.RED + "|" + Utils.WHITE + " GitHub:Lucksi" +
              Utils.RED + "                                    |")
        print(Utils.RED + "|" + Utils.WHITE + " Twitter:@Lucksi_22" +
              Utils.RED + "                               |")
        print(Utils.RED + "|" + Utils.WHITE +
              " Linkedin:https://www.linkedin.com/in/lucksi" + Utils.RED + "      |")
        print(Utils.RED + "----------------------------------------------------")

    @staticmethod
    def dataExtraction(parser, name, report,out,htmlReport):
        f2 = open(htmlReport,"a")
        if name == "Ahmia":
            f = open(report, "a")
            f.write(name + " onion-links\r\n\n")
            i = 0
            list1 = parser.find_all("li", class_="result")
            for link in list1:
                title = link.find("h4").text.replace(" ", "").replace("\n", "")
                url = link.find("a")["href"].split("redirect_url=")[-1].lstrip()
                md5url = hashlib.md5(url.encode('utf-8')).hexdigest()
                description = link.find("p").text.replace("\n", "")
                timestamp = link.find("span", class_="lastSeen")[
                    "data-timestamp"].replace("\n", "").replace(" ", "")
                if out == 1:
                    print(Utils.GREEN + "[+]" +
                        Utils.WHITE + "Title: {}".format(Utils.GREEN + title))
                    print(Utils.YELLOW + "[v]" +
                        Utils.WHITE + "Url: {}".format(Utils.GREEN + url))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "Description: {}".format(Utils.GREEN + description))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "Timestamp: {}".format(Utils.GREEN + timestamp))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "MD5-url: {}\n".format(Utils.BLUE + md5url))
                f.write("Title: {}\r\n".format(title))
                f.write("Url: {}\r\n".format(url))
                f.write("Description: {}\r\n".format(description))
                f.write("Timestamp: {}\r\n".format(timestamp))
                f.write("MD5-Url: {}\r\n\n".format(md5url))

                f2.write("<h4>({})Title: {}</h4>".format(Engine.count,title))
                f2.write("<p>Url: {}</p>".format("<a href ='" + url + "' target = 'blank'>" + url + "</a>"))
                f2.write("<p>Description: {}</p>".format(description))
                f2.write("<p>Timestamp: {}</p>".format(timestamp))
                f2.write("<p>MD5-Url: <a>{}</a></p>".format(md5url))
                Engine.count = Engine.count + 1
                i = i + 1

        elif name == "Torch":
            f = open(report, "a")
            f.write(name + "onion-links\r\n\n")
            i = 0
            list1 = parser.find_all("div", class_="result mb-3")
            for link in list1:
                title = link.find("h5").text.replace(
                    "  ", "").replace("\n", "")
                url = link.find("a")["href"]
                description = link.find("p").text.replace("\n", "")
                md5url = hashlib.md5(url.encode('utf-8')).hexdigest()
                if out == 1:
                    print(Utils.GREEN + "[+]" +
                        Utils.WHITE + "Title: {}".format(Utils.GREEN + title))
                    print(Utils.YELLOW + "[v]" +
                        Utils.WHITE + "Url: {}".format(Utils.GREEN + url))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "Description: {}".format(Utils.GREEN + description))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "MD5-url: {}\n".format(Utils.BLUE + md5url))
                f.write("Title: {}\r\n".format(title))
                f.write("Url: {}\r\n".format(url))
                f.write("Description: {}\r\n".format(description))
                f.write("MD5-Url: {}\r\n\n".format(md5url))

                f2.write("<h4>({})Title: {}</h4>".format(Engine.count,title))
                f2.write("<p>Url: {}</p>".format("<a href ='" + url + "' target = 'blank'>" + url + "</a>"))
                f2.write("<p>Description: {}</p>".format(description))
                f2.write("<p>MD5-Url: <a>{}</a></p>".format(md5url))
                Engine.count = Engine.count + 1
                i = i+1

        elif name == "Torch-Images":
            report = report.replace(".txt","_image.txt")
            f = open(report, "a")
            f.write(name + " onion-links\r\n\n")
            i = 0
            list1 = parser.find_all("div", class_="imagehold")
            for link in list1:
                link2 = link.find_all("a")
                for link3 in link2:
                    title = link3.find("img")["alt"].replace(
                        "  ", "").replace("\n", "")
                    url = link3["href"]
                    image = link3.find("img")["src"]
                    md5url = hashlib.md5(url.encode('utf-8')).hexdigest()
                    if out == 1:
                        print(Utils.GREEN +
                            "[+]" + Utils.WHITE + "Title: {}".format(Utils.GREEN + title))
                        print(Utils.YELLOW + "[v]" +
                            Utils.WHITE + "Url: {}".format(Utils.GREEN + url))
                        print(Utils.YELLOW +
                            "[v]" + Utils.WHITE + "Image-Url: {}".format(Utils.GREEN + image))
                        print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "MD5-url: {}\n".format(Utils.BLUE + md5url))
                    f.write("Title: {}\r\n".format(title))
                    f.write("Url: {}\r\n".format(url))
                    f.write("Image-Url: {}\r\n".format(image))
                    f.write("MD5-Url: {}\r\n\n".format(md5url))

                    f2.write("<h4>({})Title: {}</h4>".format(Engine.count,title))
                    f2.write("<p>Url: {}</p>".format("<a href ='" + url + "' target = 'blank'>" + url + "</a>"))
                    f2.write("<p>Image-Url: {}</p>".format("<a href ='" + image + "' target = 'blank'>" + image + "</a>"))
                    f2.write("<p>MD5-Url: <a>{}</a></p>".format(md5url))
                    i = i+1
                    Engine.count = Engine.count + 1
            report = report.replace("_image.txt",".txt")

        elif name == "notevil":
            f = open(report, "a")
            f.write(name + " onion-links\r\n\n")
            i = 0
            list1 = parser.find_all("div", class_="row")
            for link in list1:
                title = link.find_all("a")[2].text.replace(
                    "  ", "").replace("\n", "")
                url = link.find_all("a")[2]["href"]
                description = link.find("span").text.replace("\n", "")
                md5url = hashlib.md5(url.encode('utf-8')).hexdigest()
                if out == 1:
                    print(Utils.GREEN + "[+]" +
                        Utils.WHITE + "Title: {}".format(Utils.GREEN + title))
                    print(Utils.YELLOW + "[v]" +
                        Utils.WHITE + "Url: {}".format(Utils.GREEN + url))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "Description: {}".format(Utils.GREEN + description))
                    print(Utils.YELLOW + "[v]" + Utils.WHITE +
                        "MD5-url: {}\n".format(Utils.BLUE + md5url))
                f.write("Title: {}\r\n".format(title))
                f.write("Url: {}\r\n".format(url))
                f.write("Description: {}\r\n".format(description))
                f.write("MD5-Url: {}\r\n\n".format(md5url))

                f2.write("<h4>({})Title: {}</h4>".format(Engine.count,title))
                f2.write("<p>Url: {}</p>".format("<a href ='" + url + "' target = 'blank'>" + url + "</a>"))
                f2.write("<p>Description: {}</p>".format(description))
                f2.write("<p>MD5-Url: <a>{}</a></p>".format(md5url))
                Engine.count = Engine.count + 1
                i = i+1
        f.write("Total Onion {} Site Found: {}\r\n".format(name, str(i)))
        f.close()
        print(Utils.BLUE + "[I]" + Utils.WHITE + "Total {} Onion Site Found: {}".format(
            Utils.GREEN + name + Utils.WHITE, Utils.GREEN + str(i) + Utils.WHITE))

    @staticmethod
    def Torch(parameter, report, out,htmlReport):
        images = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                     "Do you want to search images?(1)Yes(2)No" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
        while images < 1 or images > 2:
            images = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                         "Do you want to search images?(1)Yes(2)No" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
        if images == 1:
            image_url = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/images?query={}".format(
                parameter)
        print(Utils.GREEN + "\n[+]" + Utils.WHITE +
              "Searching Torch Results for : {}\n".format(Utils.GREEN + parameter))
        url = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query={}&action=search".format(
            parameter)
        try:
            req = requests.get(url, proxies=Engine.proxy,
                               headers=Engine.headers)
            parser = soup(req.content, "html.parser")
            Engine.dataExtraction(parser, "Torch", report, out,htmlReport)
            if images == 1:
                try:
                    print(Utils.GREEN + "\n[+]" + Utils.WHITE +
                          "Searching Torch Images Results for : {}\n".format(Utils.GREEN + parameter))
                    req = requests.get(
                        image_url, proxies=Engine.proxy, headers=Engine.headers)
                    parser = soup(req.content, "html.parser")
                    Engine.dataExtraction(parser, "Torch-Images", report, out,htmlReport)
                except Exception as e:
                    pass
        except Exception as e:
            pass

    @staticmethod
    def Notevil(parameter, report, out,htmlReport):
        print(Utils.GREEN + "\n[+]" + Utils.WHITE +
              "Searching notevil Results for : {}\n".format(Utils.GREEN + parameter))
        url = "http://notevilmtxf25uw7tskqxj6njlpebyrmlrerfv5hc4tuq7c7hilbyiqd.onion/index.php?q={}".format(
            parameter)
        try:
            req = requests.get(url, proxies=Engine.proxy,
                               headers=Engine.headers)
            parser = soup(req.content, "html.parser")
            Engine.dataExtraction(parser, "notevil", report, out,htmlReport)
        except Exception as e:
            pass


    @staticmethod
    def Ahmia(parameter, report, out,htmlReport):
        print(Utils.GREEN + "\n[+]" + Utils.WHITE +
              "Input Parameter: {}".format(parameter))
        period = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                     "Insert a Period of time\n(1)Last-Day\t\t(2)Last-Week\n(3)Last-Month\t\t(4)All-Results" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
        while period < 1 or period > 4:
            period = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                         "Insert a Period of time\n(1)Last-Day\t\t(2)Last-Week\n(3)Last-Month\t\t(4)All-Results" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
        if period == 1:
            url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}&d=1".format(
                parameter)
            resc_url = "https://ahmia.fi/search/?q={}&d=1".format(parameter)
        elif period == 2:
            url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}&d=7".format(
                parameter)
            resc_url = "https://ahmia.fi/search/?q={}&d=7".format(parameter)
        elif period == 3:
            url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}&d=30".format(
                parameter)
            resc_url = "https://ahmia.fi/search/?q={}&d=30".format(parameter)
        elif period == 4:
            url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}&d=all".format(
                parameter)
            resc_url = "https://ahmia.fi/search/?q={}&d=all".format(parameter)
        print(Utils.GREEN + "\n[+]" + Utils.WHITE +
              "Searching Ahmia Results for : {}\n".format(Utils.GREEN + parameter))
        try:
            req = requests.get(url, proxies=Engine.proxy,
                               headers=Engine.headers)
            parser = soup(req.content, "html.parser")
            Engine.dataExtraction(parser, "Ahmia", report, out,htmlReport)
        except Exception as e:
            try:
                print(resc_url)
                req = requests.get(
                    resc_url, proxies=Engine.proxy, headers=Engine.headers)
                parser = soup(req.content, "html.parser")
                Engine.dataExtraction(parser, "Ahmia", report, out,htmlReport)
            except Exception as e:
                pass

    @staticmethod
    def HelpMsg():
        print(Utils.RED + "____________________________________________________________________")
        print (Utils.RED + "|" + Utils.WHITE + " DB-A = Execute Local Database" + Utils.RED +"                                    |\n|" + Utils.WHITE + " DB-D = Deactivate Local Database" + Utils.RED + "                                 |\n|" + Utils.WHITE + " DB-S = Local Database Status" + Utils.RED + "                                     |\n|" + Utils.WHITE + " Darkus-Exit = Exit from the programm" + Utils.RED + "                             |\n|" + Utils.WHITE + "--Check = Check if the given url is included on Ahmia Blacklist" + Utils.RED + "   |")
        print(Utils.RED + "--------------------------------------------------------------------")
        Engine.Main("No-Res")

    @staticmethod
    def Requirements():
        Engine.Agreement()
        Utils.Clear_Screen()
        print(Utils.BLUE + "[I]" + Utils.WHITE +
              "Checking if Tor Service is active...")
        sleep(3)
        try:
            service = requests.get("http://localhost:9050")
            print(Utils.GREEN + "\n[+]" +
                  Utils.WHITE + "Tor Service is active restart")
            os.system("sudo service tor restart")
        except requests.ConnectionError:
            print(Utils.RED + "\n[!]" + Utils.WHITE +
                  "Tor Service is not active. Activating Tor Service...\n")
            os.system("sudo service tor start")
            print(Utils.GREEN + "\n[+]" +
                  Utils.WHITE + "Tor Service activated\n")


    @staticmethod
    def Main(mode):
        if mode == "Res":
            print(Utils.BLUE + "[I]" + Utils.WHITE +
                "Checking internet connection...")
            sleep(3)
        ipUrl = "http://ip-api.com/json"
        try:
            ipReq = requests.get(ipUrl, proxies=Engine.proxy, timeout=15)
            if mode == "Res":
                Engine.Banner()
                reader = ipReq.text
                converted = json.loads(reader)
                ip = converted["query"]
                country = converted["country"]
                print(Utils.BLUE + "\n[I]" + Utils.WHITE +
                    "Your Tor-Proxy ip address: {}".format(Utils.GREEN + ip))
                print(Utils.BLUE + "\n[I]" + Utils.WHITE +
                    "Your are currently located in: {}".format(Utils.GREEN + country))
                print(Utils.BLUE + "\n[I]" + Utils.WHITE +
                    "Darkus-Exit for quitting the program")
            param = str(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                        "Insert a Parameter to search(Help For see all the options)" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
            while param == "":
                param = str(input(
                    Utils.GREEN + "\n[+]" + Utils.WHITE + "Insert a Parameter to search(Darkus-Exit for quitting the program)" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
            if param != "Darkus-Exit":
                if param == "Help" or param == "help":
                    Engine.HelpMsg()
                elif param == "DB-A":
                    os.system("sudo php -S 127.0.0.1:5600  >/dev/null 2>&1 &")
                    print(Utils.BLUE + "\n[I]" + Utils.WHITE + "Local Database started at http://127.0.0.1:5600")
                    Engine.Main("No-Res")
                elif param == "DB-D":
                    os.system("sudo killall php >/dev/null 2>&1 &")
                    print(Utils.BLUE + "\n[I]" + Utils.WHITE + "Local Database stopped")
                    Engine.Main("No-Res")
                elif param == "DB-S":
                    try:
                        service = requests.get("http://localhost:5600")
                        print(Utils.GREEN + "\n[+]" +
                            Utils.WHITE + "Local Database Active at http://127.0.0.1:5600 ")
                    except requests.ConnectionError:
                        print(Utils.RED + "\n[!]" + Utils.WHITE +
                            "Local Database is not not Active")
                    Engine.Main("No-Res")
                else:
                    if "--Check" in param:
                        url = param.replace("--Check","").replace(" ","")
                        if url ==  "" or ".onion" not in url:
                            print(Utils.BLUE + "[I]" + Utils.WHITE + "Please Insert a valid onion url before '--check'")
                        
                        else:
                            Engine.HashCheck(url)
                    else:
                        fold = "output/{}".format(param)
                        if os.path.exists(fold):
                            pass
                        else:
                            os.mkdir(fold)
                        report = "output/{}/{}.txt".format(param,param)
                        if os.path.exists(report):
                            os.remove(report)
                            if os.path.exists(report.replace(".txt","_image.txt")):
                                os.remove(report.replace(".txt","_image.txt"))
                        if os.path.exists("output/{}/{}.Dk".format(param,param)):
                            os.remove("output/{}/{}.Dk".format(param,param))
                            if os.path.exists(report.replace(".Dk","_image.Dk")):
                                os.remove(report.replace(".Dk","_image.Dk"))
                        if os.path.exists("output/{}/{}.html".format(param,param)):
                            os.remove("output/{}/{}.html".format(param,param))
                        htmlReport= Engine.HtmlReport(report,param)

                        out = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                                        "Do you want to print the output on Screen?(1)Yes(2)No" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
                        while out < 1 or out > 2:
                                out = int(input(Utils.GREEN + "\n[+]" + Utils.WHITE +
                                        "Do you want to print the output on Screen?(1)Yes(2)No" + Utils.RED + "\n\n[:DARKUS:]" + Utils.WHITE + "-->"))
                        Engine.Ahmia(param, report, out,htmlReport)
                        Engine.Torch(param, report, out,htmlReport)
                        Engine.Notevil(param, report, out,htmlReport)
                        f = open(report, "a")
                        f.write("Total Onion Site Found: {}\r\n\nReport created with Darkus:https://github.com/Lucksi/Darkus".format(str(Engine.count)))
                        f.close()
                        print(Utils.BLUE + "\n[I]" + Utils.WHITE + "Total Onion Site Found: {}".format(
                                Utils.GREEN + str(Engine.count) + Utils.WHITE))
                        report2 = report.replace(".txt","_image.txt")
                        print(Utils.BLUE + "\n[I]" + Utils.WHITE + "Html Report Created at: {} ".format(Utils.GREEN + htmlReport + Utils.WHITE))
                        f = open(htmlReport,"a")
                        f.write("</div>\n</body>\n</html>")
                        f.close()
                        Engine.encoding(report,"Web")
                        if os.path.isfile(report2):
                            Engine.encoding(report2,"Image")
                        Engine.count = 0
                    cont = input(Utils.WHITE + "\nPress enter to continue...")
                    Utils.Clear_Screen()
                    Engine.Main("Res")

            else:
                print(Utils.BLUE + "\n[I]" +
                    Utils.WHITE + "Stopping Tor Service...")
                os.system("sudo service tor stop")
                sleep(2)
                print(Utils.WHITE + "\nExit Thank you for having used Darkus...")
        except requests.ConnectionError as e:
            print(Utils.RED + "\n\n[!]" + Utils.WHITE +
                  "Cannot connect to Network,Check your internet connection" + str(e))


if __name__ == "__main__":
    try:
        Engine.Requirements()
        Engine.Main("Res")
    except KeyboardInterrupt:
        print(Utils.RED + "\n\n[!]" + Utils.WHITE +
              "You Have pressed CTRL C stopping Tor Services and Exit")
        os.system("sudo service tor stop")
