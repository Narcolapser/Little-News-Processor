Little-News-Processor
=====================

Little News Processor (LNP) is a system for reformatting multiple difference news feeds into a single format for outputting into various locations. In it's function, it bears a closer resemblance to a web scrapper than a feed reader.

	LNP is designed with 3 conceptual areas. Inputs, Processors, and Outputs. an Input *requires* no arguments and has a "fetch" method in it's script file. The idea is that it's focus is on getting data into the system. As much data as it can formated as python objects easy to work with. Processors have a "consume" method that does work on information you pass to it from another Processor or an input. And an Output has no return but rather pushes information outside, to a txt file, pdf, web, kindle, etc. The only thing that keeps these seperate is psychological. Any one of them could do any of these tasks, but by giving them the title of input, processor, or output, people intuatively understand the purpose of the module. 
	
	Imagine you wanted to keep track of your finances closely. You wanted a daily update on your cash flow with charts and predictions and statistics. That would be easy with LNP. Take an input that pulls information from your bank. Take an input that pulls information from any other financial records you may have (I keep a google doc with all my reciepts for example). Plug those into a processors that create charts, graphs, and statistics. Then you can have an entire report sent to your tablet and a summary report sent to your phone through two different outputs. Or the same output that has been fed different data. 
	
	LNP is still very much so in alpha. There is currently not even a GUI, so it is inaccessible to non-programmers. But as the project develops I hope to see a community who greates pluggins for it to help data flow from the internet to their mind.
