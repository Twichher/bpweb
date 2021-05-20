from flask import Flask, render_template, request, escape
from methods import search4letters
from time import strftime
app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                            the_title='Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str, time: str) -> None:
    with open('C:\\Users\\vladi\python_prj\webapp\\vsearch.log', 'a') as log:
        print(req.form,req.remote_addr,req.user_agent,res,time, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase, letters))
    time = strftime('%I:%M %p')
    log_request(request, results, time)
    return render_template('results.html', the_phrase=phrase, 
                                           the_letters=letters,
                                           the_title=title,
                                           the_results=results,)


@app.route('/viewlog')
def view_the_log() -> str:
    with open('C:\\Users\\vladi\python_prj\webapp\\vsearch.log') as log:
        contents = log.readlines()
    return escape(''.join(contents)) 



if __name__ == '__main__':
    app.run(debug=True)