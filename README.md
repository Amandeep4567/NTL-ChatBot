# NTL-ChatBot


<b>Problem Statement</b>

If a person who is not a part of the NTL wants to know what NTL actually is and how it works, he/she might definitely search “Next tech lab SRM AP” in google then some webpage of SRM will be loaded, and we are just a part of it then which defines us that we are different from the other labs.
So the point is to create our own website
 But people have so many questions regarding how to join NTL, What are the prerequisites for joining NTL, and so on. Instead of answering them manually, We’ve come up with an idea

<b>Our Solution</b?

Our plan is to build a chatbot for our website which actually answers the queries of anyone not only queries but also guides them in joining the NTL
It also informs them about the hackathons we’ve participated in and also won
To bring the interest among them that NTL is not like the other clubs

<b>Project Utilisation</b>

1. Integrating the Chatbot  with The NTL website so that it will solve everyone's queries
2. We can also integrate that module into the discord, so it would be easy for any freshmen to get their doubts cleared
3. In the future, we can integrate it with any application of NTL

<b>Project Implementation:</b>

The chatbot takes questions from the user as its input and then presents the answer as its output. There are 2 categories of questions that the chatbot has been trained to answer
1. Questions related to NTL - we provided the chatbot with our own data that consists of a list of questions that someone might ask about NTL, along with the answers. Chatbot will match the question with this data and if a match is found then it will print the appropriate output
2. Generic questions - another possibility is that the user can ask questions that is not related to NTL at all and in that case, we have provided the chatbot with an openai key. It will fetch the answer for such questions using the openai.

We have used fast api to host the server. The json text returned as a result is used by the website to provide a semantic chatbot experience
