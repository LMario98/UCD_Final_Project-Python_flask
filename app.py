from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks = {
    1: {'title': 'Python Tutorial', 'description': 'Python is a popular programming language.', 'url': 'https://www.w3schools.com/python/default.asp'},
    2: {'title': 'Learning Flask', 'description': 'Read the official documentation', 'url': 'https://flask.palletsprojects.com/'},
}

# Home Page 
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
   
    title = request.form['title']
    description = request.form['description']
    url = request.form.get('url', '')

    
    new_id = max(tasks.keys()) + 1 if tasks else 1

    tasks[new_id] = {'title': title, 'description': description, 'url': url}

    
    return redirect(url_for('home'))



@app.route('/delete/<int:task_id>')
def delete_task(task_id):
   
    if task_id in tasks:
        del tasks[task_id]
    return redirect(url_for('home'))

@app.route('/Projects')
def projects():
    # return "<h1>Projects</h1><p>Here are some of my projects.</p>"
    return render_template('projects.html')


@app.route('/skills')
def skills():
    # return "<h1>Skills</h1><p>These are my skills.</p>"
    return render_template('skills.html')


@app.route('/about')
def about():
    return render_template('about.html')
    # return "<h1>About Me</h1><p>Learn more about me here.</p>"



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



@app.route('/submitted')
def submitted():
    return "<h1>Thank You!</h1><p>Your submission has been received.</p>"

if __name__ == '__main__':
    app.run(debug=True)














