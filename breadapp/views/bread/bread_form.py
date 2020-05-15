import sqlite3
from django.urls import reverse
from django.shortcuts import redirect, render
from breadapp.models import Bread, Ingredient, BreadIngredient, model_factory
from ..connection import Connection



def bread_form(request):
    template = "bread/bread_form.html"
    context = {

    }
    return render(request, template, context)
def get_bread(bread_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bread)
        db_cursor = conn.cursor()

        db_cursor("""
            SELECT * from breadapp_bread where id = ?
        """, (bread_id,))

        bread = db_cursor.fetchone()

        return bread

def bread_edit_form(request, bread_id):
    bread = get_bread(bread_id)
    