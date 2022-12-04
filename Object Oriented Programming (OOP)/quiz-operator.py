# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:         
            self.displayProgress()  
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('Mark zuckerberg hangi sosyal medya uygulamasının sahibidir ?', ['Facebook','Twitter','Instagram','Discord'], 'Facebook')
q2 = Question('En çok kullanılan sosyal medya uygulaması ?', ['Facebook','Twitter','Instagram','Discord'], 'Instagram')
q3 = Question('Dunyanın en zengin adamı kimdir? ?', ['Elon Musk','Bill Gates','Steve Jobs','Jack Ma'], 'Elon Musk')
q4 = Question('Son çıkan Unreal Engine oyun motorunun sürümü nedir ?', ['2','3','4','5'], '5')
q5 = Question('Hangisi memeli hayvandır ?', ['Timsah','Piton','Yarasa','Kurbağa'], 'Yarasa')

questions = [q1,q2,q3,q4,q5]



quiz = Quiz(questions)

quiz.loadQuestion()
