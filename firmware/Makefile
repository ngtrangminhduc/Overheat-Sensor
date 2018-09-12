#makefile
ghmain:	ghmain.o ghutils.o hshbme280.o
	gcc -g -o ghmain ghmain.o ghutils.o hshbme280.o -lwiringPi
ghmain.o:	ghmain.c ghutils.h
	gcc -g -c ghmain.c
ghutils.o:	ghutils.c ghutils.h hshbme280.h
	gcc -g -c ghutils.c
hshbme280.o:	hshbme280.c hshbme280.h
	gcc -g -c hshbme280.c
