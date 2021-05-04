## Welcome to Python Learning!

In this repo you'll find the final projcet of my Learn Python in 30 Days online course. The final project is a Python Learning App, read through how it works below. Don't hesitate to reach out with any questions!

## Final Project - Python Learning App

The app's purpose is to quiz que user with Python questions, determine if the user gets them right or wrong and finally calcualte and save the final score.
Here's how the app should work.

1. When running `main.py`, the script reads through the `topics.json`, `questions.json`, and `past_scores.json` files and prints the welcome page below to the user: 

![image](https://user-images.githubusercontent.com/65046112/112773545-698c3f80-9004-11eb-972a-98ec8ba570bc.png)

2. The user then inputs a number referencing the topic to get quizzed. Let's say the user inputs "2", this would take take them to the quiz on Lists and start prompting the questions on that topic.

![image](https://user-images.githubusercontent.com/65046112/112773583-8de81c00-9004-11eb-9a9a-ccc62d0e2295.png)

Whenever the user enters an invalid input, they are prompted over and over until they enter a valid question or enter "q" to quit.

![image](https://user-images.githubusercontent.com/65046112/112773633-a9532700-9004-11eb-9acf-21997c4ff276.png)

When they get the right answer, the program prints a message to the user saying they got it right.

![image](https://user-images.githubusercontent.com/65046112/112773641-b5d77f80-9004-11eb-854b-b32831b622d7.png)

Whenever the user enters the wrong answer, the app lets them know as well.

![image](https://user-images.githubusercontent.com/65046112/112773917-e966d980-9005-11eb-8f16-478908393e96.png)

3. Once the user finishes answering all questions on that topic (which is maxed out to 10 questions per run), the app prints the final score for that run and saves the score into `past_scores.json`.

![image](https://user-images.githubusercontent.com/65046112/112773659-c982e600-9004-11eb-9fa1-f13658b4ae31.png)
