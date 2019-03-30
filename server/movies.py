from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from math import ceil

from server.db import get_db

bp = Blueprint('movies', __name__)

movies_per_page = 10


@bp.route('/movies')
def movies():
    db = get_db()
    total = db.execute(
        'SELECT COUNT(*) FROM movies'
    ).fetchone()

    page = request.args.get('page')
    print("ORIGINAL PAGE: " + str(page))
    # Check what page the user is viewing

    if page is None:
        page = 1
    else:
        page = int(page)

    offset = (page - 1) * movies_per_page

    if request.args.get('search'):
        # Search query in request
        movies = db.execute(
            'SELECT * FROM movies'
            ' WHERE title LIKE ?'
            ' LIMIT ? OFFSET ?',
            ('%' + request.args.get('search') + '%', movies_per_page, offset,)
        ).fetchall()

        # Number of query results
        results = db.execute(
            'SELECT COUNT(*) FROM movies'
            ' WHERE title LIKE ?',
            ('%' + request.args.get('search') + '%',)
        ).fetchone()[0]

        maxPages = ceil(int(results) / movies_per_page)
    else:
        # No query, just load from DB
        maxPages = ceil(int(total[0]) / movies_per_page)

        movies = db.execute(
            'SELECT * FROM movies LIMIT ? OFFSET ?', (movies_per_page, offset,)
        ).fetchall()

        results = -1

    # Determine the paths for the next and previous buttons
    path = request.path + '?'
    if request.args.get('search'):
        path = path + 'search=' + request.args.get('search') + '&'

    next = path + 'page=' + str(page+1)
    prev = path + 'page=' + str(page-1)

    return render_template('movies.html',
                           movies=movies,
                           stats={'total': total[0],
                                  'results': results},
                           pages={'current': page,
                                  'max': maxPages},
                           links={'next': next,
                                  'prev': prev}
                           )
