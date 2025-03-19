print("Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!")

question1 = "Кто придумал эчпочмак?"
question2 = "Луковый суп — это блюдо какой кухни?"
question3 = "Где родина начос?"
question4 = "Как называются китайские пельмени?"
question5 = "В национальную кухню какой страны входят драники?"

true_answer1 = "татары"
true_answer2 = "Франция"
true_answer3 = "Мексика"
true_answer4 = "гёдза"
true_answer5 = "Беларусь"

answer1 = input(question1)
answer2 = input(question2)
answer3 = input(question3)
answer4 = input(question4)
answer5 = input(question5)

Score = 0

if answer1 == "татары":
    Score += 1
if answer2 == "Франция":
    Score += 1
if answer3 == "Мексика":
    Score += 1
if answer4 == "гёдза":
    Score += 1
if answer5 == "Беларусь":
    Score += 1
print("вы набрали",Score,"очков")

if Score >= 3:
     print("Ты умный молодец")
else:
    print("Вы бурати то есть вы тоже бревно тупое")

