from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>Welcome to the news website!</p>
    <a href="/reporters">List of Reporters</a>
    '''

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    
    reporters = {
        1: "John Doe",
        2: "Jane Smith",
        3: "Alice Johnson"
    }
    
    return f'''
    <h2>Reporter {reporter_id} - {reporters.get(reporter_id, "Unknown Reporter")}</h2>
    <a href="/">Return to home page</a><br>
    <a href="/reporter/{reporter_id}/articles">View articles by this reporter</a>
    '''

@app.route('/article/<article_name>')
def article(article_name):
    return f'''
    <h2>{article_name.replace('-', ' ').title()}</h2>
    <a href="/">Return back to home page</a>
    '''

@app.route('/reporters')
def reporters():
    reporters_list = {
        1: "John Doe",
        2: "Jane Smith",
        3: "Alice Johnson"
    }
    reporter_links = ''.join([f'<li><a href="/reporter/{id}">{name}</a></li>' for id, name in reporters_list.items()])
    
    return f'''
    <h2>List of Reporters</h2>
    <ul>
        {reporter_links}
    </ul>
    <a href="/">Return to home page</a>
    '''

@app.route('/reporter/<int:reporter_id>/articles')
def reporter_articles(reporter_id):
  
    articles = {
        1: ["breaking-news", "latest-updates"],
        2: ["tech-innovations", "ai-trends"],
        3: ["health-tips", "nutrition-facts"]
    }
    
    article_links = ''.join([f'<li><a href="/article/{name}">{name.replace("-", " ").title()}</a></li>' for name in articles.get(reporter_id, [])])
    
    return f'''
    <h2>Articles by Reporter {reporter_id}</h2>
    <ul>
        {article_links}
    </ul>
    <a href="/">Return to home page</a>
    '''
