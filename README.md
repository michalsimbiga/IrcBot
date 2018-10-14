# Simple IRC bot

## Features:

 - Works on sockets to connect our bot to host:port #channel instances.
 - Maintains itself by answering Ping-Pong queries
 - Utilizes markovify package to create markov-chains from given persona files
 - Creates json model of those chains and stores it locally for future reuse
 - Generates a random sentence each time we call "!bot" command
 
# TODO:
 - command line switches for host, port, channel, nick
 - wikipedia lookup
 - google first 3 lookup
 - karma system for users
 
