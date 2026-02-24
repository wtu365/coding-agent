from together import Together
client = Together()

messages_history = []

while True:
    user_input = input("Enter your prompt to the LLM (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    messages_history.append({"role": "user", "content": user_input})
    print(f"You have entered: {user_input}")

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct-Turbo",
        messages=messages_history
    )

    print(f"LLM Response: {response.choices[0].message.content}")
    messages_history.append({"role": "agent", "content": response.choices[0].message.content})