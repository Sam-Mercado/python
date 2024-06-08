import pytest
from tkinter import Tk, Button, Label
from tkinter import Frame
import calculator


def app():
    root = Tk()
    frm_main = Frame(root)
    frm_main.pack()
    calculator.populate_main_window_calculator(frm_main)
    yield root
    root.destroy()

def test_display_in_screen(app):
    btn_1 = app.children['!frame'].children['!button4']
    lbl_screen = app.children['!frame'].children['!label']
    btn_1.invoke()
    assert lbl_screen['text'] == '1'

def test_delete_from_screen(app):
    btn_1 = app.children['!frame'].children['!button4']
    lbl_screen = app.children['!frame'].children['!label']
    btn_1.invoke()
    calculator.delete_from_screen()
    assert lbl_screen['text'] == ''

def test_calculation(app):
    btn_1 = app.children['!frame'].children['!button4']
    btn_2 = app.children['!frame'].children['!button5']
    btn_plus = app.children['!frame'].children['!button12']
    btn_equal = app.children['!frame'].children['!button20']
    lbl_screen = app.children['!frame'].children['!label']

    btn_1.invoke()
    btn_plus.invoke()
    btn_2.invoke()
    btn_equal.invoke()

    assert lbl_screen['text'] == '3'

def test_calculation_error(app):
    btn_1 = app.children['!frame'].children['!button4']
    btn_div = app.children['!frame'].children['!button16']
    btn_equal = app.children['!frame'].children['!button20']
    lbl_screen = app.children['!frame'].children['!label']

    btn_1.invoke()
    btn_div.invoke()
    btn_equal.invoke()

    assert lbl_screen['text'] == 'ERROR'

if __name__ == "__main__":
    pytest.main()