# import os
# from groq import Groq
# import json
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq(
#     api_key=os.getenv('GROQ_API_KEY'),
# )

# MODEL = 'llama-3.3-70b-versatile'

# messages=[
#             {
#                 'role': 'system',
#                 'content': 'You are a helpful medical assistant that can help diagnose an issue the user describes. You will have a back and forth conversation with the use asking one question at a time, in a natural tone. you do not have to summarize everything the use tells you but do mention th eimportant things. Then ask your next question but ask it in a new line. Ask consise questions, do not repeat yourself, only ask the important questions. Once you have gathered information to form a diagnosis, you will provide the user with a diagnosis. If a user asks you to verify a possible diagnosis, verify it and end your diagnosis with by describing why it is possible that the user is rigth or wrong.'
#             }
# ]

# try:
#     while True:
#         user_input = input("User: ")
#         if user_input.lower() in ["quit", "exit"]:
#             break

#         messages.append({
#             'role': 'user',
#             'content': user_input
#         })

#         chat_completion = client.chat.completions.create(
#             model=MODEL,
#             messages=messages,
#         )

#         assistant_response = chat_completion.choices[0].message.content
#         print(f"\nAssistant Doctor: {assistant_response}")

#         messages.append({
#             'role': 'system',
#             'content': assistant_response
#         })

#         if "diagnosis" in assistant_response.lower() or "reccomend" in assistant_response.lower():
#             diagnosis = assistant_response
#             print(f"\n{diagnosis}")
#             break

# except Exception as e:
#     print(f"An error occurred: {e}")


