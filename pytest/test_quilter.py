import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/")

import matplotlib.pyplot as plt
import quilter


def test_add():
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot([1, 2], label="my leg")
    ax.set_title("test")
    ax.legend()

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.plot([2, 2])
    ax2.set_title("test 2")

    out = fig + fig2

    assert isinstance(out, plt.Figure), "test addition failed"


def test_div():
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot([1, 2], label="my leg")
    ax.set_title("test")
    ax.legend()

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.plot([2, 2])
    ax2.set_title("test 2")

    out = fig / fig2

    assert isinstance(out, plt.Figure), "test divide failed"


def test_combo():
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot([1, 2], label="my leg")
    ax.set_title("test")
    ax.legend()

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.plot([2, 2])
    ax2.set_title("test 2")

    out = (fig + fig2) / fig2

    assert isinstance(out, plt.Figure), "test combo failed"
