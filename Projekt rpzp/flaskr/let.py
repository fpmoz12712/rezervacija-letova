from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('let', __name__)

@bp.route('/')
def index():
    db = get_db()
    letovi = db.execute(
        'SELECT *, l1.naziv As naziv1, l2.naziv As naziv2 '
        ' FROM let l JOIN lokacija l1 ON l.polazna_lokacija = l1.id JOIN lokacija l2 ON l.dolazna_lokacija = l2.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('let/index.html', letovi=letovi)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        tip = request.form.get('tip', 'off')
        polazna_lokacija = request.form['polazna_lokacija']
        dolazna_lokacija = request.form['dolazna_lokacija']
        datum_polaska = request.form['datum_polaska']
        error = None

        if tip == 'on':
            tip = 1
        elif tip == 'off':
            tip = 2

        if not polazna_lokacija:
            error = 'Polazna lokacija je obavezna'

        if not dolazna_lokacija:
            error = 'Dolazna lokacija je obavezna'

        if not datum_polaska:
            error = 'Datum polaska je obavezan'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO let (tip, polazna_lokacija, dolazna_lokacija, datum_polaska)'
                ' VALUES (?, ?, ?, ?)',
                (tip, polazna_lokacija, dolazna_lokacija, datum_polaska)
            )
            db.commit()
            return redirect(url_for('let.index'))
    db = get_db()
    lokacije = db.execute(
        'SELECT *'
        ' FROM lokacija'
    ).fetchall()
    return render_template('let/create.html', lokacije=lokacije)