from flask import Flask, jsonify, request, render_template, url_for
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "static/images/thumbs/smilecat.jpeg"

user_bio = "idk what sounds cats make so imma just write rrrr"

posts = {
    "static/images/thumbs/confusedasfcat.jpg": "when you have 5 labs to do and 15 minutes to submit",
    "static/images/thumbs/joycat.jpeg": "me when instructors typing my code for me",
    "static/images/thumbs/mecat.jpg": "instructors when students ask questions they could've found the answer to in google"}


#####


@app.route('/')  # '/' for the default page
def home():
     return render_template('index.html',
                             image=image_link,
                             bio=user_bio,
                             post_data = posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
