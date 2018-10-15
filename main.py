from bot_class import Bot
import time
import threading
import optparse


if __name__ == "__main__":

    PARSER = optparse.OptionParser(" usage %prog -a <irc_address> -p <irc_port> -c <irc_channel> -n <bot_nickname> ")

    PARSER.add_option('-a',
                      dest='irc_address',
                      type='string',
                      default="irc.freenode.org",
                      help="Specify irc address")
    PARSER.add_option('-p',
                      dest='irc_port',
                      type='int',
                      default=6667,
                      help="Specify irc port")
    PARSER.add_option('-c',
                      dest='irc_channel',
                      type='string',
                      default="#tk",
                      help="Specify irc channel")
    PARSER.add_option('-n',
                      dest='bot_nickname',
                      type='string',
                      default="JustABotBotBot",
                      help="Specify bot nickname")

    (OPTIONS, ARGS) = PARSER.parse_args()
    IRC_ADDRESS = OPTIONS.irc_address
    IRC_PORT = OPTIONS.irc_port
    IRC_CHANNEL = OPTIONS.irc_channel
    BOT_NICKNAME = OPTIONS.bot_nickname

    try:
        a = Bot(IRC_ADDRESS, IRC_PORT, IRC_CHANNEL, BOT_NICKNAME)
        time.sleep(2)
        t = threading.Thread(target=a.maintain)
        t.start()

    except KeyboardInterrupt:
        t.stop()
        exit(0)
