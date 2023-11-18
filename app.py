from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from database.database_executor import DatabaseExecutor

app = Flask(__name__)

# secret key for session
app.secret_key = 'TODO: Set Secret Key'

from flask import request

@app.route('/display-books/<genre>', methods=['GET'])
def display_books(genre):
    db_executor = DatabaseExecutor()

    # Get books by genre
    books = db_executor.get_books_by_genre(genre)

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort the books based on the selected criteria
    if sort_by == 'title':
        books.sort(key=lambda x: x.title)
    elif sort_by == 'price':
        # Change the sorting logic for 'price' to handle numerical values
        books.sort(key=lambda x: float(x.price))

    # Handle descending order
    if order == 'desc':
        books.reverse()

    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]

    return render_template("display-books.html", genre_page=genre, books=books_data, sort_by=sort_by, order=order)

# ...

@app.route('/display-accessories', methods=['GET'])
def display_accessories():
    db_executor = DatabaseExecutor()

    # Get accessories
    accessories = db_executor.get_accessories()

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort the accessories based on the selected criteria
    if sort_by == 'title':
        accessories.sort(key=lambda x: x.item_name)
    elif sort_by == 'price':
        # Change the sorting logic for 'price' to handle numerical values
        accessories.sort(key=lambda x: float(x.price))

    # Handle descending order
    if order == 'desc':
        accessories.reverse()

    accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for accessory in accessories]

    return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data, sort_by=sort_by, order=order)



@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")


@app.route('/non-fiction')
def non_fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Non-Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fiction')
def fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/romance')
def romance():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Romance"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/action')
def action():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Action"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/kids')
def kids():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Kids"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fantasy')
def fantasy():
    # Initialize the DatabaseExecutor
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fantasy"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/horror')
def horror():
    db_executor = DatabaseExecutor()
    
    # Get books by genre
    genre_page = "Horror"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/comic-manga')
def comic_manga():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Comic/Manga"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html",  genre_page=genre_page, books=books_data)


@app.route('/accessories')
def accesories():
    db_executor = DatabaseExecutor()

    # get the accessories
    genre_page = "Accessories"
    accessories = db_executor.get_accessories()
    accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for accessory in accessories]
    return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db_executor = DatabaseExecutor()
    if request.method == 'POST':
        username = request.json.get('login-username')
        password = request.json.get('login-password')
        user = db_executor.authenticate_user(username, password)
        if user:
            session['username'] = username
            print("SUCCESS")
            return jsonify({"status": "success", "username": username})
        else:
            print("FAILED")
            return jsonify({"status": "failure", "error": "Invalid username or password"})

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.pop('username', None)
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")

@app.route('/signup', methods=['POST'])
def signup():
    db_executor = DatabaseExecutor()
    if request.method == 'POST':
        # will automatically set admin to false, since we should never be creating an admin account through the website
        admin = False
        username = request.json.get('signup-username')
        password = request.json.get('signup-password')

        # register the user
        db_executor.register_user(admin, username, password)

        # return empty string to complete valid response (can change later to pop up a success message)
        return ''


@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'

@app.route('/check_login_status')
def check_login_status():
    if 'username' in session:
        return jsonify({"status": "success", "username": session['username']})
    else:
        return jsonify({"status": "failure"})


if __name__ == '__main__':
    app.run(debug=True)
