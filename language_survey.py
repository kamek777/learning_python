from survey import AnonymousSurvey

#Zdefiniowanie pytania i utworzenie ankiety
question = "Jaki jest Twój ojczysty język?"
my_survey = AnonymousSurvey(question)

#Wyświetlenie pytania i przechowywanie odpowiedzi na nie.
my_survey.show_question()
print("Wpisz 'q', aby zakończyć działanie programu.\n")

while True:
    response = input("Język: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
#Wyświetlenie wyników ankiety.
print("\nDziękujemy każdemu respondentowi za udział w ankiecie!")
my_survey.show_results()