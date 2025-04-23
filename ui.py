
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        #score

        self.label = Label(text="score:0",fg="white",highlightthickness=0,bg=THEME_COLOR,font=("Arial",20,"bold"))
        self.label.grid(column=1,row=0)
        #canvas
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,120,
                                                     width=280,
                                                     text="question",
                                                     font=("Arial",20,"italic")
                                                     )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        #button right
        self.true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_img,highlightthickness=0,command=self.right_answer,bd=0)
        self.true_button.grid(column=0,row=2)
        #button wrong
        self.false_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0,command=self.wrong_answer,bd=0)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
       self.canvas.config(bg="white")
       if self.quiz.still_has_questions():
           self.label.config(text=f"Score: {self.quiz.score}")
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
       else:
           self.canvas.itemconfig(self.question_text, text="you've reached the end of level")
           self.true_button.config(state="disabled")
           self.false_button.config(state="disabled")
    def right_answer(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")


        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)










