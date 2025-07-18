import random
T= [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What's your most embarrassing moment?",
    "Do you have a secret crush?",
    "Have you ever broken something and blamed someone else?",
    "What's the most childish thing you still do?",
    "What's the one thing you never told your parents?",
    "Have you ever stalked someone online?",
    "Who was your first love?",
    "Do you keep any secrets from your friends?"
    "Who was your first crush?",
    "Do you have a secret crush right now?",
    "Have you ever had a crush on a teacher?",
    "Have you ever had a romantic dream about someone here?",
    "What's your idea of a perfect first date?",
    "Would you date someone younger than you?",
    "Have you ever stalked someone online?",
    "Have you ever lied about liking someone?",
    "Would you kiss your crush if they asked right now?",
    "Do you believe in love at first sight?",
    "What is one thing you've never told anyone?",
    "What's your biggest fear?",
    "What's your most embarrassing moment?",
    "Have you ever broken something and blamed someone else?",
    "Have you ever cheated on a test?",
    "Have you ever lied to your parents about where you were?",
    "Have you ever stolen anything?",
    "Who do you secretly envy?",
    "Do you keep a diary?",
    "Have you ever cried for no reason in public?"
]
D= [
    "Do 10 pushups right now.",
    "Call your crush and say 'I love you.'",
    "Text your best friend and say 'I have a secret, guess what!'",
    "Sing a song loudly for 30 seconds.",
    "Send a voice note to someone saying a random tongue twister.",
    "Dance without music for 1 minute.",
    "Eat a spoonful of salt or chili powder.",
    "Speak in a funny accent for the next 3 turns.",
    "Change your profile picture to a funny one for 1 hour.",
    "Say something romantic to the person on your right.",
    "Post 'I am a potato' on your Instagram story.",
    "Act like a monkey for 20 seconds.",
    "Reveal the last message you sent.",
    "Let the group give you a new nickname.",
    "Close your eyes and send a random emoji to someone.",
    "Take a selfie making a weird face and send it to the group.",
    "Talk non-stop for 2 minutes.",
    "Let someone else write a WhatsApp message for you and you must send it without editing.",
    "Do a fake crying scene like in a drama",
    "Read out loud your last 5 Google searches.",
    "Sing the chorus of your guilty pleasure song.",
    "Tell the group your most embarrassing nickname.",
    "Send a selfie making a duck face to a random contact.",
    "Let someone else go through your phone gallery for 30 seconds.",
    "Tell the group about your first crush.",
    "Let someone send one emoji from your phone to your ex (if you have one).",
    "Post an old cringy photo on your story for 5 mins.",
    "Say something flirty to the person you like in a voice note.",
    "Talk about your weirdest dream ever",
    "Say 'I like you' to someone you secretly admire (even fake if no one).",
    "Write a 4-line love poem for someone in the group.",
    "Compliment every person in the group one by one.",
    "Share your dream date idea.",
    "Describe your ideal partner using only emojis.",
    "Send a heart emoji to your crush without explanation.",
    "Call someone and say 'I'm missing you'.",
    "Sing a romantic song for someone you find cute.",
    "Flirt with someone in the group for 1 full minute.",
    "Say something cheesy like a movie dialogue with full drama",
    "Do a 30-second roast of yourself."
]
print(":) TRUTH OR DARE ")
print("ARE YOU READY ?")
print("OK LET'S START....")
NAME=input("ENTER YOUR NAME :")
print("          _______________________.   ")
print("ARE YOU AFRAID ?", NAME)
YN=input("ENTER YES OR NO..")
if YN =="NO" or YN == "no" :
    print("OHOOO....OK SELECT:")
    while True: 
        TD=input("TRUTH OR DARE: ")
        if TD =="TRUTH" or TD == "truth" :
            print("BE HONEST: ", random.choice(T))
            print(" WRITE YOUR ANSWER 👇")
            AN=input("👉 ")

        elif TD =="DARE" or TD == "dare" :
            print("DARE😈: ", random.choice(D))
            DN=input("DONE OR NOT ? ")
            if DN =="DONE" or DN == "done":
                print("BRAVO")
            elif DN == "NOT" or DN == "not" :
                print("BHAI TUM TRUTH HI LO....RHNE DO DARE TUMHARE BSS KA NHI HAI..")
            else:
                print("WRONG INPUT!!!!!....RESTART GAME!!!!")
        else:
            ("WRONG INPUT....DARR GYE KYA!!!!!!")
        
else:
    print("DARR LG RHA THA TO START KYU KIYA... ")
    