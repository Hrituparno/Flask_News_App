from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='0acf7dede0a040b5ba19b4998c38ce41')

@app.route('/', methods=['GET', 'POST'])
def home():
    cat = request.args.get('category', 'general')
    page = int(request.args.get('page', 1))
    is_ajax = request.args.get('ajax') == '1'

    try:
        if request.method == 'POST':
            kw = request.form['keyword']
            res = newsapi.get_everything(q=kw, language='en', page_size=20, page=page)
            arts = res['articles']
            heading = f"Results for “{kw}”"
            title = heading
        else:
            res = newsapi.get_top_headlines(category=cat, language='en', country='us', page_size=20, page=page)
            arts = res['articles']
            heading = cat.capitalize()
            title = heading

    except Exception as e:
        # Fallback for Vercel/Cloud IPs (NewsAPI Free Tier blocks cloud IPs)
        print(f"API Error (using mock data): {e}")
        arts = [
            {
                "source": {"name": "TechCrunch"},
                "author": "Tech Editor",
                "title": "The Future of AI: Generative Models Take Center Stage",
                "description": "Artificial Intelligence is evolving rapidly. New generative models are transforming industries from creative arts to software engineering, marking a new era of automation.",
                "url": "https://techcrunch.com/category/artificial-intelligence/",
                "urlToImage": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=1600",
                "publishedAt": "2026-02-08T10:30:00Z",
                "content": "Full analysis of the AI revolution..."
            },
            {
                "source": {"name": "The Verge"},
                "author": "Nilay Patel",
                "title": "Global Markets Rally as Tech Sector Rebounds",
                "description": "After a volatile quarter, major tech stocks are showing signs of strong recovery, driven by breakthroughs in semiconductor efficiency and cloud computing.",
                "url": "https://www.theverge.com/tech",
                "urlToImage": "https://images.unsplash.com/photo-1611974765270-ca1258634369?auto=format&fit=crop&q=80&w=1600",
                "publishedAt": "2026-02-08T09:15:00Z",
                "content": "Market analysis..."
            },
            {
                "source": {"name": "Wired"},
                "author": "Gadget Lab",
                "title": "Sustainable Energy: The Shift to Fusion Power",
                "description": "Scientists achieve net energy gain in nuclear fusion, paving the way for limitless clean energy. Here is what this means for the next decade of power generation.",
                "url": "https://www.wired.com/category/science/",
                "urlToImage": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&q=80&w=1600",
                "publishedAt": "2026-02-08T08:00:00Z",
                "content": "Energy breakthrough..."
            },
             {
                "source": {"name": "BBC News"},
                "author": "Science Team",
                "title": "SpaceX Starship Successfully Reaches Orbit",
                "description": "The massive rocket has completed its first full orbital test flight, opening new possibilities for interplanetary travel and heavy payload delivery.",
                "url": "https://www.bbc.com/news/science_and_environment",
                "urlToImage": "https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&q=80&w=1600",
                "publishedAt": "2026-02-08T07:45:00Z",
                "content": "Space exploration update..."
            }
        ]
        heading = f"Top Stories (Demo Mode)" if request.method == 'GET' else f"Results (Demo Mode)"
        title = heading

    if is_ajax: return {"articles": arts, "heading": heading}
    
    return render_template('home.html',
                           title=title,
                           heading=heading,
                           articles=arts,
                           current_category=cat if request.method == 'GET' else None)
@app.route('/bookmarks')
def bookmarks():
    return render_template('home.html',
                           title="Bookmarked Stories",
                           heading="Your Saved Stories",
                           articles=[],
                           current_category=None)



@app.route('/summarize', methods=['POST'])
def summarize():
    import time
    data = request.get_json() or request.form
    title = data.get('title', 'Unknown News')
    
    # Mock AI logic - in production, this would call OpenAI/Gemini
    time.sleep(0.5) # Fast simulation
    
    mock_summaries = [
        f"Key insights from '{title}': The article explores the major shift in industry trends prompted by recent global events. Expert analysis suggests a sustained period of innovation and rapid adaptation within the sector.",
        f"Summary of today's report on '{title}': Stakeholders are closely monitoring new regulatory changes that could redefine market competition. The narrative highlights both the risks of non-compliance and the opportunities for early adopters.",
        f"Quick recap for '{title}': Technology continues to be a disruptive force, as detailed in this latest update. The core takeaway focuses on the intersection of human creativity and automated efficiency as a path forward."
    ]
    import random
    summary = random.choice(mock_summaries)
    
    return {"summary": summary}

if __name__ == '__main__':
    app.run(debug=True)
