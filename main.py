import banner_db
from banner_db import title_header
from bs4 import BeautifulSoup as bs
import requests
import subprocess
from bcolors import bcolors
from autoscraper import AutoScraper

program_running = True


# ----------##--------------##-----------#
#               FUNCTIONS                #
# -------- -##--------------##-----------#

# Print a banner from the banner db
def display_banner(banner):
    print(banner)


# ----------##--------------##-----------#
#               MENUS                #
# -------- -##--------------##-----------#

def display_menu():
    print(f'\t{bcolors.OKBLUE + bcolors.HEADER}Choose from your options below:  {bcolors.ENDC} \n')
    print(f'\t\t{bcolors.OKGREEN} (1) Install Packages {bcolors.ENDC} ')
    print(f'\t\t{bcolors.OKGREEN} (2) Convert Images {bcolors.ENDC} ')
    print(f'\t\t{bcolors.OKGREEN} (3) Map Local Network {bcolors.ENDC} ')
    print(f'\t\t{bcolors.OKGREEN} (4) Create Content {bcolors.ENDC} ')
    print(f'\t\t{bcolors.OKGREEN} (5) Scrape the Web {bcolors.ENDC} ')
    print(f'\t\t{bcolors.OKGREEN} (6) Make Boss Decisions {bcolors.ENDC} \n')
    menu_choice = input(f'\t\t\t{bcolors.WARNING}Please enter your menu choice: {bcolors.ENDC}')
    return menu_choice


def scrape_menu():
    subprocess.run("clear")
    wanted_list = []
    back_or_forward = input(f'{bcolors.WARNING + bcolors.HEADER} Scrape(1) or return to main menu(0)?: {bcolors.ENDC} \n')
    if back_or_forward == 1:
        print(f'\t{bcolors.OKBLUE + bcolors.HEADER}To scrape from the web, we need some deets:  {bcolors.ENDC} \n')
        url = input(f'\t\t{bcolors.OKGREEN} (#) URL of page to scrape: {bcolors.ENDC} ')
        type = input(f'\t\t\t{bcolors.OKGREEN} (#) Search via Text(text) or by HTML Tags(tag): {bcolors.ENDC} ')
        if type == "text":
            text = input(f'\t\t\t{bcolors.OKGREEN} (#) Input the text: {bcolors.ENDC} ')
        elif type == "tag":
            tag = input(f'\t\t\t{bcolors.OKGREEN} (#) input the tag (p, h1, etc): {bcolors.ENDC} ')
        else:
            print(f"Sorry, but your input was not recognized. Try again!")
            scrape_menu()
        print(f'\t\t{bcolors.OKBLUE}  {bcolors.ENDC} ')
    elif back_or_forward == 0:
        display_init_opening()
    else:
        print("Sorry could not read your input, please try again.")
        scrape_menu()
        

def display_init_opening():
    subprocess.run("clear")
    display_banner(banner_db.program_title)
    init_choice = display_menu()
    return init_choice


while program_running:
    subprocess.run("clear")
    choice = display_init_opening()

    if choice == "1":
        subprocess.run("clear")
        display_banner(banner_db.title_header)

    if choice == "5":
        subprocess.run("clear")
        display_banner(banner_db.title_header)

    if choice == "5":
        subprocess.run("clear")
        display_banner(banner_db.title_header)

    if choice == "5":
        subprocess.run("clear")
        display_banner(banner_db.title_header)