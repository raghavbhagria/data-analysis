# &emsp;<b><U>FINAL DATA ANALYSIS REPORT</U>
# &emsp;&emsp;&emsp;&emsp;&emsp;<U> <b>GROUP 46</U>

## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<B>INTRODUCTION
### Our group decided to analyze the data for airplane crashes over a span of 5 years from **2004-2009**. Upon exploring the dataset a series of questions popped up in our minds.Since air travel was gaining popularity over that period of time each one of us had a series of question with different approaches we did the following data analysis.<br><br>
## &emsp;&emsp;&emsp;&emsp;<B>EXPLORATORY DATA ANALYSIS

## <B>QUESTIONS ANSWERED DURING ANALYSIS<br><br>
## <u>Sumer Mann</u><br>
### I am interested in knowing the trends in air plane crashes and trying to find ways to ensure more safety and better air-travel expirence. In addition to this, I am also concerned how many lives were lost and how many survived these crashes? Secondly, the trends of plane crashes will let me analyze on what route did most crashes happened and what airline was responsible for the crashes.<br>
### There are some visualizations that I think would be helpful to understand my analysis. First of all I made a joint plot of <u>Fatalities during crash</u> and <u>People aboard durng crash</u>. 
![](/Users/sumermann/Desktop/301/project-group46/images/images_for_final_report-sumer/jointplot.png)
### This plot shows a diagnal straight line. The data points falling in this reigon are the ones where people aboard is equal to fatalities. This is not a positive obversation and tells us that the air travel system and technology was not perfect at that time.<br>
### Secondly, I made a small dataframe out of the dataset which includes <u>Airline</u> and <u>Fatalities during plane crash of that airline operator</u>. 
![](/Users/sumermann/Desktop/301/project-group46/images/images_for_final_report-sumer/visual.png)
### This is just a small segment but it clearly shows that the West Caribbean Airways is the operator with the largest toll number of <b>8160</b>. This number is humongous. This company started in December 1998 and the operations ceased in September 2005 due to serious financial and procedural problems.<br>
### For a more enhanced and deep understanding for my research question, I am adding a snapshot of my tableau. 
![](/Users/sumermann/Desktop/301/project-group46/images/images_for_final_report-sumer/Dashboard-photo.png)
### I am also adding a link to my python notebook where I did a detailed analysis and research.
[complete analysis](/Users/sumermann/Desktop/301/project-group46/notebooks/analysis1.ipynb)<br>
### Some Insights that I was able to find out during this research was how data for aboard and fatalities went in hand-to-hand throughout the dataset with some outliers from the trend. Trimming down the dataset proved to be a good step as it helped me understand and focus me analyze on my reaearch analysis. Death of a single person is not acceptable.There can always be improvement is the avaition sector so that minimum lives are lost and the air transport can be made more safer in future times. I can say that lives lost cannot be brought back but as the technology is advancing day-by-day, air travel can be definitely made more safer in coming years.<br><br>
## <u>Raghav Bhagria</u><br>
I approached the data set in a way to answer the my reasearch questions which were:
1. What was it when a plane crashed and maximum people were on aboard?
1. Is there a great trend in number of survivor and fatalities?
1. highest number of crashes by operator and Type of aircrafts?
1. what type crashed the most?


To answer these question I did my exploratory data analysis under which I plotted the following the two graphs : 

![](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/images/Final%20report%20images%20Raghav/Screen%20Shot%202022-12-03%20at%2012.37.54%20PM.png)

from the first hist plot I was able  to find out that the model that crashed the most was which was Cesna 208B Grand Caravan with the number of crashes being over 8 times in a span of 5 years.(answer to qusetion 4)</br>
![](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/images/Final%20report%20images%20Raghav/Screen%20Shot%202022-12-03%20at%2012.38.12%20PM.png)
</br>
The scatter plot makes it very clear that in most of these incidents (except a few) all the people that were on board died. I came to this conclusion by looking at the straight diagonal line plotted on the graph.(answer to question 2) </br>

My complete data analysis file is here linked below:
![independent notebook](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/notebooks/analysis2.ipynb)
![group analysis](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/notebooks/group_analysis.ipynb)

this has all these visualizations:

![](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/images/Final%20report%20images%20Raghav/Screen%20Shot%202022-12-03%20at%2012.38.40%20PM.png)
this scatter plot shows that maximum people aboard a plane that crashed was in year 2005.(answer to question 1)</br>

![](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/images/Final%20report%20images%20Raghav/Screen%20Shot%202022-12-03%20at%2012.38.51%20PM.png)


this bar plot shows maximum Fatilities were incurred to air france over these 5 years.(answer to question 3)

![](https://github.com/ubco-W2022T1-cosc301/project-group46/blob/main/images/Final%20report%20images%20Raghav/Screen%20Shot%202022-12-03%20at%2012.39.01%20PM.png)

this bar plot states the airplane type that crashed and caused the maximum fatalities which from 2004-2009 was : Airbus-A320-233(answer to question 3)

## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<B>CONCLUSION

Through this project we got to learn a lot about how data analysis is actually done and with how we can experimentally derive results to our questions through data analysis. This particular dataset was collected from kaggle and we had to put in a lot of hardwork in cleaning it up and then going ahead using python,pandas,Seaborn and markdown to complete our data analysis. Overall we were able to find all the answers to our research questions and this project was a huge learning for us on how data analysis is done. 
