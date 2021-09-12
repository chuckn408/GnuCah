#!/bin/sh

echo "Welcome to GNU+Cards!";
echo "---------------------";

bcmax=$(sed -n '$=' ../Main/bc);
wcmax=$(sed -n '$=' ../Main/wc);
Y=$bcmax; #AmtBlkCrds

RANDOM=$$
Ran=$((1 + $RANDOM % $Y)); #RanNumGen

Bout=$(sed $Ran'q;d' ../Main/bc) #prep'd for wc_count
wc_count=$(echo $Bout | tr ' ' '\n' | tr '.' '\n' | grep -c '____'); #Need wordcount later

##########output
sed $Ran'q;d' ../Main/bc;
i=1;
while [ $i -le $wc_count ]
do
	Y=$wcmax; #AmtWhtCrds
	sed $Ran'q;d' ../Main/wc;
	i=$((i+1))
	Ran=$((1 + $RANDOM % $Y)); #RanNumGen
done;

