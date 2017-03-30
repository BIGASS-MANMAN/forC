#/bin/bash
TITLE=$1
NUMBER=$2
STUDENT=$3

if [ ! -d ../Student/$TITLE/$STUDENT ]
then
mkdir ../Student/$TITLE/$STUDENT
fi

unzip -o ../Student/$TITLE/$STUDENT.zip -d ../Student/$TITLE/$STUDENT/
cp ./Makefile ../Student/$TITLE/$STUDENT/
cd ../Student/$TITLE/$STUDENT

for ((i=1;i<$NUMBER+1;i++)); do
        if [ -f enc_$i.c ]
        then
        iconv -f cp949 -t utf-8 $i.c > enc_$i.c
        fi
done

make 2>&1|tee make.log
for ((i=1;i<$NUMBER+1;i++)); do
	if [ -f $i ]
	then
	./$i > $i.log
	fi
done
make clean

cd ../../../src
python normalization.py $TITLE $NUMBER $STUDENT
python Compare.py $TITLE $NUMBER $STUDENT
