# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import requests
import os
from bs4 import BeautifulSoup as soup
import json
from time import sleep
import base64


class Colors:
    YELLOW = "\033[0;93m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"


class Engine:
    proxy = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    headers = {
        "Useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    }
    count = 0

    @staticmethod
    def encoding(report):
        quest = int(input(Colors.BLUE + "\n[?]" + Colors.WHITE + "Do you want to encode the report(1)Yes(2)No?" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
        if quest == 1:
            EncodedFile = report.replace(".txt", ".Dk")
            f = open(report, "r+")
            reader = f.read()
            f.close()
            print(Colors.GREEN + "\n[+]" +
                      Colors.WHITE + "Encoding report...")
            sleep(3)
            encodingString = reader.encode("utf-8")
            Base64_Byte = base64.b64encode(encodingString)
            FinalString = Base64_Byte.decode("utf-8")
            f = open(EncodedFile, "w+", encoding="ascii")
            f.write(FinalString)
            f.close()
            print(Colors.YELLOW + "[v]" + Colors.WHITE +
                      "Report Encoded: {}".format(Colors.GREEN + EncodedFile.replace("output/","")))
            os.remove(report)
            print(Colors.GREEN + "\n[+]" + Colors.WHITE + "Report saved in: {}".format(
                Colors.GREEN + EncodedFile))
        else:
            print(Colors.GREEN + "\n[+]" + Colors.WHITE + "Report saved in: {}".format(
                Colors.GREEN + report))


    @staticmethod
    def Agreement():
        os.system("clear")
        print(Colors.BLUE + "[I]" + Colors.WHITE + "Checking Usage Agreement")
        sleep(3)
        if os.path.exists("Agreement.txt"):
            sleep(3)
            f = open("Agreement.txt", "r", newline=None)
            content = f.read()
            f.close()
            if content != "Agreement Accepted":
                sleep(4)
                os.system("clear")
                f = open("Banner/Banner.txt", "r", newline=None)
                for line in f:
                    sleep(0.3)
                    print(Colors.RED + line.replace("\n", ""))
                f.close()
                sleep(0.3)
                try:
                    choice = str(input(Colors.WHITE + "\nThis tool is intented only for research and educational purposes only. I do not assume any liability for the the bad usage of this tool\n\nPress" +
                                       Colors.GREEN + "(Y)" + Colors.WHITE + "To accept" + Colors.RED + "(N)" + Colors.WHITE + "To decline\n\n" + Colors.RED + "[:DARKUS:]" + Colors.WHITE + "-->"))
                    if choice == "Y" or choice == "y":
                        f = open("Agreement.txt", "w")
                        f.write("Agreement Accepted")
                        f.close()
                        os.system("clear")
                        print(Colors.YELLOW +
                              "[v]" + Colors.WHITE + "Agreement Accepted")
                        sleep(2)
                    elif choice == "N" or choice == "n":
                        print(
                            Colors.RED + "Agreement refused You cannot use this tool if you do not accept this condition...\nExit")
                        exit()
                    else:
                        Engine.Agreement()
                except ValueError:
                    Engine.Agreement()
                except KeyboardInterrupt:
                    print("\n")
                    exit()
            else:
                print(Colors.YELLOW + "\n[v]" +
                      Colors.WHITE + "Usage Agreement found")
                sleep(2)
        else:
            os.system("clear")
            f = open("Banner/Banner.txt", "r", newline=None)
            for line in f:
                sleep(0.3)
                print(Colors.RED + line.replace("\n", ""))
            f.close()
            sleep(0.3)
            try:
                choice = str(input(Colors.WHITE + "\nThis tool is intented only for research and educational purposes only. I do not assume any liability for the the bad usage of this tool\n\nPress" +
                                       Colors.GREEN + "(Y)" + Colors.WHITE + "To accept" + Colors.RED + "(N)" + Colors.WHITE + "To decline\n\n" + Colors.RED + "[:DARKUS:]" + Colors.WHITE + "-->"))
                if choice == "Y" or choice == "y":
                    f = open("Agreement.txt", "w")
                    f.write("Agreement Accepted")
                    f.close()
                    os.system("clear")
                    print(Colors.YELLOW + "[v]" +
                          Colors.WHITE + "Agreement Accepted")
                    sleep(2)
                elif choice == "N" or choice == "n":
                    print(
                        Colors.RED + "Agreement refused You cannot use this tool if you do not accept this condition...\nExit\n")
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
        os.system("clear")
        f = open("Banner/Banner.txt", "r", newline=None)
        for line in f:
            sleep(0.3)
            print(Colors.RED + line.replace("\n", ""))
        f.close()
        sleep(0.3)
        print(Colors.WHITE + "\nA Onion Websites Searcher\t  Coded by Lucksi")
        print(Colors.RED + "____________________________________________________")
        print(Colors.RED + "|" + Colors.WHITE + " Instagram:lucks_022" +
              Colors.RED + "                              |")
        print(Colors.RED + "|" + Colors.WHITE + " Email:lukege287@gmail.com" +
              Colors.RED + "                        |")
        print(Colors.RED + "|" + Colors.WHITE + " GitHub:Lucksi" +
              Colors.RED + "                                    |")
        print(Colors.RED + "|" + Colors.WHITE + " Twitter:@Lucksi_22" +
              Colors.RED + "                               |")
        print(Colors.RED + "|" + Colors.WHITE +
              " Linkedin:https://www.linkedin.com/in/lucksi" + Colors.RED + "      |")
        print(Colors.RED + "----------------------------------------------------")

    @staticmethod
    def dataExtraction(parser, name, report):
        if name == "Ahmia":
            f = open(report, "a")
            f.write(name + "\tonion-links\r\n")
            i = 0
            list1 = parser.find_all("li", class_="result")
            for link in list1:
                title = link.find("h4").text.replace(" ", "").replace("\n", "")
                url = "http://" + \
                    link.find("cite").text.replace("\n", "").replace(" ", "")
                description = link.find("p").text.replace("\n", "")
                timestamp = link.find("span", class_="lastSeen")[
                    "data-timestamp"].replace("\n", "").replace(" ", "")
                print(Colors.GREEN + "[+]" +
                      Colors.WHITE + "Title: {}".format(Colors.GREEN + title))
                print(Colors.YELLOW + "[v]" +
                      Colors.WHITE + "Url: {}".format(Colors.GREEN + url))
                print(Colors.YELLOW + "[v]" + Colors.WHITE +
                      "Description: {}".format(Colors.GREEN + description))
                print(Colors.YELLOW + "[v]" + Colors.WHITE +
                      "Timestamp: {}\n".format(timestamp))
                f.write("Title: {}\r\n".format(title))
                f.write("Url: {}\r\n".format(url))
                f.write("Description: {}\r\n".format(description))
                f.write("Timestamp: {}\r\n\n".format(timestamp))
                Engine.count = Engine.count + 1
                i = i + 1
        elif name == "Torch":
            f = open(report, "a")
            f.write(name + "\tonion-links\r\n")
            i = 0
            list1 = parser.find_all("div", class_="result mb-3")
            for link in list1:
                title = link.find("h5").text.replace(
                    "  ", "").replace("\n", "")
                url = link.find("a")["href"]
                description = link.find("p").text.replace("\n", "")
                print(Colors.GREEN + "[+]" +
                      Colors.WHITE + "Title: {}".format(Colors.GREEN + title))
                print(Colors.YELLOW + "[v]" +
                      Colors.WHITE + "Url: {}".format(Colors.GREEN + url))
                print(Colors.YELLOW + "[v]" + Colors.WHITE +
                      "Description: {}\n".format(Colors.GREEN + description))
                f.write("Title: {}\r\n".format(title))
                f.write("Url: {}\r\n".format(url))
                f.write("Description: {}\r\n".format(description))
                Engine.count = Engine.count + 1
                i = i+1
    
        elif name == "Torch-Images":
            f = open(report, "a")
            f.write(name + "\tonion-links\r\n")
            i = 0
            list1 = parser.find_all("div", class_="imagehold")
            for link in list1:
                link2 = link.find_all("a")
                for link3 in link2:
                    title = link3.find("img")["alt"].replace(
                        "  ", "").replace("\n", "")
                    url = link3["href"]
                    image = link3.find("img")["src"]
                    print(Colors.GREEN +
                          "[+]" + Colors.WHITE + "Title: {}".format(Colors.GREEN + title))
                    print(Colors.YELLOW + "[v]" +
                          Colors.WHITE + "Url: {}".format(Colors.GREEN + url))
                    print(Colors.YELLOW +
                          "[v]" + Colors.WHITE + "Image-Url: {}\n".format(Colors.GREEN + image))
                    f.write("Title: {}\r\n".format(title))
                    f.write("Url: {}\r\n".format(url))
                    f.write("Image-Url: {}\r\n\n".format(image))
                    i = i+1
                    Engine.count = Engine.count + 1
        f.write("Total Onion {} Site Found: {}\r\n".format(name, str(i)))
        f.close()
        print(Colors.BLUE + "[I]" + Colors.WHITE + "Total {} Onion Site Found: {}".format(
            Colors.GREEN + name + Colors.WHITE, Colors.GREEN + str(i) + Colors.WHITE))

    @staticmethod
    def Torch(parameter, report):
        images = int(input(Colors.GREEN + "\n[+]" + Colors.WHITE +
                     "Do you want to search images?(1)Yes(2)No" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
        while images < 1 or images > 2:
            images = int(input(Colors.GREEN + "\n[+]" + Colors.WHITE +
                         "Do you want to search images?(1)Yes(2)No" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
        if images == 1:
            image_url = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/images?query={}".format(
                parameter)
        print(Colors.GREEN + "\n[+]" + Colors.WHITE +
              "Searching Torch Results for : {}\n".format(Colors.GREEN + parameter))
        url = "http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query={}&action=search".format(
            parameter)
        try:
            req = requests.get(url, proxies=Engine.proxy,
                               headers=Engine.headers)
            parser = soup(req.content, "html.parser")
            Engine.dataExtraction(parser, "Torch", report)
            if images == 1:
                try:
                    print(Colors.GREEN + "\n[+]" + Colors.WHITE +
                          "Searching Torch Images Results for : {}\n".format(Colors.GREEN + parameter))
                    req = requests.get(
                        image_url, proxies=Engine.proxy, headers=Engine.headers)
                    parser = soup(req.content, "html.parser")
                    Engine.dataExtraction(parser, "Torch-Images", report)
                except Exception as e:
                    pass
        except Exception as e:
            pass

    @staticmethod
    def Ahmia(parameter, report):
        print(Colors.GREEN + "\n[+]" + Colors.WHITE +
              "Input Parameter: {}".format(parameter))
        period = int(input(Colors.GREEN + "\n[+]" + Colors.WHITE +
                     "Insert a Period of time\n(1)Last-Day\t\t(2)Last-Week\n(3)Last-Month\t\t(4)All-Results" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
        while period < 1 or period > 4:
            period = int(input(Colors.GREEN + "\n[+]" + Colors.WHITE +
                         "Insert a Period of time\n(1)Last-Day\t\t(2)Last-Week\n(3)Last-Month\t\t(4)All-Results" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
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
        print(Colors.GREEN + "\n[+]" + Colors.WHITE +
              "Searching Ahmia Results for : {}\n".format(Colors.GREEN + parameter))
        try:
            req = requests.get(url, proxies=Engine.proxy,
                               headers=Engine.headers)
            parser = soup(req.content, "html.parser")
            Engine.dataExtraction(parser, "Ahmia", report)
        except Exception as e:
            try:
                print(resc_url)
                req = requests.get(
                    resc_url, proxies=Engine.proxy, headers=Engine.headers)
                parser = soup(req.content, "html.parser")
                Engine.dataExtraction(parser, "Ahmia", report)
            except Exception as e:
                pass

    @staticmethod
    def Main():
        Engine.Agreement()
        os.system("clear")
        print(Colors.BLUE + "[I]" + Colors.WHITE +
              "Checking if Tor Service is active...")
        sleep(3)
        try:
            service = requests.get("http://localhost:9050")
            print(Colors.GREEN + "\n[+]" +
                  Colors.WHITE + "Tor Service is active")
        except requests.ConnectionError:
            print(Colors.RED + "\n[!]" + Colors.WHITE +
                  "Tor Service is not active. Activating Tor Service...")
            os.system("sudo service tor start")
            print(Colors.GREEN + "\n[+]" +
                  Colors.WHITE + "Tor Service activated")
        print(Colors.BLUE + "\n[I]" + Colors.WHITE +
              "Checking internet connection...")
        sleep(3)
        ipUrl = "http://ip-api.com/json"
        try:
            ipReq = requests.get(ipUrl, proxies=Engine.proxy, timeout=15)
            Engine.Banner()
            reader = ipReq.text
            converted = json.loads(reader)
            ip = converted["query"]
            country = converted["country"]
            print(Colors.BLUE + "\n[I]" + Colors.WHITE +
                  "Your Tor-Proxy ip address: {}".format(Colors.GREEN + ip))
            print(Colors.BLUE + "\n[I]" + Colors.WHITE +
                  "Your are currently located in: {}".format(Colors.GREEN + country))
            param = str(input(Colors.GREEN + "\n[+]" + Colors.WHITE +
                        "Insert a Parameter to search" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
            while param == "":
                param = str(input(
                    Colors.GREEN + "\n[+]" + Colors.WHITE + "Insert a Parameter to search" + Colors.RED + "\n\n[:DARKUS:]" + Colors.WHITE + "-->"))
            report = "output/{}.txt".format(param)
            if os.path.exists(report):
                os.remove(report)
            if os.path.exists("output/{}.Dk".format(param)):
                os.remove("output/{}.Dk".format(param))
            Engine.Ahmia(param, report)
            Engine.Torch(param, report)
            f = open(report, "a")
            f.write("Total Onion Site Found: {}\r\n\nReport created with Darkus:https://github.com/Lucksi/Darkus".format(str(Engine.count)))
            f.close()
            print(Colors.BLUE + "\n[I]" + Colors.WHITE + "Total Onion Site Found: {}".format(
                Colors.GREEN + str(Engine.count) + Colors.WHITE))
            Engine.encoding(report)
            print(Colors.BLUE + "\n[I]" +
                  Colors.WHITE + "Stopping Tor Service...")
            os.system("sudo service tor stop")
            sleep(2)
            print(Colors.WHITE + "\nExit Thank you for having used Darkus...")
        except requests.ConnectionError:
            print(Colors.RED + "\n\n[!]" + Colors.WHITE +
                  "Cannot connect to Network,Check your internet connection")


if __name__ == "__main__":
    try:
        Engine.Main()
    except KeyboardInterrupt:
        print(Colors.RED + "\n\n[!]" + Colors.WHITE +
              "You Have pressed CTRL C stopping Tor Services and Exit")
        os.system("sudo service tor stop")
