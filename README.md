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
xIn : a script designed to fetch data from an outside source. Given no arguments.
xProc : a script designed to process internal data. Give the data as only argument.
xOut : a script designed to take data and put it some where external. Given data and location as arguments.
xNetwork : a script that describes an arrangement of the scripts above. 
In these cases replace "x" with the desired name.

Road map:
Version 0.1:
	Read in bible verses
	read in news from toolong-didntread.com.

Version 0.2:
	process both bible and tldr-n inputs
	output to txt

Version 0.3:
	fetch and consume weather forcasts.
	output to pdf

Version 0.4:
	fetch and consume personal finance information.
	add chart processor
	
Version 0.5:
	add gs.stat counter as an input.
	add image support, use /r/Blackandwhiteporn for source material.
	improve HTML out (and as a result improve pdf out)

Version 0.6:
	Begin simple GUI

Version 0.7:
	Add personal support data processing and display.
	  process petra statements and such.
	Add rss feeds.

Version 0.8:
	Improve gui presentation
	add edditor for pluggins into the program.

Version 0.9:
	Bug hunt. Get this thing Robost for the dot O release.

Version 1:
	Party.
