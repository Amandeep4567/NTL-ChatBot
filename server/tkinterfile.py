
from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"




import re
import long_responses as long
import openai
import uvicorn
from fastapi import FastAPI

global m
global n
app=FastAPI()

def func(value):
    return ''.join(value.splitlines())


# Send function
def send():
	send = e.get()
	t=send
	txt.insert(END, "\n" +'You: '+send)
	# Testing the response system
	split_message = re.split(r'\s+|[,;?!.-]\s*', t.lower())
	n=t
    
	if('' in split_message):
		split_message.remove('')


	h=['hello', 'hi', 'hey', 'sup', 'heyo', 'Hey there!']
	b=['bye', 'goodbye']
	t1=['thank', 'thanks']
	if('ntl' in split_message ):
		query=get_response(split_message)
		m=query
		txt.insert(END, "\n" +'Bot: ' + query)
		
	elif(t in h):
		m='Hello!'
		txt.insert(END, "\n" +'Bot: Hello! ')
	elif(t in b):
		m='See you!'
		txt.insert(END, "\n" +'Bot: See you!')
		

	elif(t in t1):
		m='You\'re welcome!'
		txt.insert(END, "\n" +'Bot:You\'re welcome!')
		
	else:
		res=gpt3(t)
		m=res
		txt.insert(END, "\n" +'Bot: '+func(res))

	
	

	# user = e.get().lower()

	# if (user == "hello"):
	# 	txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	# elif (user == "hi" or user == "hii" or user == "hiiii"):
	# 	txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	# elif (user == "how are you"):
	# 	txt.insert(END, "\n" + "Bot -> fine! and you")

	# elif (user == "fine" or user == "i am good" or user == "i am doing good"):
	# 	txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	# elif (user == "thanks" or user == "thank you" or user == "now its my time"):
	# 	txt.insert(END, "\n" + "Bot -> My pleasure !")

	# elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
	# 	txt.insert(END, "\n" + "Bot -> We have coffee and tea")

	# elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
	# 	txt.insert(
	# 		END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

	# elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
	# 	txt.insert(END, "\n" + "Bot -> Have a nice day!")

	# else:
	# 	txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)




def gpt3(stext):
     openai.api_key = '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'
     response = openai.Completion.create(
       engine= "text-davinci-003",
       
       prompt=stext,
              temperature=0.1,
              max_tokens=1000,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
     )
     content = response.choices[0].text.split('.')
     
     return response.choices[0].text

# def gpt3(stext):
#     openai.api_key = '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'
#     response=openai.Completion.create(
#     model="text-davinci-003",
#     prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ:",
#     temperature=0,
#     max_tokens=100,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=["\n"]
#     )
#     content = response.choices[0].text.split('.')
#     print(content)
#     return response.choices[0].text
@app.get('/')
def fun():
    return {'question':n,'answer':m,}

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        word=word.lower()
        if word in recognised_words:
            message_certainty += 1

    


    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    count=0
    # Checks that the required words are in the string
    for word in required_words:
        word=word.lower()
        if word not in user_message:
         
            count=count+1
            #has_required_words = False
    if(count==len(required_words)):
        has_required_words = False



    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100*(len(required_words)-count))
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list

        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'Hey there!'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    #response('its student driven club',['what', 'is', 'NTL'], required_words=['what','NTL'])
    response("NTL or Next Tech Lab is a successful student-led club that promotes an environment of invention and innovation.",re.split(" ","What is NTL the full form of next tech lab"),required_words=['what','NTL'])
    response("Students run the NTL.",re.split(" ","Who runs the NTL"),required_words=['runs','ntl','who'])
    response("NTL was founded by  Adithyn Anshuman.",re.split(" ","Who is the head of NTL"),required_words=['who','ntl','head'])
    response("NTL was founded by  Adithyn Anshuman. It is a student run lab and is headed by the syndicates. The newly recruited members are the associates of next tech lab and assosicates who shows dedication towards the lab becomes the member of NTL.",re.split(" ","NTL structure What are the positions in NTL"),required_words=['structure','positions','ntl'])
    response("NTL is a student run lab. Every individual in NTL is constantly learning and implementing.",re.split(" ","How does NTL work actually works"),required_words=['work','works','how'])
    response("NTL students have published research papers, represented the university in numerous hackathons and won coding competetions.",re.split(" ","What are the achievements of NTL"),required_words=['achievements','ntl'])
    response("only ntl members are allowed to come to ntl.",re.split("","Can anyone come to ntl i to visit ntl"),required_words=['come','visit','can','comes'])
    response("NTL is situated in the old academic block.",re.split(" ","Where is NTL location"),required_words=['location','where'])
    response("Their are 5 labs in NTL, namely Mckarthy, Norman, Posch, Sathoshi and Tesla. Students can pick whichever lab they want to work in. It is possible to change labs after joining but the student has to provide valid reasons for the shift.",re.split(" ","What are the different labs in Can I shift from one to another Is movement from one lab lab possible Divisions in labs names"),required_words=['labs','what','divisions','movement'])
    response("NTL has around 60 people at the moment.",re.split(" ","How many people are there in NTL"),required_words=['people','how','many'])
    response("In NTL there are no teachers, everyone is a student. Students learn and implement concepts on their own and if they require any help then they can ask their peers to guide them. NTL helps students in understanding how to overcome challenges on their own and at the same time, it compells students to be innovative.",re.split(" ","How NTL is different from other labs Why should I join How Helps What are the advantages of joining Does any one teach in"),required_words=['how','teach','advantages','diffrent','from'])
    response("Any student can be a part of NTL if they are truly passionate about technology. However, it always helps to know some basic concepts before joining. Here is a list of some pre-requisites for each lab:\n Mckarthy - python programming language basics of numpy and pandas\nNorman - HTML, CSS and basics of javascript\nTesla - basic knowledge of networking, micro-controllers and how internet works\nPosch - beginner level knowledge of C#\nSatoshi - linux, front-end knowledge and one programming language",re.split(" ","What are the prerequisites to join NTL what do i need to know to join ntl should i know something to is any prior course required to join"),required_words=['prerequisites','course','required','join'])
    response("The hierarchy of the members of NTL is as follows:\nThe ones who joined as new members will be given the tag of 'associates'\nThen the one who has done some work in their respective fields are promoted to'members' from 'associates'\nThe ones who monitor all the things related to the particular labs and take charge\nhave board members and syndicate tags\nThere is no particular syndicate for the Next tech lab, we have 2 syndicates for\neach and evey lab.  totally there are 15 syndicates in the next tech lab",re.split(" ","What is the syndicate in NTL hierarchy Who are members is the syndicate What are assosicates How many syndicates What position will i get"),required_words=['syndicates','position','hierarchy','members'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
   
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(split_message):
    # split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    
    # if('' in split_message):
    #     split_message.remove('')
   
    response = check_all_messages(split_message)
    return response





lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()

