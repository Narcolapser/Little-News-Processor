commit:
#	make clean
	git add *
	git commit

clean:
	rm *~ 
	rm */*~ 
	rm *.pyc
	rm */*.pyc
	rm *.pdf
	rm *.txt
	rm *.html
