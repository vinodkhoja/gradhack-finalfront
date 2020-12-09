from django.shortcuts import render
from django.http import HttpResponse
from BankforBanks import models
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from jinja2 import Environment, FileSystemLoader


import random, math
from django.template import loader

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./BankforBanks/echarts_templates"))

# Create your views here.

def index(request):
    # l3d = line3d()
    # return HttpResponse(l3d.render_embed())
    return render(request, "index.html")


def sign_in(request):
    return render(request, "signIn.html")

def log_out(request):
    return render(request, "logOut.html")

def main_page(request):
    return render(request, "main.html")

def accounts(request):
    return render(request, "accounts.html")

def add_account(request):
    return render(request, "addAccount.html")

def bank_stats(request):
    return render(request, "bankStats.html")

def analysis(request):
    return render(request, "analysis.html")

def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D()
    line3d.add("", _data, grid3d_opts=opts.Grid3DOpts(
            width=100, depth=100, rotate_speed=150, is_rotate=True
        ))
    return line3d

