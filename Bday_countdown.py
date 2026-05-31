#INCLUDED 3 BONUS : HOW TO TELL AGE, TRY AND ACCEPT, DECLINING FUTURE DATES
#1 NEW FUNCTION USED: 1. name: divmod
#                     2. uses: returns both quotient and remainder. 

import datetime as dt
import time


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
print('But I can tell you ... it was a ...', end = ' ')
print(weekday_names[weekday_num])
#AQUAIRIOUS/CAPRICON
if month == 1:
     print('You are a very lucky person!!!')
     print('This is your horroscope for today!')
     print('Your zodiac is .......  AQUAIRIOUS/CAPRICON!??')
     print()
     print()
     print('Aquarius is the visionary humanitarian and original thinker of the zodiac.\n' 
     ' They look toward the future, valuing innovation, intellectual freedom, and the collective progress of society over tradition.\n' 
     'Core Trait: Independent innovation.\n'
     'Superpower: Visionary thinking.\n' 
     'Weakness: Emotional detachment.\n')
     print()
     print()
     print('Capricorn represents ambition, discipline, and long-term vision.\n' 
     ' They possess the patience to climb the highest mountains, building legacy, structure, and order through sheer grit and responsibility.\n' 
     'Core Trait: Strategic ambition.\n' 
     'Superpower: Relentless discipline.\n' 
     'Weakness: Rigidness.\n')


#Piesces/Aquairious
if month == 2:
     print('You are a very lucky person!!!')
     print('This is your horroscope for today!')
     print('Your zodiac is .......  PISCES/AQUAIRIOUS!??')
     print()
     print()
     print('Pisces is the dreamer, mystic, and artist.\n' 
    ' Boundless empathy allows them to absorb emotions and connect deeply with the spiritual realm.\n' 
    ' They express their rich inner world through art and compassion.\n' 
    'Core Trait: Boundless imagination.\n' 
    'Superpower: Creative empathy.\n' 
    'Weakness: Escapism.\n')
     print()
     print()
     print('Aquarius is the visionary humanitarian and original thinker of the zodiac.\n' 
     ' They look toward the future, valuing innovation, intellectual freedom, and the collective progress of society over tradition.\n' 
     'Core Trait: Independent innovation.\n'
     'Superpower: Visionary thinking.\n' 
     'Weakness: Emotional detachment.\n')
        

#Trying out new and weeird bonus ideas!!!!
if month == 3:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  AIRIES/PISCES!??')
    print()
    print()
    print('Aries is the trailblazer of the zodiac.\n ' 
    'Driven by intense passion and high energy, they approach life with a fearless, competitive spirit.\n' 
    ' They excel at starting new projects and thrive on challenges.\n' 
    'Core Trait: Bold initiative.\n' 
    'Superpower: Unshakeable courage.\n' 
    'Weakness: Impatience.\n')
    print()
    print()
    print('Pisces is the dreamer, mystic, and artist.\n' 
    ' Boundless empathy allows them to absorb emotions and connect deeply with the spiritual realm.\n' 
    ' They express their rich inner world through art and compassion.\n' 
    'Core Trait: Boundless imagination.\n' 
    'Superpower: Creative empathy.\n' 
    'Weakness: Escapism.\n')
        
    
#TAURUS/AIRIES
if month == 4:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  TAURUS/AIRIES!??')
    print()
    print()
    print('Taurus represents stability, patience, and grounded strength.\n' 
    ' They value comfort, consistency, and the finer things in life.\n' 
    ' Known for their incredible work ethic, they build lasting foundations.\n' 
    'Core Trait: Steady reliability.\n' 
    'Superpower: Practical determination.Weakness: Stubbornness.\n')
    print()
    print()
    print('Aries is the trailblazer of the zodiac.\n ' 
    'Driven by intense passion and high energy, they approach life with a fearless, competitive spirit.\n' 
    ' They excel at starting new projects and thrive on challenges.\n' 
    'Core Trait: Bold initiative.\n' 
    'Superpower: Unshakeable courage.\n' 
    'Weakness: Impatience.\n')
    
#GEMINI/TAURUS
if month == 5 :
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  GEMINI/TAURUS!!??')
    print()
    print()
    print('Taurus represents stability, patience, and grounded strength.\n' 
    ' They value comfort, consistency, and the finer things in life.\n' 
    ' Known for their incredible work ethic, they build lasting foundations.\n' 
    'Core Trait: Steady reliability.\n' 
    'Superpower: Practical determination.Weakness: Stubbornness.\n')
    print()
    print()
    print('Gemini is the intellectual butterfly of the cosmos.\n ' 
    'Driven by constant curiosity, they are master communicators who process information rapidly.\n' 
    ' They love learning, sharing ideas, and adapting to change.\n' 
    'Core Trait: Mental agility.\n' 
    'Superpower: Versatility.\n' 
    'Weakness: Scattered focus.\n')

    
  

#CANCER/GEMINI
if month == 6:


    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  CANCER/LEO!!??')
    print()
    print()
    print('Cancer is the nurturing protector, deeply attuned to emotional undertones.\n' 
    ' They possess profound intuition and prioritize creating safe, loving spaces for family and friends.\n' 
    ' Their empathy is unmatched.\n' 
    'Core Trait: Deep emotional depth.\n' 
    'Superpower: Natural intuition.\n' 
    'Weakness: Moodiness.')
    print()
    print()
    

    print('Gemini is the intellectual butterfly of the cosmos.\n ' 
    'Driven by constant curiosity, they are master communicators who process information rapidly.\n' 
    ' They love learning, sharing ideas, and adapting to change.\n' 
    'Core Trait: Mental agility.\n' 
    'Superpower: Versatility.\n' 
    'Weakness: Scattered focus.\n')

#LEO/CANCER
if month == 7:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  CANCER/LEO!!??')
    print()
    print()
    print('Cancer is the nurturing protector, deeply attuned to emotional undertones.\n' 
    ' They possess profound intuition and prioritize creating safe, loving spaces for family and friends.\n' 
    ' Their empathy is unmatched.\n' 
    'Core Trait: Deep emotional depth.\n' 
    'Superpower: Natural intuition.\n' 
    'Weakness: Moodiness.')
    print()
    print()
    print('Leo radiates warmth, creativity, and magnetic charisma.\n' 
    ' Natural-born leaders, they love to celebrate life and inspire others.\n' 
    ' They are fiercely loyal friends with generous, golden hearts.\n' 
    'Core Trait: Radiant confidence.\n' 
    'Superpower: Creative leadership.\n' 
    'Weakness: Pride.\n')

#VIRGO/LEO
if month == 8:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is ....... Leo / Virgo !!??')
    print()
    print()
    print('Virgo brings order, clarity, and precision to the world. They possess analytical minds and a deep desire to be of service.\n' 
    ' They excel at problem-solving and notice details others miss.\n' 
    'Core Trait: Meticulous analysis.\n' 
    'Superpower: Practical efficiency.\n' 
    'Weakness: Perfectionism.\n')
    print()
    print()
    print('Leo radiates warmth, creativity, and magnetic charisma.\n' 
    ' Natural-born leaders, they love to celebrate life and inspire others.\n' 
    ' They are fiercely loyal friends with generous, golden hearts.\n' 
    'Core Trait: Radiant confidence.\n' 
    'Superpower: Creative leadership.\n' 
    'Weakness: Pride.\n')

#VIRGO/LIBRA
if month == 9:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  VIRGO/LIBRA!!??')
    print()
    print()
    print('Virgo brings order, clarity, and precision to the world. They possess analytical minds and a deep desire to be of service.\n' 
    ' They excel at problem-solving and notice details others miss.\n' 
    'Core Trait: Meticulous analysis.\n' 
    'Superpower: Practical efficiency.\n' 
    'Weakness: Perfectionism.\n')
    print()
    print()
    print('Libra seeks harmony, balance, and beauty in all things.\n' 
    ' Natural diplomats, they excel at seeing multiple perspectives and bringing people together.\n'
    '. They value justice, art, and thriving relationships.\n'
    'Core Trait: Diplomatic grace.\n' 
    'Superpower: Creating harmony.\n' 
    'Weakness: Indecisiveness.\n')

#LIBRA/SCORPIO    
if month == 10:
    print('You are a very luckyperson!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  LIBRA/SCORPIO!!??')
    print()
    print()
    print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n' 
    ' They possess magnetic focus and can see right through deception.\n' 
    ' They undergo powerful personal transformations throughout life.\n' 
    'Core Trait: Strategic intensity.\n' 
    'Superpower: Psychological insight.\n' 
    'Weakness: Secretiveness.\n')


#Scorpio/Sagittarius
if month == 11:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  SCORPIO\SAGITTARIUS!!??')
    print()
    print()
    print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n' 
    ' They possess magnetic focus and can see right through deception.\n' 
    ' They undergo powerful personal transformations throughout life.\n' 
    'Core Trait: Strategic intensity.\n' 
    'Superpower: Psychological insight.\n' 
    'Weakness: Secretiveness.\n')
    print()
    print()
    print('Sagittarius is the eternal optimist and philosophical adventurer.\n' 
    ' Driven by a thirst for freedom and truth, they love exploring new cultures, ideas, and horizons with infectious enthusiasm.\n' 
    'Core Trait: Philosophical exploration.\n' 
    'Superpower: Limitless optimism.\n' 
    'Weakness: Bluntness.\n')


if month == 12:
    print('You are a very lucky person!!!')
    print('This is your horroscope for today!')
    print('Your zodiac is .......  SCORPIO\SAGITTARIUS!!??')
    print()
    print()
    print('Scorpio is a powerhouse of intensity, passion, and psychological depth.\n' 
    ' They possess magnetic focus and can see right through deception.\n' 
    ' They undergo powerful personal transformations throughout life.\n' 
    'Core Trait: Strategic intensity.\n' 
    'Superpower: Psychological insight.\n' 
    'Weakness: Secretiveness.\n')
    print()
    print()
    print('Capricorn represents ambition, discipline, and long-term vision.\n' 
     ' They possess the patience to climb the highest mountains, building legacy, structure, and order through sheer grit and responsibility.\n' 
     'Core Trait: Strategic ambition.\n' 
     'Superpower: Relentless discipline.\n' 
     'Weakness: Rigidness.\n')

current_time = dt.datetime.now()
thisyear = current_time.year
thisyear_bday = dt.datetime(thisyear, month, day)
#Calculating users current age!!
current_time = dt.datetime.now()
Diff = current_time - date_birth
view_diff = Diff.days//365
print('Your age is currently:', view_diff)









if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    next_bday = dt.datetime(thisyear+1, month, day)
    test_year = date_birth.year + 1
    bday_list = [0, 0, 0, 0, 0 ,0 ,0]
    while test_year < next_bday.year:
        test_date = dt.datetime(test_year , month, day)
        weekday_num = test_date.weekday()
        bday_list[weekday_num] = bday_list[weekday_num] +1
        test_year = test_year + 1
    print()
    for kk in range(7):
        print('Your birthday was on a', weekday_names[kk], bday_list, 'times.')

    print()    







    
print('Your next birthday will be on ...', end = ' ')
print(next_bday)
print()
print('That will be a ...', end = ' ')
weekday_num = next_bday.weekday()
print(weekday_names[weekday_num])

print()
print()


print("Press Enter to start the countdown live ticker...")
input()

while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    
    total_mins_left, seconds_left  = divmod(total_seconds_left, 60)
    hrs_left, minutes_left  = divmod(total_mins_left, 60)

    #Trying out new stuff and making the code more cleaner and compatible
    print(f'Your next birthday is {days_left} days, {hrs_left} hrs, {minutes_left} mins, {seconds_left} secs away.', end = '\r')

    time.sleep(1)
 

