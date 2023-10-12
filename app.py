from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

# from module flask import capital Flask
# listening for GET requests only so far
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

#^^ helps w debugging and viewing info in ssn will talk later
#root route
#^^instantiate it with our app..make sure route name is inputed in arg

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p> Welcome to my simple app. </p>
            <a href= '/hello'>Go to Hello page </a>
        </body>
    </html>
    """
    return html

#decorators demand that there is a function right after it
@app.route('/hello')
def say_hello():
    """Return simple "Hello" Greeting."""
    #string will be use to construct a full http response
    return render_template("hello.html")

@app.route('/search')
def search():
    #filled with information parsed from the query string
    # print(request.args)
    term = request.args["term"]
    sort =request.args["sort"]
    return f"<h1>Search Results For: {term} </h1> <p> Sorting by: {sort} </p>"

#post requests are normally through forms, ajax or curl
#curl -X  POST http://....5000
# curl http... a GET request

#adding form GET request, then add post route


#name field is importantto store the data 
@app.route('/add-comment')
def add_comment_form():
    """Shows add comment form"""
    return """
    <h1>Add Comment </h1>
    <form method="POST">
      <input type='text' placeholder='comment' name='comment'/>
      <input type='text' placeholder='username' name='username'/>
      <button>Submit</button>
    </form>
  """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    """Saves comment data (pretends to)"""

    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
      <h1>SAVED YOUR COMMENT</h1>
      <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
      </ul>
    """
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"

#dealing with multtiple variables withing a single route
#called restful routing
#url prams or variable are more like a subject and query params are modifiers or additional info
@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"

#posts by id example fake database
POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}

#keys are integers but we are getting strings
#can specify fancy syntax on flask for ints
#.get to handle the errors if key not found -> only hits it if the ids are integers 'ahfk' wont work
@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id,  "Post not found")
    return f"<p>{post}</p>"
