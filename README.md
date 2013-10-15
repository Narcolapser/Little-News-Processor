Little-News-Processor
=====================

Little News Processor (LNP) is a system for reformatting multiple difference news feeds into a single format for outputting into various locations. This idea was concieved by a desire for peices of news that are pertinent to me being automatically desposited on my kindle every morning. 

Why not use an existing solution?

I looked into existing open source solutions avaliable. They all dealt with gathering in rss feeds of some nature or another and presenting them to you in a form for you to read or sync to a device (maybe). But the problem is that this is far to unflexible of a news source for me. Some of my news doesn't come in the form of rss feeds. A lot of the news I want is actually personal information. So I need to make my own solution that handles many more input options and can also tend to many output options.

The different sources is one thing, but the other real major break in mentallity of LNP in contast to most other news programs is that LNP processess data. It can just simply pull down the rss feeds and out put them if you want, OR you could have it process the information. For example. You wanted to monitor the trend of the word "Cloud" in a 10-50 gaming news feeds. you could read them yourself and get a biased opinion on how much people are talking about it, or you could have LNP parse all of the posts and find the objective number of times that "cloud" appears in the weblogs.

So different kind of sources. What kind of sources are you thinking?
	RSS (your normal news feeds)
	HTML (read from sites that don't support news feeds natively, like bank account information, weather, etc)
	CSV/XSLX (Data, gonna come back to what I mean)
	SQL (Data!)
	TXT/XML (Data?)

What else can you do with processing?
So, The bible is huge. I want to set up a reading schedule for myself and have the passages I want pulled from a SQL database and put into the out put of my personal news feed. This means that there is a static body of information that is picked through on a schedule rather than just all dumped in at once. This is true for txt and csv as well. You can have it give you parts of an input at a time based off of how the plug in is programmed.

What's more, say I keep close tabs on my bank acounts. Every day I log in and check the transactions, download the csv, add it to my spread sheet and plug in transaction purposes and types etc. LNP will read in that spread sheet and make informatics. say like a pie chart of how much I have spent this month and how much of my income I have left. Or a table of my expendatures and how they have varied from last month.

This sounds complex. How are you going to pull it off?
Three APIs. Yea. Three. This is why. LNP exists to provide the inter-API communication and act as the frame work for the 3 to communicate, but LNP itself has absolutely no knowledge of what's beyond the input or the out put, and it does not know any of the data it feeds into the processing or out of it. It only knows a universal description language (XML) that will be used to wrap the information and unify it. This allows input, output, and processing pluggins to be written easily as they only have to care about getting data down and shaping it, taking shaped and processed data and formatting it, or taking data and making information. 

The input API is very straight forward. You write a python script which has one required function "fetch" this function has 1 argument. That argument may be a tuple, but LNP cares not, however LNP will send one and only one and always one argument. LNP expects in return a data set, whose format will be described in the XML description file.

The output API is very similar a very straight forward API. With this there are two arguments sent to the "put" function. This is because I assume you are going to want the data to out put and the location to put it. So if you write a PDF or out put to WordPress, you gotta the information in those two arguements.

The processing API is again, very simple. Here, 1 input, 1 output, function named "consume" to avoid naming conflicts with the "process" library. 

With the input API one might take the location of an RSS feed as the argument, the plugin would then fetch the information from the feed and return it. perhaps if you had a tuple it would take the location and a date so that you could prevent downloading the entire feed repeatebly.

The output API might take a set of text, and a couple of images and arange them and out put a pdf that is automatically pushed to my kindle. so in the morning when I wake, there's my personal news pdf ready and waiting.

The processing API is meant to simplify both the in and output a little by taking some stress from them. for example the input api might give me all my account information, and the out put api will do a great job and writting to a pdf. But it doesn't make sense for the "bank account" pluggin to make pie charts. nor does it make sense for the "pdf writter" pluggin to. so the processing api exists simply to fill the gaps and keep the programming modular as possible. 
