score = 0
question_no = 0
question_no += 1
ques = input(f"{question_no}.Who is the first person to define speed ? ").lower()
if ques == 'galileo':
    score=score+1
    print(f"correct! you got,{score} point")
        
else:
    print('Incorrect!')
    print(f"correct answer is --> galileo")
question_no += 1
ques = input(f"{question_no}. The filament of an electric bulb is made of___? ").lower()
if ques == 'tungsten':
    score=score+1
    print(f"correct! you got,{score} point")
        
else:
    print('Incorrect!')
    print(f'correct answer is --> tungsten')
question_no += 1
ques = input(f"{question_no}. Who is known as the Father of Nuclear Physics? ").lower()
if ques == 'ernest rutherford':
    score=score+1
    print(f"correct! you got,{score} point")
        
else:
    print('Incorrect!')
    print(f'correct answer is --> ernest rutherford')
