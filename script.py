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
