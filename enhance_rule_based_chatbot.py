import datetime
import random
import re


def get_weather(query):
  cities = {
      "london": "12°C, Rainy and windy",
      "new york": "18°C, Partly cloudy",
      "tokyo": "22°C, Clear skies",
      "paris": "15°C, Light drizzle",
  }

  for city in cities:
    if city in query.lower():
      return f"The current simulated weather in {city.title()} is {cities[city]}."

  return "I can check the weather for London, New York, Tokyo, or Paris. Which city would you like?"


def get_news():
  headlines = [
      "Tech Giants Announce Breakthrough in Quantum Computing Efficiency.",
      "Global Renewable Energy Adoption Reaches a Historic New Milestone.",
      "Researchers Discover New Deep-Sea Species off the Coast of New Zealand.",
      "International Space Station Prepares for Upcoming Crew Rotation.",
  ]
  return "Here is today's top news headline:\n- " + random.choice(headlines) + "\n(Type 'news' again for another update!)"


def get_local_time(query):
  now = datetime.datetime.now()
  return f"According to your local system clock, it is currently {now.strftime('%H:%M:%S on %A, %B %d, %Y')}."


def match_intent(user_input):
  text = user_input.lower().strip()

  if re.search(r"\b(hi|hello|hey|greetings|howdy)\b", text):
    return "greeting"
  elif re.search(r"\b(weather|forecast|temperature|rain|sun)\b", text):
    return "weather"
  elif re.search(r"\b(news|headlines|updates|latest)\b", text):
    return "news"
  elif re.search(r"\b(time|clock|hour|date)\b", text):
    return "time"
  elif re.search(r"\b(help|assist|support|options)\b", text):
    return "help"
  elif re.search(r"\b(bye|exit|quit|goodbye)\b", text):
    return "exit"
  elif re.search(r"\b(history|memory|previous)\b", text):
    return "history"
  else:
    return "unknown"


def display_help():
  return (
      "Here are things you can ask me:\n"
      "  • Greetings: Say 'Hello' or 'Hi'\n"
      "  • Weather: Ask about weather (e.g., 'What's the weather in Tokyo?')\n"
      "  • News: Ask for 'news updates'\n"
      "  • Time: Ask for 'local time'\n"
      "  • Memory: Ask to see 'history' of your previous inputs\n"
      "  • Exit: Type 'bye' or 'exit' to quit"
  )


def chatbot():
  conversation_history = []

  print("🤖 Enhanced Rule-Based Chatbot Initialized!")
  print("Type 'help' to see what I can do, or 'exit' to end the chat.\n")

  while True:
    try:
      user_input = input("You: ")
    except (KeyboardInterrupt, EOFError):
      print("\nChatbot: Goodbye! Thanks for chatting.\n")
      break

    if not user_input.strip():
      print("Chatbot: Please enter a valid message or command.")
      continue

    conversation_history.append(user_input)
    intent = match_intent(user_input)

    if intent == "greeting":
      response = "Hello there! I'm your enhanced assistant. How can I help you today?"
      print("Chatbot: " + response)

    elif intent == "weather":
      response = get_weather(user_input)
      print("Chatbot: " + response)

    elif intent == "news":
      response = get_news()
      print("Chatbot: " + response)

    elif intent == "time":
      response = get_local_time(user_input)
      print("Chatbot: " + response)

    elif intent == "help":
      response = display_help()
      print("Chatbot:\n" + response)

    elif intent == "history":
      if len(conversation_history) <= 1:
        response = "You haven't entered any previous messages yet (aside from this request)."
      else:
        past_inputs = ", ".join([f"'{msg}'" for msg in conversation_history[:-1]])
        response = f"Here are your previous inputs in this session: {past_inputs}"
      print("Chatbot [Memory]: " + response)

    elif intent == "exit":
      print("Chatbot: Goodbye! Have a wonderful day!")
      break

    else:
      response = "I'm not quite sure how to respond to that. Type 'help' to see available topics or try rephrasing!"
      print("Chatbot: " + response)


if __name__ == "__main__":
  chatbot()