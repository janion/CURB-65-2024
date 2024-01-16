from shiny import App

from curb65.ui import curb65_ui
from curb65.server import curb65_server

app = App(ui=curb65_ui(), server=curb65_server)