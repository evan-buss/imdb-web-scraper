# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import logging
import os


class MovieToDBPipeLine(object):
    def __init__(self):
        self.connection = sqlite3.connect(
            os.path.abspath(os.path.join(
                __file__, "../../instance/movies.db")),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS movies'
            ' (title TEXT PRIMARY KEY,'
            ' year INT,'
            ' rating REAL,'
            ' poster TEXT,'
            ' summary TEXT)'
        )

    def process_item(self, item, spider):
        self.cursor.execute(
            'SELECT * FROM movies WHERE title = ?', (item['title'],)
        )

        result = self.cursor.fetchone()
        if result:
            logging.warning(f"{item['title']} is already in the database")
        else:
            self.cursor.execute(
                'INSERT INTO movies (title, year, rating, poster, summary)'
                ' VALUES (?, ?, ?, ?, ?)',
                (
                    item['title'],
                    item['year'],
                    item['rating'],
                    item['poster'],
                    item['summary']
                )
            )
            self.connection.commit()
            logging.info(f"{item['title']} added to the database")
        return item
