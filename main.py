import wikipediaapi
import wikipedia
import gradio as gr

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent="MyWikipediaChatbot/1.0 (https://replit.com; contact: your-email@example.com)",
    language="en"
)

# Function to search Wikipedia
def search_wikipedia(query):
    try:
        # Try to find relevant Wikipedia pages
        search_results = wikipedia.search(query)

        if not search_results:
            return f"❌ No relevant Wikipedia page found for '{query}'. Try a different phrase!"

        # Use the top result as the page title
        page_title = search_results[0]
        page = wiki_wiki.page(page_title)

        if not page.exists():
            return f"❌ Wikipedia page not found for '{query}'. Try another term!"

        return f"**{page.title}**\n\n{page.summary[:500]}...\n\n[Read more on Wikipedia]({page.fullurl})"

    except Exception as e:
        return f"⚠️ An error occurred: {e}"

# Create a Gradio chatbot UI
chatbot = gr.Interface(
    fn=search_wikipedia,
    inputs=gr.Textbox(placeholder="Ask me anything..."),
    outputs="markdown",
    title="Wikipedia Chatbot",
    description="Type any topic, and I'll fetch information from Wikipedia!"
)

# Launch the Gradio interface
if __name__ == "__main__":
    chatbot.launch(share=True)
