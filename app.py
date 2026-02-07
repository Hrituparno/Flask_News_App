from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='0acf7dede0a040b5ba19b4998c38ce41')

@app.route('/', methods=['GET', 'POST'])
def home():
    cat = request.args.get('category', 'general')
    page = int(request.args.get('page', 1))
    is_ajax = request.args.get('ajax') == '1'

    if request.method == 'POST':
        kw = request.form['keyword']
        res = newsapi.get_everything(q=kw, language='en', page_size=20, page=page)
        arts = res['articles']
        if is_ajax: return {"articles": arts, "heading": f"Search: {kw}"}
        return render_template('home.html',
                               title=f"Results for “{kw}”",
                               heading=f"Search: {kw}",
                               articles=arts,
                               current_category=None)
    else:
        res = newsapi.get_top_headlines(category=cat, language='en', country='us', page_size=20, page=page)
        arts = res['articles']
        if is_ajax: return {"articles": arts, "heading": cat.capitalize()}
        return render_template('home.html',
                               title=cat.capitalize(),
                               heading=cat.capitalize(),
                               articles=arts,
                               current_category=cat)
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
