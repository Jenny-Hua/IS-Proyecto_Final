from flask import render_template
from . import ponencia


@ponencia.route('/ponencias', methods=('GET', 'POST'))
def ponencia():
    title = 'Ponencias'
    return render_template('ponencias.html', title=title)
