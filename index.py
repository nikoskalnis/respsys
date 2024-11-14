def AI():
  print("Hello, how can I assist you?")
  while True:
    user_input = input("You: ").lower()
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
      print("Hi, how's it going?")
    elif "quit" in user_input:
      print("Goodbye!")
      break
AI()
