
score = 0

quiz = [
    {
        "Question": "Which of these is a Star Trek character? ",
        "Options": ["A. Marty McFly \n",
                    "B. Spock \n",
                    "C. Dr Frink \n",
                    "D. Dr Mario"] ,
        "Answer": "B"

    },
    {
        "Question": "Who developed Minecraft?",
        "Options": ["A. Phil Fish \n",
                    "B. Edmund McMillen \n ",
                    "C. Notch \n",
                    "D. Peter Molyneux "] ,
        "Answer": "C"

    },
    {
        "Question": "Who was Hogwarts Headmaster?",
        "Options": ["A. Gandalf \n",
                    "B. Merlin \n",
                    "C. Jareth, the Goblin King \n",
                    "D. Dumbledore "] ,
        "Answer": "D"

    },
    {
        "Question": "Where do the Simpsons Live? \n",
        "Options": ["A. 742 Evergreen Terrace \n",
                    "B. 64 Zoo Lane \n",
                    "C. Bag End \n",
                    "D. 1640 Riverside Drive "] ,
        "Answer": "A"

    },
    {
        "Question": "Which of these is a Star Wars Character?",
        "Options": ["A. Captain Pickard \n",
                    "B. Captain Crunch \n",
                    "C. Captain Rex \n",
                    "D. Captain Hook "] ,
        "Answer": "C"

    },
    {
        "Question": " In The Hitchhikers Guide To The Galaxy, what is the answer to the Ultimate Question of Life, the Universe and Everything?",
        "Options": ["A. Pi \n",
                    "B. 78 \n",
                    "C. 42 \n",
                    "D. 100001 "] ,
        "Answer": "C"

    },
    {
        "Question": "In Red Dwarf, what is Dave Lister’s favorite food?",
        "Options": ["A. Fish fingers and custard \n",
                    "B. Chicken vindaloo \n",
                    "C. Gazpacho soup \n",
                    "D. Triple fried egg, chili, and chutney sandwiches"] ,
        "Answer": "D"

    },
    {
        "Question": "In Blade Runner (1982), what are the bioengineered beings called?",
        "Options": ["A. Synthetics \n",
                    "B. Cylons \n",
                    "C. Replicants \n",
                    "D. Androids"] ,
        "Answer": "C"

    },
    {
        "Question": "In Back to the Future, how much power does the DeLorean need to travel through time?",
        "Options": ["A. 1.21 Gigawatts \n",
                    "B. 2.21 Gigawatts \n",
                    "C. 1.21 Terawatts \n",
                    "D. 500 Horsepower "] ,
        "Answer": "A"

    },
    {
        "Question": "In Jurassic Park, what kind of dinosaur kills Dennis Nedry?",
        "Options": ["A. Tyrannosaurus Rex \n",
                    "B. Velociraptor \n",
                    "C. Dilophosaurus \n",
                    "D. Triceratops"] ,
        "Answer": "C"

    },
    {
        "Question": "What is the name of the shark from Jaws?",
        "Options": ["A. Bruce \n",
                    "B. Benny \n",
                    "C. Bertram \n",
                    "D. Rufus"],
        "Answer": "A"

    },
    {
        "Question": "Which of these is the name of a Muppet?",
        "Options": ["A. Freddy Frog \n",
                    "B. Gerbil \n",
                    "C. Creature \n",
                    "D. Waldorf"],
        "Answer": "D"

    },
    {
        "Question": "What is the name of the famous mascot from the View Askewniverse?",
        "Options": ["A. Timmy the Sapphire Shrimp \n",
                    "B. Mooby the Golden Calf \n",
                    "C. Eric the Ruby Rhino \n",
                    "D. Henry the Orange Cat"],
        "Answer": "B"

    },
    {
        "Question": "Finish the famous movie quote, 'You shall not.....'",
        "Options": ["A. Pass \n",
                    "B. Scream \n",
                    "C. Hit me \n",
                    "D. Dance"],
        "Answer": "A"

    },
    {
        "Question": "Which of these actors has never played Batman?",
        "Options": ["A. Christian Bale \n",
                    "B. Adam West \n",
                    "C. Adam Sandler \n",
                    "D. Val Kilmer"],
        "Answer": "C"

    },


]
print(f"What is your name? ")
name = input()
for q in quiz:
    print(q["Question"])
    print(q["Options"])
    print(f"Choose an option, A, B, C, or D")
    answer = input().upper()
    if answer == q["Answer"]:
        score += 1
        print(f"Correct!")
    else:
        print(f"Incorrect!")
print(f"Well done", name, "Your final score is")
if score <= 5:
    print(score, f" you suck")
elif score == 10:
    print(score, f" Not bad")
elif score <= 14:
    print(score, f" Wow you are good")
else:
    print(score, f" NERD!!!!")


