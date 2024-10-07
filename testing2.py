import os
from member import Member
from groq import Groq

members = []

num = input("Let's create some accounts! Type 1 to continue, 0 to exit: ")
while num == "1":
    name = input("What is your name: ")
    age = input("How old are you: ")
    gender = input("What is your gender: ")


    stress = int(input("Thank you for the information! We would like to know how your week have been"
                   "\nRate level of stress on a scale from 1 to 10: "))
    frustrated = int(input("How many times did you feel frustrated this week? "))
    sad = int(input("How many times did you feel sad this week? "))
    if frustrated > 10:
        frustrated = 10
    if sad > 10:
        sad = 10
    score = int(100 - stress * 2 - frustrated * 1.1 - sad * 1.35)

    improve = input("What is one aspect of your life that you want to improve on? ")

    members.append(Member(name, age, gender, score))

    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": "Please give me a better idea of how to plan my week to increase my work life balance. "
                           "My stress levels this week were a " + str(stress) + " out of 10. I felt frustrated " + str(frustrated)
                           + " times. I also felt sad " + str(sad) + " times. Here is one aspect of my life that I would "
                           "like to improve on. " + improve + ". please give me a general plan and some activities I "
                                                              "could do this week."
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")


    num = input("\n\n\nAdd another account? Type 1 to continue, 0 to exit: ")

print("Here are the results!")
for i in members:
    print(i)
