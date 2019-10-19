# © 2019, Drew Goodman, all rights reserved

import random

art = '''
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........
'''

responses = {
    1: "It is certain",
    2: "It is decidedly so",
    3: "Without a doubt",
    4: "Yes - definitely",
    5: "You may rely on it",
    6: "As I see it, yes",
    7: "Most likely",
    8: "Outlook good",
    9: "Yes",
    10: "Signs point to yes",
    11: "Reply hazy, try again",
    12: "Ask again later",
    13: "Better not tell you now",
    14: "Cannot predict now",
    15: "Concentrate and ask again",
    16: "Don't count on it",
    17: "My reply is no",
    18: "My sources say no",
    19: "Outlook not so good",
    20: "Very doubtful",
}

print(art)
print("M A G I C   8 - B A L L\n\n")
n = input("\nPlease ask the Magic 8-Ball a question! \n\tThen press enter to continue: \n\n").strip()

while n != "":
    roll = random.randint(1,(len(responses)))
    print(f'MAGIC 8-BALL SAYS:     "{responses[roll]}"')
    n = input("\nPlease ask the Magic 8-Ball another question! \n\tThen press enter to continue: \n\n")
else:
    print("\nCome back again soon!")