import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from ..connection import Connection
from breadapp.models import Bread, model_factory

def bread_list(request):
    if request.method == "GET":
        '''connect to data base and grab the entire list of breads then doa  fetch all and send those breads tot he html page'''
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Bread)

            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                Select * from breadapp_bread
            """)

            breads = db_cursor.fetchall()

            template = "bread/bread_list.html"
            context = {
                'breads': breads
            }

            return render(request, template, context)
    if request.method == "POST":
        ''' check that it is a post method and then add the bread to the breadapp_bread table, afterwards get all the breads again!!!!'''
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Bread)
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT into breadapp_bread (name, region)
                values (?, ?)
            """, (form_data["name"], form_data["region"]))
            
            return redirect(reverse('breadapp:breads'))

