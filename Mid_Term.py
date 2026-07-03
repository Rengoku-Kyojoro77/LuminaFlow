import datetime as dt
import time
import random
import turtle

def main_menu():
    while True:
        print("\n=== PROJECT MAIN MENU ===")
        print("1. Birthday Countdown")
        print("2. Secret Message Encoder/Decoder")
        print("3. Hungry Snake Game")
        print("4. Card Game (War)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5 or name): ").strip().lower()
        
        if choice in ['1', 'birthday countdown', 'countdown']:
            print("\n--- Starting Birthday Countdown ---")
            print('Welcome to your birthday countdown')

            current_year = dt.datetime.now().year
            year = int(input('Which year were you born in?\n'))

            while current_year < year:
                print('dont try to be too smart!! that date belongs to the future')
                print('Try again')
                year = int(input('Which year were you born in?\n'))

            month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))

            while month < 1 or month > 12:
                print('Invalid month! Please enter a number between 1 and 12.')
                print('Try again')
                month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))

            day = int(input('Which day in that month?\n'))

            while day < 1 or day > 31:
                print('Invalid day! Please enter a number between 1 and 31.')
                print('Try again')
                day = int(input('Which day in that month?\n'))

            date_birth = dt.datetime(year, month, day)
            weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            weekday_num = date_birth.weekday()
            
            print('You may have forgotten which day of the week it was ...')
            print('But I can tell you ... it was a ...', end=' ')
            print(weekday_names[weekday_num])

            if month == 1:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  AQUARIUS/CAPRICORN!??\n\n')
                print('Aquarius is the visionary humanitarian and original thinker of the zodiac.\n They look toward the future, valuing innovation, intellectual freedom, and the collective progress of society over tradition.\nCore Trait: Independent innovation.\nSuperpower: Visionary thinking.\nWeakness: Emotional detachment.\n\n')
                print('Capricorn represents ambition, discipline, and long-term vision.\n They possess the patience to climb the highest mountains, building legacy, structure, and order through sheer grit and responsibility.\nCore Trait: Strategic ambition.\nSuperpower: Relentless discipline.\nWeakness: Rigidness.\n')

            elif month == 2:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  PISCES/AQUARIUS!??\n\n')
                print('Pisces is the dreamer, mystic, and artist.\n Boundless empathy allows them to absorb emotions and connect deeply with the spiritual realm.\n They express their rich inner world through art and compassion.\nCore Trait: Boundless imagination.\nSuperpower: Creative empathy.\nWeakness: Escapism.\n\n')
                print('Aquarius is the visionary humanitarian and original thinker of the zodiac.\n They look toward the future, valuing innovation, intellectual freedom, and the collective progress of society over tradition.\nCore Trait: Independent innovation.\nSuperpower: Visionary thinking.\nWeakness: Emotional detachment.\n')
                
            elif month == 3:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  ARIES/PISCES!??\n\n')
                print('Aries is the trailblazer of the zodiac.\n Driven by intense passion and high energy, they approach life with a fearless, competitive spirit.\n They excel at starting new projects and thrive on challenges.\nCore Trait: Bold initiative.\nSuperpower: Unshakeable courage.\nWeakness: Impatience.\n\n')
                print('Pisces is the dreamer, mystic, and artist.\n Boundless empathy allows them to absorb emotions and connect deeply with the spiritual realm.\n They express their rich inner world through art and compassion.\nCore Trait: Boundless imagination.\nSuperpower: Creative empathy.\nWeakness: Escapism.\n')
                    
            elif month == 4:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  TAURUS/ARIES!??\n\n')
                print('Taurus represents stability, patience, and grounded strength.\n They value comfort, consistency, and the finer things in life.\n Known for their incredible work ethic, they build lasting foundations.\nCore Trait: Steady reliability.\nSuperpower: Practical determination. Weakness: Stubbornness.\n\n')
                print('Aries is the trailblazer of the zodiac.\n Driven by intense passion and high energy, they approach life with a fearless, competitive spirit.\n They excel at starting new projects and thrive on challenges.\nCore Trait: Bold initiative.\nSuperpower: Unshakeable courage.\nWeakness: Impatience.\n')
                
            elif month == 5:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  GEMINI/TAURUS!!??\n\n')
                print('Taurus represents stability, patience, and grounded strength.\n They value comfort, consistency, and the finer things in life.\n Known for their incredible work ethic, they build lasting foundations.\nCore Trait: Steady reliability.\nSuperpower: Practical determination. Weakness: Stubbornness.\n\n')
                print('Gemini is the intellectual butterfly of the cosmos.\n Driven by constant curiosity, they are master communicators who process information rapidly.\n They love learning, sharing ideas, and adapting to change.\nCore Trait: Mental agility.\nSuperpower: Versatility.\nWeakness: Scattered focus.\n')

            elif month == 6:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  CANCER/LEO!!??\n\n')
                print('Cancer is the nurturing protector, deeply attuned to emotional undertones.\n They possess profound intuition and prioritize creating safe, loving spaces for family and friends.\n Their empathy is unmatched.\nCore Trait: Deep emotional depth.\nSuperpower: Natural intuition.\nWeakness: Moodiness.\n\n')
                print('Gemini is the intellectual butterfly of the cosmos.\n Driven by constant curiosity, they are master communicators who process information rapidly.\n They love learning, sharing ideas, and adapting to change.\nCore Trait: Mental agility.\nSuperpower: Versatility.\nWeakness: Scattered focus.\n')

            elif month == 7:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  CANCER/LEO!!??\n\n')
                print('Cancer is the nurturing protector, deeply attuned to emotional undertones.\n They possess profound intuition and prioritize creating safe, loving spaces for family and friends.\n Their empathy is unmatched.\nCore Trait: Deep emotional depth.\nSuperpower: Natural intuition.\nWeakness: Moodiness.\n\n')
                print('Leo radiates warmth, creativity, and magnetic charisma.\n Natural-born leaders, they love to celebrate life and inspire others.\n They are fiercely loyal friends with generous, golden hearts.\nCore Trait: Radiant confidence.\nSuperpower: Creative leadership.\nWeakness: Pride.\n')

            elif month == 8:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is ....... Leo / Virgo !!??\n\n')
                print('Virgo brings order, clarity, and precision to the world. They possess analytical minds and a deep desire to be of service.\n They excel at problem-solving and notice details others miss.\nCore Trait: Meticulous analysis.\nSuperpower: Practical efficiency.\nWeakness: Perfectionism.\n\n')
                print('Leo radiates warmth, creativity, and magnetic charisma.\n Natural-born leaders, they love to celebrate life and inspire others.\n They are fiercely loyal friends with generous, golden hearts.\nCore Trait: Radiant confidence.\nSuperpower: Creative leadership.\nWeakness: Pride.\n')

            elif month == 9:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  VIRGO/LIBRA!!??\n\n')
                print('Virgo brings order, clarity, and precision to the world. They possess analytical minds and a deep desire to be of service.\n They excel at problem-solving and notice details others miss.\nCore Trait: Meticulous analysis.\nSuperpower: Practical efficiency.\nWeakness: Perfectionism.\n\n')
                print('Libra seeks harmony, balance, and beauty in all things.\n Natural diplomats, they excel at seeing multiple perspectives and bringing people together.\n They value justice, art, and thriving relationships.\nCore Trait: Diplomatic grace.\nSuperpower: Creating harmony.\nWeakness: Indecisiveness.\n')

            elif month == 10:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  LIBRA/SCORPIO!!??\n\n')
                print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n They possess magnetic focus and can see right through deception.\n They undergo powerful personal transformations throughout life.\nCore Trait: Strategic intensity.\nSuperpower: Psychological insight.\nWeakness: Secretiveness.\n')

            elif month == 11:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  SCORPIO or SAGITTARIUS!!??\n\n')
                print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n They possess magnetic focus and can see right through deception.\n They undergo powerful personal transformations throughout life.\nCore Trait: Strategic intensity.\nSuperpower: Psychological insight.\nWeakness: Secretiveness.\n\n')
                print('Sagittarius is the eternal optimist and philosophical adventurer.\n Driven by a thirst for freedom and truth, they love exploring new cultures, ideas, and horizons with infectious enthusiasm.\nCore Trait: Philosophical exploration.\nSuperpower: Limitless optimism.\nWeakness: Bluntness.\n')

            elif month == 12:
                print('You are a very lucky person!!!')
                print('This is your horoscope for today!')
                print('Your zodiac is .......  SCORPIO/SAGITTARIUS!!??\n\n')
                print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n They possess magnetic focus and can see right through deception.\n They undergo powerful personal transformations throughout life.\nCore Trait: Strategic intensity.\nSuperpower: Psychological insight.\nWeakness: Secretiveness.\n\n')
                print('Capricorn represents ambition, discipline, and long-term vision.\n They possess the patience to climb the highest mountains, building legacy, structure, and order through sheer grit and responsibility.\nCore Trait: Strategic ambition.\nSuperpower: Relentless discipline.\nWeakness: Rigidness.\n')

            current_time = dt.datetime.now()
            thisyear = current_time.year
            thisyear_bday = dt.datetime(thisyear, month, day)

            Diff = current_time - date_birth
            view_diff = Diff.days // 365
            print('Your age is currently:', view_diff)

            if thisyear_bday > current_time:
                next_bday = thisyear_bday
            else:
                next_bday = dt.datetime(thisyear + 1, month, day)

            test_year = date_birth.year + 1
            bday_list = [0, 0, 0, 0, 0, 0, 0]
            while test_year < next_bday.year:
                test_date = dt.datetime(test_year, month, day)
                weekday_num_test = test_date.weekday()
                bday_list[weekday_num_test] = bday_list[weekday_num_test] + 1
                test_year = test_year + 1

            for kk in range(7):
                print('Your birthday was on a', weekday_names[kk], bday_list[kk], 'times.')
            print()

            print('Your next birthday will be on ...', end=' ')
            print(next_bday)
            print('That will be a ...', end=' ')
            weekday_num = next_bday.weekday()
            print(weekday_names[weekday_num])
            print()

            print("Press Ctrl+C to exit ticker loop...")
            print("Press Enter to start the countdown live ticker...")
            input()

            try:
                while next_bday > current_time:
                    current_time = dt.datetime.now()
                    dd = next_bday - current_time
                    days_left = dd.days
                    total_seconds_left = dd.seconds
                    total_mins_left, seconds_left = divmod(total_seconds_left, 60)
                    hrs_left, minutes_left = divmod(total_mins_left, 60)
                    print(f'Your next birthday is {days_left} days, {hrs_left} hrs, {minutes_left} mins, {seconds_left} secs away.', end='\r')
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nCountdown loop ended.")
                
            print("\nReturning to Main Menu...")

        elif choice in ['2', 'secret message encoder/decoder', 'encoder', 'decoder', 'secret message']:
            run_secret_messages()

        elif choice in ['3', 'hungry snake game', 'snake', 'snake game']:
            run_snake_game()

        elif choice in ['4', 'card game', 'cards', 'war', 'card war']:
            run_card_war_game()

        elif choice in ['5', 'exit', 'quit']:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def run_snake_game():
    print("\n--- Starting Hungry Snake Game ---")
    print("Close the graphics window to return to menu at any time.")
    
    bnd = turtle.Turtle()
    bnd.ht()
    bnd.penup()
    bnd.speed(0)
    bnd.fillcolor('lightgreen')
    bnd.begin_fill()
    bnd.goto(-220, -220)
    bnd.pendown()
    bnd.goto(220, -220)
    bnd.goto(220, 220)
    bnd.goto(-220, 220)
    bnd.goto(-220, -220)
    bnd.end_fill()

    t = turtle.Turtle()
    t.shape('square')
    t.color("black")
    t.penup()

    n_foods = 10
    list_of_foods = []
    for kk in range(n_foods):
        food = turtle.Turtle()
        food.penup()
        food.speed(0)
        food.shape("square")
        food.color("blue")
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        list_of_foods.append(food)

    pen = turtle.Turtle()
    pen.penup()
    pen.goto(180, 180)
    pen.color("white")
    pen.ht()

    report = turtle.Turtle()
    report.penup()
    report.goto(0, 0)
    report.color("white")
    report.ht()

    started = 0
    steps = 0

    def right():
        if t.heading() != 180.0:
            t.setheading(0.0)

    def left():
        if t.heading() != 0.0:
            t.setheading(180.0)

    def up():
        if t.heading() != 270.0:
            t.setheading(90.0)

    def down():
        if t.heading() != 90.0:
            t.setheading(-90.0)

    ts = t.screen
    ts.bgcolor("khaki")
    ts.listen()
    ts.onkey(right, "Right")
    ts.onkey(left, "Left")
    ts.onkey(up, "Up")
    ts.onkey(down, "Down")

    caught = [False] * n_foods
    segments = []
    game_over = False

    try:
        while not game_over:
            steps = steps + 1
            pen.write(len(segments), align="center", font=("Courier", 24, "normal"))
            for kk in range(len(list_of_foods)):
                if not caught[kk]:			
                    if t.distance(list_of_foods[kk]) < 20:
                        caught[kk] = True
                        list_of_foods[kk].color('green')
                        segments.append(list_of_foods[kk])
                        pen.clear()

            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)

            if len(segments) > 0:
                x = t.xcor()
                y = t.ycor()
                segments[0].st()
                segments[0].goto(x, y)

            t.forward(20)
            if t.xcor() > 10:
                started = 1

            if len(segments) == n_foods:
                if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
                    game_over = True
                    time.sleep(1)
                    t.clear()
                    t.ht()
                    for kk in range(len(segments)):
                        segments[kk].ht()
                    report.write("Steps Taken: " + str(steps), align="center", font=("Courier", 24, "normal"))
            time.sleep(0.1)
    except turtle.Terminator:
        print("Snake game screen closed early.")

    try:
        turtle.clearscreen()
    except:
        pass
    print("\nReturning to Main Menu...")


def run_secret_messages():
    def even_odd_swap(x):
        if len(x) % 2 != 0:
            x = x + ' '
        even_letters = x[::2]
        odd_letters = x[1::2]
        s = ''
        for i in range(len(even_letters)):
            s = s + even_letters[i]
            s = s + odd_letters[i]
        return s

    def reverse(x):
        return x[::-1]

    def reverse_word_concise(x):
        words = x.split()
        s = ''
        for everyword in words:
            s = s + reverse(everyword) + ' '
        return s

    def swap_middle(x):
        if len(x) % 2 != 0:
            x = x + ' '
        first_half = x[0:int(len(x)/2):1]
        second_half = x[int(len(x)/2)::1]
        s = ''
        s = s + second_half
        s = s + first_half
        return s

    def swap_middle_rev(x):
        x_swap = swap_middle(x)
        return reverse(x_swap)

    def swap_middle_rev_decode(x):
        x_rev = reverse(x)
        return swap_middle(x_rev)

    def general_swap(message, n, key):
        if len(message) % n != 0:
            message = message + (n - len(message) % n) * ' '
        s = ''
        for kk in range(int(len(message)/n)):
            temp = message[kk*n:(kk+1)*n:1]
            for jj in key:
                s = s + temp[jj]
        return s

    print("\n--- Secret Message Encoder/Decoder ---")
    user_text = input("Enter the message string: ")
    print("\nSelect Mode:")
    print("1. Even/Odd Swap")
    print("2. Full Reverse")
    print("3. Concise Reverse Words")
    print("4. Swap Middle halves")
    print("5. Swap Middle + Reverse combo")
    print("6. General Block Swap Encryption Key")
    
    mode = input("Enter choice (1-6): ").strip()
    if mode == '1':
        enc = even_odd_swap(user_text)
        print("Encoded:", enc)
        print("Decoded:", even_odd_swap(enc))
    elif mode == '2':
        enc = reverse(user_text)
        print("Encoded:", enc)
        print("Decoded:", reverse(enc))
    elif mode == '3':
        enc = reverse_word_concise(user_text)
        print("Encoded:", enc)
    elif mode == '4':
        enc = swap_middle(user_text)
        print("Encoded:", enc)
        print("Decoded:", swap_middle(enc))
    elif mode == '5':
        enc = swap_middle_rev(user_text)
        print("Encoded:", enc)
        print("Decoded:", swap_middle_rev_decode(enc))
    elif mode == '6':
        n = 6
        E_key = [4, 5, 1, 3, 2, 0]
        enc = general_swap(user_text, n, E_key)
        print("Encoded Block:", enc)
        D_key = [0] * n
        for kk in range(n):
            D_key[kk] = E_key.index(kk)
        print("Decoded Block:", general_swap(enc, n, D_key))
    else:
        print("Invalid choice.")
    print("\nReturning to Main Menu...")


def run_card_war_game():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']