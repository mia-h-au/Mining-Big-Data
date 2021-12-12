Exercise 4 (MapReduce) - Requirements

Part 1: Write a program that processes the FirstInputFile http://www.gutenberg.org/cache/epub/100/pg100.txt 
and the SecondInputFile http://www.gutenberg.org/files/3399/3399.txt. 
This program should count the number of words with a specific amount of letters in these files. 
For example, the number of words with 4 letters, 5 letters and so on. 
If one word is repeated 20 times in the text, count it individually 20 times.

Part 3: Write a second program that again processes the FirstInputFile http://www.gutenberg.org/cache/epub/100/pg100.txt 
and the SecondInputFile http://www.gutenberg.org/files/3399/3399.txt. 
However, in addition to counting the number of words with a specific amount of letters, if one word is repeated several times, count it only once. 
So, your output should be the frequency of words with same length, but count a repeated word only once. 


INSTRUCTIONS TO RUN THE CODE

Part 1
-Set a project in Eclipse and add the WordCount.java(renamed from WordCount12.java) in the project according to instructions in Stanford document on http://snap.stanford.edu/class/cs246-2017/homeworks/hw0/tutorialv3.pdf 
-Adding 2 jar files: htrace-core4.4.0.1-incubating.jar from /usr/lib/hadoop-hdfs/lib and sl4j-log4j12.jar from /usr/lib/hadoop/lib
-Download the file http://www.gutenberg.org/cache/epub/100/pg100.txt and http://www.gutenberg.org/files/3399/3399.txt, paste them into folder cloudera/workspace/WordCount
-Right click the project and input “pg100.txt output1” in “run as- run configuration-arguments”
Run the project
-Check the output in cloudera/workspace/WordCount/output1
-Right click the project and input “3399.txt output1”  in “run as- run configuration-arguments”
-Check the output in cloudera/workspace/WordCount/output2


Part 3
-Set a project in Eclipse and add the WordCount.java(renamed from WordCount34.java) in the project according to instructions in Stanford document on http://snap.stanford.edu/class/cs246-2017/homeworks/hw0/tutorialv3.pdf 
-Adding 2 jar files: htrace-core4.4.0.1-incubating.jar from /usr/lib/hadoop-hdfs/lib and sl4j-log4j12.jar from /usr/lib/hadoop/lib
-Download the file http://www.gutenberg.org/cache/epub/100/pg100.txt and http://www.gutenberg.org/files/3399/3399.txt, paste them into folder cloudera/workspace/WordCount
-Right click the project and input “pg100.txt temp output1” in “run as- run configuration-arguments”
-Run the project
-Check the output in cloudera/workspace/WordCount/output1
-Right click the project and input “3399.txt temp output1”  in “run as- run configuration-arguments”
-Check the output in cloudera/workspace/WordCount/output2

