import sqlite3

from django.urls import reverse
from django.shortcuts import redirect, render
from ..connection import Connection
from breadapp.models import Bread, Ingredient, BreadIngredient, model_factory

def bread_details(request, bread_id):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_bread
            db_cursor = conn.cursor()
            db_cursor.execute("""
                select b.id,
            b.name,
            b.region,
            i.id ing_id,
            i.name ing_name,
            i.local_source,
            bi.amount,
            bi.id relationship_id
            from breadapp_bread b 
            left join breadapp_breadingredient bi on bi.bread_id = b.id
            left join breadapp_ingredient i on bi.ingredient_id = i.id
            where b.id = ?
            
            """, (bread_id,))

            breads = db_cursor.fetchall()
            bread_dict = {}
            for (bread, ingredient) in breads :
                if bread.id not in bread_dict:
                    bread_dict[bread.id] = bread
                    bread_dict[bread.id].all_ingredients.append(ingredient)
                else:
                    bread_dict[bread_id].all_ingredients.append(ingredient)
            

            template = "bread/bread_details.html"
            bread_list = list(bread_dict.values())
            context = {
                'bread': bread_list[0]
            }
            return render(request, template, context)
    if request.method == "POST":
        form_data = request.POST
        if(
            "actual_method" in form_data and form_data['actual_method'] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                 db_cursor = conn.cursor()

                 db_cursor.execute("""
                    DELETE FROM breadapp_breadingredient
                    where id = ?
                 """, (bread_id,))


            return(redirect(reverse('breadapp:breads')))





def create_bread(cursor, row):
    row = sqlite3.Row(cursor, row)

    bread = Bread()
    bread.name = row["name"]
    bread.id = row["id"]
    bread.region = row['region']

    bread.all_ingredients = list()

    ingredient = Ingredient()
    ingredient.id = row['ing_id']
    ingredient.name = row['ing_name']
    ingredient.local_source = row['local_source']
    ingredient.amount = row["amount"]
    ingredient.relationship_id = row["relationship_id"]

    

    
    
    return (bread,ingredient,)

