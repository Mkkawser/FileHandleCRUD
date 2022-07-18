from asyncore import write
from distutils.file_util import copy_file
import pickle
import csv
from ctypes import c_void_p
from dataclasses import replace
import os
from turtle import update
import pandas as pd

filepath = "demo.csv"

inf = ["MK", "CSE", "Narayngonj"]
Hader = ["Name", "Sub", "State"]


def create():
    with open(filepath, "a", newline='') as f:
        fWriter = csv.writer(f)
        fWriter.writerow(Hader)
        fWriter.writerow(inf)


def fileRead():
    with open(filepath, "r") as f:
        freader = csv.reader(f)
        for line in freader:
            print(line)


def delete():
    with open(filepath, "r") as f:
        freader = list(csv.DictReader(f))
        # for line in freader:
        #     if line["Name"] == "MK":
        #         line["Name"] = "Kawser Ahmed"

    with open("update.csv", "w", newline="") as ff:
        fw = csv.DictWriter(ff, Hader)
        fw.writeheader()
        for line in freader:
            if line["Name"] == "mk":
                continue
            fw.writerow(line)

    x = copy_file("update.csv", filepath)
    # print(x)


def update():
    with open(filepath, "r") as f:
        freader = list(csv.DictReader(f))
        # for line in freader:
        #     if line["Name"] == "MK":
        #         line["Name"] = "Kawser Ahmed"

    with open("update.csv", "w", newline="") as ff:
        fw = csv.DictWriter(ff, Hader)
        fw.writeheader()
        for line in freader:
            if line["Name"] == "Kawser Ahmed":
                line["Name"] = "mk"
            fw.writerow(line)

    x = copy_file("update.csv", filepath)


# create()
# fileRead()


# update()
# print(os.path.getsize(filepath))
# print(Hader.index('Name'))
