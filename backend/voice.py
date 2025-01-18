# import gradio as gr
# import groq
# import os
# import io
# import numpy as np
# import soundfile as sf
# from dotenv import load_dotenv

# load_dotenv()

# # Get the GROQ_API_KEY from environment variables
# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     raise ValueError("Please set the GROQ_API_KEY environment variable.")

# # Initialize the Groq client
# client = groq.Client(api_key=api_key)

# def transcribe_audio(audio):
#     if audio is None:
#         return "No audio provided.", ""
    
#     # Gradio provides audio as a tuple: (sampling_rate, numpy_array)
#     sr, y = audio

#     # Convert to mono if stereo
#     if y.ndim > 1:
#         y = y.mean(axis=1)

#     # Normalize audio
#     y = y.astype(np.float32)
#     y /= np.max(np.abs(y)) + 1e-8  # Avoid division by zero

#     # Write audio to buffer
#     buffer = io.BytesIO()
#     sf.write(buffer, y, sr, format='wav')
#     buffer.seek(0)

#     try:
#         # Use Distil-Whisper English model for transcription
#         completion = client.audio.transcriptions.create(
#             model="distil-whisper-large-v3-en",
#             file=("audio.wav", buffer),
#             response_format="text"
#         )
#         transcription = completion
#     except Exception as e:
#         transcription = f"Error in transcription: {str(e)}"

#     response = generate_response(transcription)
#     return transcription, response

# def generate_response(transcription):

#     if not transcription or transcription.startswith("Error"):
#         return "No valid transcription available. Please try speaking again."

#     try:
#         # Use Llama 3.1 70B model for text generation
#         completion = client.chat.completions.create(
#             model="llama-3.1-70b-versatile",
#             messages=[
#                 {"role": "system", "content": "You are a helpful medical assistant that can help diagnose an issue the user describes. You will have a back and forth conversation with the use asking one question at a time, in a natural tone. you do not have to summarize everything the use tells you but do mention th eimportant things. Then ask your next question but ask it in a new line. Ask consise questions, do not repeat yourself, only ask the important questions. Once you have gathered information to form a diagnosis, you will provide the user with a diagnosis. If a user asks you to verify a possible diagnosis, verify it and end your diagnosis with by describing why it is possible that the user is rigth or wrong."},
#                 {"role": "user", "content": transcription}
#             ],
#         )
#         return completion.choices[0].message.content
#     except Exception as e:
#         return f"Error in response generation: {str(e)}"

# def respond(message, chat_history):
#     if chat_history is None:
#         chat_history = []

#     # Prepare the message history for the API
#     messages = [
#         {
#             'role': 'system',
#             'content': 'You are a helpful medical assistant that can help diagnose an issue the user describes. You will have a back and forth conversation with the use asking one question at a time, in a natural tone. you do not have to summarize everything the use tells you but do mention th eimportant things. Then ask your next question but ask it in a new line. Ask consise questions, do not repeat yourself, only ask the important questions. Once you have gathered information to form a diagnosis, you will provide the user with a diagnosis. If a user asks you to verify a possible diagnosis, verify it and end your diagnosis with by describing why it is possible that the user is rigth or wrong.'
#         }
#     ]

#     messages.extend({"role": "user", "content": content} for _, content in chat_history)
#     messages.append({"role": "user", "content": message})

#     try:
#         # Use Llama 3.1 70B model for generating assistant response
#         completion = client.chat.completions.create(
#             model="llama-3.1-70b-versatile",
#             messages=messages,
#         )
#         assistant_message = completion.choices[0].message.content
#         chat_history.append((message, assistant_message))
#     except Exception as e:
#         assistant_message = f"Error: {str(e)}"
#         chat_history.append((message, assistant_message))

#     return "", chat_history, chat_history  # Return state as the third output

# # Custom CSS for the Groq badge and color scheme
# custom_css = """
# .gradio-container {
#     background-color: #f5f5f5;
# }
# .gr-button-primary {
#     background-color: #f55036 !important;
#     border-color: #f55036 !important;
# }
# #groq-badge {
#     position: fixed;
#     bottom: 20px;
#     right: 20px;
#     z-index: 1000;
# }
# """

# with gr.Blocks(css=custom_css) as demo:
#     gr.Markdown("# 🎙️ Groq x Gradio Multi-Modal Assistant")

#     with gr.Tab("Audio"):
#         gr.Markdown("## Speak to the AI")
#         with gr.Row():
#             audio_input = gr.Audio(type="numpy", label="Speak or Upload Audio")
#         with gr.Row():
#             transcription_output = gr.Textbox(label="Transcription")
#             response_output = gr.Textbox(label="AI Assistant Response")
#         process_button = gr.Button("Process", variant="primary")
#         process_button.click(
#             transcribe_audio,
#             inputs=audio_input,
#             outputs=[transcription_output, response_output]
#         )

#     with gr.Tab("Chat"):
#         gr.Markdown("## Chat with the AI Assistant")
#         chatbot = gr.Chatbot()
#         state = gr.State([])  # Initialize the chat state
#         with gr.Row():
#             user_input = gr.Textbox(show_label=False, placeholder="Type your message here...", container=False)
#             send_button = gr.Button("Send", variant="primary")
#         send_button.click(
#             respond,
#             inputs=[user_input, state],
#             outputs=[user_input, chatbot, state],
#         )

#     # Add the Groq badge
#     gr.HTML("""
#     <div id="groq-badge">
#         <div style="color: #f55036; font-weight: bold;">POWERED BY GROQ</div>
#     </div>
#     """)

#     gr.Markdown("""
#     ## How to use this app:

#     ### Audio Tab
#     1. Speak into the microphone or upload an audio file.
#     2. Click the "Process" button to transcribe your speech and generate an AI response.

#     ### Chat Tab
#     1. Type your message into the text box.
#     2. Click the "Send" button to interact with the AI assistant.
#     """)

# demo.launch()
