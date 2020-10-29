# John Nguyen
# Integration Project
# Game is base on story telling where a hero come save the world
# Game is option choice (1,2)

# info about developer printed
def developer_info():
    print("Hi, my name is John Nguyen.")
    print("This is my first time coding a game. Hope you like it.")
    return


# Title of the Game
def intro_game():  # intro to the app
    print("The game is call Pick Your Faith"' '"v1.0.1")
    print("The game is base on hero who is called upon by people")
    print("And defeat evil man who rule the world.")
    return


# Game ask for player name and ask if they want to play
def welcome_player():
    player_name = input("Please enter your name: ")
    print("Welcome", player_name, ''",hope you enjoy playing this game.")
    return player_name


# game end when player doesnt want to play
def end_game():  # player doesnt want to play the game
    print("Sorry! Maybe next time.")
    exit()  # exit will kill the app, without exit(), it will go into
    # infinite loop


# player enter hero name that will be use in the story
def player_hero():
    hero_name = input("Please enter your hero name?: ")
    return hero_name


# player/hero health point in game
def health_point():
    health_point = 100
    return health_point


# player//hero money currency
def cash_money():
    cash_money: float = 100.00  # float will include decimal spots for numbers
    return cash_money


# start of the story
def game_intro():  # story will begin after player choose 1
    print("The game you will be playing is an adventure game")
    print("and you are the hero of this story.")
    print("Each choices you make will determine if you will make it to the "
          "end or not.")
    print("Your goal is to survive till the end or else its Game over.")
    # time.sleep(.5)
    print("Your hero will start with 100 health point and $100.00 cash money.")
    print("With the cash, you can purchase item from the vendor.")
    # .sleep(.5)
    print("The game will start.....")
    # time.sleep(.5)
    print("Once upon a time, there was a evil men who rule over the world.")
    print("People are crying for help.")
    print("Who is going save them?")
    print(hero_name, "has arrived and here to save you from the evil man.")
    print(hero_name, "will save you! ")
    return


# bear stop hero from crossing
def bear_story():
    global hero_health  # global variable
    global hero_coin  # global variable
    print("While walking on the path to save the world,", hero_name,
          "encounter a bear, but need to cross over the bridge.")
    print("Do you want to attack the bear and get over the bridge?")
    print("If you attack and defeat the bear, you will be rewarded")
    attack_bear = input("Do you want to attack the bear? Yes [1] or No [2]: ")
    while attack_bear != 1 and attack_bear != 2:
        if attack_bear == "1":
            print(hero_name, "attacked and defeated the bear.", hero_name,
                  "rewarded 10 coins. But lost 10hp.")
            hero_health -= 10  # operator to subtract from variable
            hero_coin += 10  # operator to add to variable
            print(hero_name, " ", hero_health, "hp", " ""coins $", format(
                hero_coin,
                "0.2f"), sep='')
            # sep operator help separation between each comma
        elif attack_bear == "2":
            print(hero_name, "decided to run around the bear. But the bear "
                             "was fast and slashed hero's face.", hero_name,
                  "lost 5hp and 5 coins.")
            hero_health -= 5  # operator to subtract health point
            hero_coin -= 5  # operator to subtract cash/money from hero
            print(hero_name, " ", hero_health, "hp", " ""coins $",
                  format(hero_coin,
                         "0.2f"), sep='')  # sep add space between strings
        else:
            attack_bear = input(
                "Invalid!, Try again. Do you want to attack the bear? Yes ["
                "1] or No [2]: ")
        return


# beautiful women turn into witch and attack hero
# having issue on this def
def witch_attk(hero_health):
    print("AWWWW!!! The beautiful women turned into a evil witch.")
    print("The evil witch attacked hero.")
    hero_health -= 10
    print(hero_name, '', hero_health, "hp.")
    return


# witch disguise as real human
def witch_story():
    global hero_health
    global hero_coin
    print("After crossing the bridge,", hero_name,
          "encounter beautiful women who needed some help.")
    print("Help!" * 2, "Strong hero please help, cry the women",
          sep="")  # * operator where it multiply help 2 times
    # sep operator for separating
    print(
        "Her wagon's wheel came off while traveling and she need your help putting wheel back on.")
    fix_wagon = input("Do you want to help fix the wagon? Yes [1] or No [2]: ")
    while fix_wagon != 1 and fix_wagon != 2:  # != player input 1, they will
        # move on to next step.
        if fix_wagon == "1":
            print("AWWWW!!!, The beautiful women turned into a evil witch.")
            print("The evil witch attacked the hero.")
            hero_health -= 10  # subtract hp from attack from witch
            print(hero_name, '', hero_health, "hp.")
            atk_back = input("Do you want to attack back and kill the evil "
                             "witch? Yes [1] or No [2]: ")
            while atk_back != 1 and atk_back != 2:  # != operator for not
                # equal. if player doesnt input 1 or 2, they will get invalid.
                if atk_back == "1":
                    print(hero_name, "attack and defeated the evil witch.")
                    print("You been rewarded 5 coins and lost 10 hp")
                    hero_health -= 10
                    print(hero_name, " ", hero_health, "hp", " ""coins $",
                          format(hero_coin, "0.2f"), sep='')
                    return
                else:
                    print(hero_name, "ran away from the evil witch.")
                    return
        elif fix_wagon == "2":
            print("Pretty please hero, please help with my wagon.")
            # having errors right now.
            # second_chance = input("Do you want to change your mind and fix
            # the wagon? Yes [1] or No [2]: ")
            # while second_chance != 1 and second_chance != 2:
            # if second_chance == 1:
            # witch_attk()
            # else:
            # print("Sorry, I have to go save the world.",hero_name,
            # "left the scene.")
            return
        else:
            fix_wagon = input("Invalid, Try again. Do you want to help fix "
                              "the wagon? Yes [1] or No [2]: ")
            return


# question from vendor
def vendor_quiz():
    global hero_health
    global hero_coin
    print("Question: Without using google, what is the output of 3**5.")
    # ** exponentiation operator where it take the first number and power to
    # second number
    quiz_answer = input("243 [1] or 33333 [2] or 3535 [3]: ")
    while quiz_answer != 1 and quiz_answer != 2 and quiz_answer != 3:
        if quiz_answer == "2" or quiz_answer == "3":
            print("Sorry, you answer the question wrong.")
            print("You will have to pay a higher price for the item.")
            higher_price()
            return
        else:
            print("Congratution, you answer the question right is right.")
            print("You can buy the items at half of original price.")
            vendor_selling()
            purchase_potion = input("Which one do you want buy? [1]. [2]. ["
                                    "3]. [4]: ")
            if purchase_potion == "1" and hero_coin >= 5:  # Player can
                # purchase if coins is more than 5
                hero_health += 5
                first_potion = 10 / 2  # operator for division. divide the
                # variable
                # coins by second number
                hero_coin -= first_potion
                return hero_health, hero_coin
            elif purchase_potion == "2" and hero_coin >= 10:  # Player can
                # purchase if coins is more than 10
                hero_health += 10
                second_potion = 20 / 2  # operator for division. divide the
                # variable
                # coins by second number
                hero_coin -= second_potion
                return hero_health, hero_coin
            elif purchase_potion == "3" and hero_coin >= 15:  # >= operator
                # greater or equal
                hero_health += 15
                third_potion = 30 / 2  # operator for division. divide the
                # variable
                # coins by second number
                hero_coin -= third_potion
                return hero_health, hero_coin
            elif purchase_potion == "4" and hero_coin >= 25:  # >= hero coins
                # have to be bigger than second number for player to purchase
                hero_health += 50
                last_potion = 50 // 2  # operator for floor division. divide
                # the
                # variable coins by second number into whole number
                hero_coin -= last_potion
                return hero_health, hero_coin
            else:
                purchase_potion = input("Invalid, Try again. [1]. [2]. [3]. ["
                                        "4]: ")
            return


# list of items that are in txt file and open operator call it
def vendor_selling():
    purchase_item = open('p_resources\items.txt')  # open operator where
    # read txt file from your computer in which they have to be in the same
    # folder
    for item in range(1, 5):
        buy_item = purchase_item.readline()
        print(str(item) + ". ", buy_item.rstrip())


# price change if player answer question wrong
def higher_price():
    purchase_item = open('p_resources\items2.txt')  # open operator where
    # read txt file from your computer in which they have to be in the same
    # folder
    for item in range(1, 5):
        buy_item = purchase_item.readline()  # readline will read line by line
        print(str(item) + ". ", buy_item.rstrip())  # rstrip() removes any
        # trailing characters at the end of strings


# player/hero get to buy item from vendor
def vendor_scam():
    global hero_health
    global hero_coin
    print("After leaving the scene,", hero_name, ''"continued on his journey.")
    print("While walking,", hero_name, "see a vendor selling some items.")
    print(hero_name, "stop and looked at the items and wanted some of them.")
    print("Here the item:")
    vendor_selling()
    print("The vendor told the hero:")
    print(
        "Before you can buy the item, you will need to solve a problem for me.")
    print("If you can get it right, you can buy item at half of original "
          "price")
    print("if not, you will have to buy the item at higher price.")
    vendor_quiz()


developer_info()
intro_game()
welcome_player()
player_answer = input("Would you like play this game? Yes [1] and No [2]: ")
while player_answer != 1 and player_answer != 2:
    if player_answer == "1":
        hero_name = player_hero()
        game_intro()
        hero_health = health_point()
        hero_coin = cash_money()
        bear_story()
        witch_story()
        vendor_scam()

    elif player_answer == "2":
        end_game()
    else:
        player_answer = input("Invalid!, Try again. Yes [1] or No [2]: ")

# import time
# import random
