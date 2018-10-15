# Simple IRC bot

# Installing 
` git clone https://github.com/michalsimbiga/IrcBot`

# Usage
` python main.py -a <irc_address> -p <irc_port> -c <irc_channel> -n <bot_nickname>`
- -a switch : takes in irc_address
- -p switch : takes in irc_port
- -c switch : takes in irc_channel
- -n switch : takes in bot_nickname

By default, bot connects to irc.freenode.org on port 6667
The default channel is #tk, and bot nickname JustABotBotBot 

## Features:
### Connection
 - Works on sockets to connect our bot to host:port #channel instances.
 - Maintains itself by answering Ping-Pong queries
### Sentence generator
 - Utilizes markovify package to create markov-chains from given persona files
 - Creates json model of those chains and stores it locally for future reuse
### Wiki lookup
 - Uses wiki api to answer queries
 
# Commands
* !hi 
 - Returns back a greeting with the username

* !bot
 - Generates a random sentence from our markov-chain model

* !wiki <search_term>
 - Wiki lookup for <search_term>, returns Search Term, Description and Link to Wiki

* !botout
 - Say's goodbye and exits the channel
 
# TODO:
 - google lookup
 - karma system for users
 
