CC= gcc
RM= rm -vf
CFLAGS= -Wall -g
CPPFLAGS= -I.
SRCFILES= $(wildcard *.c)
OBJFILES= $(patsubst %.c, %.o, $(SRCFILES))
PROGFILES= $(patsubst %.c, %, $(SRCFILES))

.PHONY: all clean

all: $(PROGFILES)
clean:
	$(RM) $(OBJFILES) $(PROGFILES) *~ 
