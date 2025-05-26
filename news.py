import requests
from newspaper import Article
from transformers import pipeline

# ---------- Configuration ----------
API_KEY = 'your_newsapi_key_here'  # Replace with your NewsAPI.org key
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# ---------- Load Summarization Model ----------
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ---------- Function to fetch news ----------
def get_top_articles():
    response = requests.get(https://indianexpress.com/article/technology/opinion-technology/sam-altman-jony-ive-new-ai-hardware-matching-iphone-success-not-easy-10027361/?ref=newlist_hp )
    data = response.json()
    return data.get("articles", [])

# ---------- Function to extract article text ----------
def extract_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# ---------- Function to summarize article ----------
def summarize(text, max_len=130, min_len=30):
    try:
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
    except:
        return "Summary generation failed."

# ---------- Main Function ----------
def main():
    articles = get_top_articles()
    for i, article in enumerate(articles[:3]):  # Get top 3 for demo
        print(f"\n📰 News {i+1}")
        print("Title:", article['title'])
        print("URL:", article['url'])

        try:
            text = extract_article_text(article['url'])
            summary = summarize(text)
            print("📝 Summary:", summary)
        except Exception as e:
            print("⚠️ Error processing this article:", e)

# ---------- Run ----------
if __name__ == "__main__":
    main()
