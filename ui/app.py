import gradio as gr
import openai

message_history = [{"role": "user", "content": f"You are a joke bot. I will specify the subject matter in my messages, and you will reply with a joke that includes the subjects I mention in my messages. Reply only with jokes to further input. If you understand, say OK."},
                   {"role": "assistant", "content": f"OK"}]

ONLINE_MODELS = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0301",
    "gpt-3.5-turbo-0613",
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-0613",
    "gpt-4-32k",
    "gpt-4-32k-0314",
    "gpt-4-32k-0613",
]

def predict(input):
    # tokenize the new input sentence
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-16k", #10x cheaper than davinci, and better. $0.002 per 1k tokens
      messages=message_history
    )
    #Just the reply:
    reply_content = completion.choices[0].message.content#.replace('```python', '<pre>').replace('```', '</pre>')

    print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    
    # get pairs of msg["content"] from message history, skipping the pre-prompt:              here.
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]  # convert to tuples of list
    return response


with gr.Blocks() as demo:
    with gr.Row().style(equal_height=True):
        with gr.Column(scale=5):
            with gr.Row():
                chatbot = gr.Chatbot(label="ProgramEngineerGPT", elem_id="chatbot").style(height=650)
            with gr.Row():
                with gr.Column(min_width=225, scale=12):
                    user_input = gr.Textbox(
                        elem_id="user_input_tb",
                        show_label=False, placeholder="Enter Text",
                    ).style(container=False)
                with gr.Column(min_width=42, scale=1):
                    submitBtn = gr.Button(value="", variant="primary", elem_id="submit_btn")
                    cancelBtn = gr.Button(value="", variant="secondary", visible=False, elem_id="cancel_btn")

        with gr.Column(min_width=50, scale=1):
            with gr.Tab(label="API Settings"):
                keyTxt = gr.Textbox(
                    show_label=True,
                    placeholder="Your API-key...",
                    type="password",
                    label="API-Key",
                )
                model_select_dropdown = gr.Dropdown(
                    label="Select Model", choices=ONLINE_MODELS, multiselect=False, value=ONLINE_MODELS[1], interactive=True
                )
            with gr.Tab(label="Prompt"):
                    systemPromptTxt = gr.Textbox(
                        show_label=True,
                        placeholder="System Prompt Here",
                        label="Current Prompt",
                        lines=10,
                    ).style(container=False)
                    with gr.Accordion(label="System Prompts", open=True):
                        with gr.Column():
                            with gr.Row():
                                with gr.Column(scale=6):
                                    templateFileSelectDropdown = gr.Dropdown(
                                        label="Actions",
                                        choices=["1", "2"],
                                        multiselect=False,
                                        value="1"
                                    ).style(container=False)
                                with gr.Column(scale=1):
                                    templateRefreshBtn = gr.Button="🔄 Refresh"
                            with gr.Row():
                                with gr.Column():
                                    templateSelectDropdown = gr.Dropdown(
                                        label="Load from Prompt template",
                                        multiselect=False,
                                    ).style(container=False)


    user_input.submit(predict, user_input, chatbot) # submit(function, input, output)
    #txt.submit(lambda :"", None, txt)  #Sets submit action to lambda function that returns empty string 


    user_input.submit(None, None, user_input, _js="() => {''}") # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.
         
demo.launch()     
