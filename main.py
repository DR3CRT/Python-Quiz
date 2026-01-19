
score = 0 # Initial score set to zero

quiz = [ # storing of questions, options and the correct answers
    {
        "Question": "Which of these is a Star Trek character? ",
        "Options": ["A. Marty McFly",
                    "B. Spock",
                    "C. Dr Frink",
                    "D. Dr Mario"] ,
        "Answer": "B"

    },
    {
        "Question": "Who developed Minecraft?",
        "Options": ["A. Phil Fish",
                    "B. Edmund McMillen",
                    "C. Notch",
                    "D. Peter Molyneux "] ,
        "Answer": "C"

    },
    {
        "Question": "Who was Hogwarts Headmaster?",
        "Options": ["A. Gandalf",
                    "B. Merlin",
                    "C. Jareth, the Goblin King",
                    "D. Dumbledore "] ,
        "Answer": "D"

    },
    {
        "Question": "Where do the Simpsons Live?",
        "Options": ["A. 742 Evergreen Terrace",
                    "B. 64 Zoo Lane",
                    "C. Bag End",
                    "D. 1640 Riverside Drive "] ,
        "Answer": "A"

    },
    {
        "Question": "Which of these is a Star Wars Character?",
        "Options": ["A. Captain Pickard",
                    "B. Captain Crunch",
                    "C. Captain Rex",
                    "D. Captain Hook "] ,
        "Answer": "C"

    },
    {
        "Question": " In The Hitchhikers Guide To The Galaxy, what is the answer to the Ultimate Question of Life, the Universe and Everything?",
        "Options": ["A. Pi",
                    "B. 78",
                    "C. 42",
                    "D. 100001 "] ,
        "Answer": "C"

    },
    {
        "Question": "In Red Dwarf, what is Dave Lister’s favorite food?",
        "Options": ["A. Fish fingers and custard",
                    "B. Chicken vindaloo",
                    "C. Gazpacho soup",
                    "D. Triple fried egg, chili, and chutney sandwiches"] ,
        "Answer": "D"

    },
    {
        "Question": "In Blade Runner (1982), what are the bioengineered beings called?",
        "Options": ["A. Synthetics",
                    "B. Cylons",
                    "C. Replicants",
                    "D. Androids"] ,
        "Answer": "C"

    },
    {
        "Question": "In Back to the Future, how much power does the DeLorean need to travel through time?",
        "Options": ["A. 1.21 Gigawatts",
                    "B. 2.21 Gigawatts",
                    "C. 1.21 Terawatts",
                    "D. 500 Horsepower "] ,
        "Answer": "A"

    },
    {
        "Question": "In Jurassic Park, what kind of dinosaur kills Dennis Nedry?",
        "Options": ["A. Tyrannosaurus Rex",
                    "B. Velociraptor",
                    "C. Dilophosaurus",
                    "D. Triceratops"] ,
        "Answer": "C"

    },
    {
        "Question": "What is the name of the shark from Jaws?",
        "Options": ["A. Bruce",
                    "B. Benny",
                    "C. Bertram",
                    "D. Rufus"],
        "Answer": "A"

    },
    {
        "Question": "Which of these is the name of a Muppet?",
        "Options": ["A. Freddy Frog",
                    "B. Gerbil",
                    "C. Creature",
                    "D. Waldorf"],
        "Answer": "D"

    },
    {
        "Question": "What is the name of the famous mascot from the View Askewniverse?",
        "Options": ["A. Timmy the Sapphire Shrimp",
                    "B. Mooby the Golden Calf",
                    "C. Eric the Ruby Rhino",
                    "D. Henry the Orange Cat"],
        "Answer": "B"

    },
    {
        "Question": "Finish the famous movie quote, 'You shall not.....'",
        "Options": ["A. Pass",
                    "B. Scream",
                    "C. Hit me",
                    "D. Dance"],
        "Answer": "A"

    },
    {
        "Question": "Which of these actors has never played Batman?",
        "Options": ["A. Christian Bale",
                    "B. Adam West",
                    "C. Adam Sandler",
                    "D. Val Kilmer"],
        "Answer": "C"

    },


]
# end of questions, options and correct answers
print(f"What is your name? ") # user prompted to input name
name = input() # user inputs name
for q in quiz:
    print(q["Question"]) # question is printed
    for opt in q["Options"]:
        print(opt) # options of answers displayed one below the other using A...(answer),B...(answer),C...(answer),D...(answer)
    print(f"Choose an option, A, B, C, or D") # user prompted to select answer using A,B,C,D
    answer = input().upper() # any input is converted to upper case for validation of answers
    if answer == q["Answer"]:
        score += 1 # if user answers correctly, 1 is added to the score
        print(f"Correct!") # a positive message is displayed for correct answer
    else:
        print(f"Incorrect!") # a negative message is displayed for incorrect answer
print(f"Well done", name, "Your final score is") # closing message is printed with name and 'your final score is'
if score <= 5:
    print(score, f" you suck") # if score is equal to or less than 5, a message is displayed
elif score == 10:
    print(score, f" Not bad") # if score is equal to 10 a message is displayed
elif score <= 14:
    print(score, f" Wow you are good") # if score is equal to or less than 14, a message is displayed
else:
    print(score, f" NERD!!!!") # if top score is reached a message is displayed


