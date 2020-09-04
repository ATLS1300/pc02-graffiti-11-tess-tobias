#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:38:06 2020

@author: tesstobias
"""
from turtle import * # import turtle into workspace

colormode(225)

panel = Screen()
w=600
h=600
panel.setup(width=w, height=h)

image = "Bezos.gif"
#panel.bgcolor("lightgreen")
panel.bgpic(image)

#code


t = Turtle()
t.hideturtle()
t.pensize(10)
t.speed(7)
t.color('green')
t.shape('turtle')

Turtle().pensize(10)

#t.left(120)
#t.forward(200)
#t.showturtle()

t.showturtle()
t.circle(90)






















