quizs = {
"question1":{
	"question": "What is the capital of France",
	"answer": "Paris"	
},
	"question2":{
		"question": "What is the capital of Portugal",
		"answer": "Lisbon"	
},
	"question3":{
		"question": "What is the capital of Switzerland",
		"answer": "Bern"	
},
	"question4":{
		"question": "What is the capital of Germany",
		"answer": "Berlin"	
},
	"question5":{
		"question": "What is the capital of Italy",
		"answer": "Rome"	
},
	"question6":{
		"question": "What is the capital of Spain",
		"answer": "Madrid"	
},
	"question7":{
		"question": "What is the capital of Australia",
		"answer": "Vienna"	

	},


}

score = 0

for key, value in quizs.items():
	print(value["question"])
	answer = input("Answer ? ")
	if answer.lower() == value["answer"].lower():
		print("Correct!")
		score +=1
		print ("Your score is: ", str(score))
		print("")
		print("")
		print("")

	else:
		print("Incorrect! The correct answer is: ", value["answer"])
		print ("Your score is: ", str(score))
		print("")
		print("")
		print("")

percentage = (score/7)*100

print(f"You got {str(score)} out of 7")
print(f"Your pecentage is: {str(int(percentage))}%")