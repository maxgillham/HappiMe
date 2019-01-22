# HappiMe  

Check it out on [Devpost](https://devpost.com/software/happime).  


## Inspiration
In 2018 there are apps to track almost everything. You can track your financial well being, food consumption or even how well you sleep. 

Mental health is a prominent topic in today's world that is constantly in the public eye. We were surprised to realise that there are no good solutions to track your mental health. Our team decided to create an app that required a small amount of user interaction (<10 seconds) that could be used to monitor an individuals mental health and reach out to their support network when they may be at risk. 
 
## What it does
HappiMe is a mental health tracking app. Our app gives users a push notification at a random time every day and asks them a simple question, "how are you feeling right now"?. Users can choose 1 of 5 preset answers. This data is captured along with their current location and the time. 

## How we built it 
The mobile application is built in React Native and connects to a python Flask server to apply our machine learning model and store important information about the users well being.  The machine learning model used to determine unusual behaviour is a density based clustering algorithm fit over historical data.

## Challenges we ran into 
We ran into issues with idea generation and using python with stdlib. It took hours to finally settle on HappiMe and we cycled through more ideas than we can count. We also ran into issues using stdlib with python but were able to work around this by directly sending our request to their messagebird API using the python requests library. 

Additionally, we wanted to show how machine learning can be leveraged if this data was aggregated. However, since we just built this app this weekend, getting historical user data to train our ML models was not very feasible.  So to really show the power of this app, we had to generate this data by designing a series of Markov decision processes and probability distributions to model how this data could appear if a user logs for 100 days.

## Accomplishments that we're proud of 
Our application can effectively detect abnormal behaviour for any given user.  If a user responds to their daily push notification indicating they are very sad, at a time and place they are historically happy or content, an option to have the app send a text to a close friend appears.  We also were able to implement means of data visualisation that the user can view and clearly see locations and times that often have a negative impact on their mental health.

## What we learned 
This weekend we learned a lot about API development, React, and machine learning. Our team member that developed the API had never done any of this type of work before so it was a brand new experience. We had never used React native before this weekend and our prior machine learning knowledge was limited. This project allowed us to use these new tools in a very engaging fashion!

## What's next for HappiMe 
The next steps for HappiMe centres around integrating new data sources and creating a therapist portal. 
HappiMe could be connected to other tracking apps (Fitbit, myFitnessPal) to capture additional data. This data would include consumption, physical activity and hours slept. Additionaly weather API's could be leveraged to include the weather at the time of notification. This data would be used to create a more robust model that could detect anomalies and more accurately describe why a person may be feeling a certain way. 
With the additional information we could provide our users with context as to why they may be feeling a certain way. This context could help to re-enforce good habits and point out why a person may be feeling poorly. 
A therapist portal would enable our app to be used as a tool to monitor the mental health remotely and help provide therapists with more information than they may usually have. 
