commit:
#	make clean
	git add *
	git commit

clean:
	rm *~ 
	rm */*~ 
	rm *.pyc
	rm */*.pyc
