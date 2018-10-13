import socket
import time
import threading
import markovify


class Bot:
    """
    Bot Instance
    """
    personas = []
    personasfiles = ["biglebowski", "spyguide", "dreampsychology", "freudOOP", "swfqw"]

    def __init__(self, host, port, nick, channel):
        self.host = host
        self.port = port
        self.nick = nick
        self.channel = channel
        self.s = socket.socket()

    def connect(self):
        """
        Handles the connection to IRC
        """
        try:
            print("Trying to establish connection\n")
            self.s.connect((self.host, self.port))
            time.sleep(3)
            print("Connected")
            self.s.send(("USER " + self.nick + " " + self.nick +
                         " " + self.nick + " :Just a bot\n").encode('utf-8'))
            self.s.send(("NICK " + self.nick + "\n").encode('utf-8'))
            self.s.send(("JOIN " + self.channel + "\n").encode('utf-8'))
            print("[+] Connected \n")

        except Exception as e:
            print(e)
            print('[-] Could not establish connection. Aborting! \n')

            exit(0)

    def privmsg(self, text):
        """
        Handles sending private messages on irc
        """
        try:
            self.s.send(("PRIVMSG " + str(self.channel) + " :" + str(text) + "\n").encode('utf-8'))
        except Exception as e:
            print(e)
            print("[---] Couldn't send message: \n")

    def fodder(self):
        """
        Handles feeding bot the markofivy model,
        or creates a new model if no previous found
        """
        try:
            model = open("model.json", "r")
            model_json = model.read()
            model.close()
            print("[+] Model found. Reading...")
        except IOError:
            print("[*] Couldn't load model file. Creating new model...")

            for element in self.personasfiles:
                try:
                    f = open("personas/" + element + ".txt")
                    text = f.read()
                    self.personas.append(markovify.Text(text))
                    f.close()
                except IOError:
                    print("[--] File not found " + element + "\n")

            model = open("model.json", "w")
            model_mark = markovify.combine(self.personas)
            model_json = model_mark.to_json()
            model.write(model_json)
            model.close()
            print("[*] Created new model. Proceeding")

        self.model_combo = markovify.Text.from_json(model_json)

    def talkytalk(self):
        """
        Generates sentence from markovify model
        """
        try:
            self.privmsg(" ".join(
                self.model_combo.make_short_sentence(
                    110, max_overlap_total=4,
                    max_overlap_ratio=0.5, tries=20).split("- ")))
        except:
            self.privmsg("[!] Cannot compute new sentence [!]")

    def maintain(self):
        """
        Main bot loop for handling commands
        """
        with open("irclog.txt", "a") as log:

            while True:
                text = self.s.recv(2040).decode('utf-8')
                print(text)
                log.write(text)

                if "PING" in text:
                    self.s.send(("PONG " + str(text.split()[-1]) + "\r\n").encode('utf-8'))
                    print("PONG " + str(text.split()[-1]) + "\r\n")
                elif "!botout" in text:
                    self.privmsg("Goodbye y'all")
                    self.s.close()
                    log.close()
                    exit(0)
                elif "!hi" in text:
                    self.privmsg("Hello there " + text[1:text.find("!")] + "!")
                elif "!bot" in text:
                    self.talkytalk()


if __name__ == "__main__":

    try:
        a = Bot("irc.freenode.org", 6667, "FreudBot", "#tk")
        a.fodder()
        a.connect()
        time.sleep(2)
        t = threading.Thread(target=a.maintain)
        t.start()

    except KeyboardInterrupt:
        t.stop()
        exit(0)
