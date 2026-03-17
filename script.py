from google import genai

client = genai.Client(api_keys="_____")

while True:
  try:
    response = client.models.generate_content(
      model = "____",
      contents = input("\nEnter your prompt: ")
    )
    print(response.text)
  except KeyboardInterrupt:
    print("\n Exiting")


# For streaming change as
try:
    response = client.models.generate_content_stream(
      model = "____",
      contents = input("\nEnter your prompt: ")
    )
    for chunk in response:
      if chunk.text:
        print(chunk.text, end="", flush=True)
  except KeyboardInterrupt:
    print("\n Exiting")
