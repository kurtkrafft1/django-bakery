import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from ..connection import Connection
from breadapp.models import Bread, model_factory

def bread_list(request):
    if request.method == "GET":
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