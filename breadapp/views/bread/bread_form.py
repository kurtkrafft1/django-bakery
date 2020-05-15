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