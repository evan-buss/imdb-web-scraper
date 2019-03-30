from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from math import ceil

from server.db import get_db

bp = Blueprint('movies', __name__)


@bp.route('/movies')
def movies():
    db = get_db()
    total = db.execute(
        'SELECT COUNT(*) FROM movies'
    ).fetchone()

    page = request.args.get('page')
    print("ORIGINAL PAGE: " + str(page))
    # Check what page the user is viewing
    if page:
        page = int(page) - 1
    else:
        page = 0

    offset = page * 20

    if request.args.get('search'):
        # Search query in request

        movies = db.execute(
            'SELECT * FROM movies'
            ' WHERE title LIKE ?'
            ' LIMIT 20 OFFSET ?',
            ('%' + request.args.get('search') + '%', offset,)
        ).fetchall()

        # Number of query results
        results = db.execute(
            'SELECT COUNT(*) FROM movies'
            ' WHERE title LIKE ?',
            ('%' + request.args.get('search') + '%',)
        ).fetchone()[0]

        maxPages = ceil(int(results) / 20)

    else:
        # No query, just load from DB
        maxPages = ceil(int(total[0]) / 20)

        movies = db.execute(
            'SELECT * FROM movies LIMIT 20 OFFSET ?', (offset,)
        ).fetchall()

        results = 0

    return render_template('movies.html',
                           movies=movies,
                           stats={'total': total[0],
                                  'results': results},
                           pages={'current': page+1,
                                  'max': maxPages},
                           )
# links={'next': nextLink, 'prev': prevLink}
