from aiogram import types
from bs4 import BeautifulSoup
import requests

array = [
    'Blog', 'Humor & entertainment',
    'Business & Start-Ups', 'News & Mass media',
    'Music', 'Sales',
    'Cryptocurrency', 'Marketing, PR, advertising',
    'Art & Photo', 'Health & Sport',
    'Politics', 'Video & movies',
    'Technologies', 'Education',
    'Travels', 'Psychology',
    'Books', 'Fashion & Beauty',
    'Games & Apps', 'Quotations',
    'Economics', 'Food & Cooking',
    'Auto', 'Languages',
    'Design', 'Animals',
    'Medicine', 'Handmade',
    'Lifehacks', 'Other',
]
print(len(array))

array_emoji = [
    "📝", "😂", "🧰", "🗞", "🎹", "🛍", "💎",
    "💰", "🎨", "⚽", "🗳", "🎞", "💻", "✏", "✈",
    "👓", "📖", "👠", "🎮", "💬", "📈", "🍕",
    "🚙", "🇬🇧", "👚", "🐶", "💊", "🤚",
    "💡", "🌐"
]


def distributor_pages(page):
    dict_pages = {
        1: "first_page",
        2: "second_page",
        3: "third_page",
        4: "fourth_page",
        5: "five_page",
    }
    items = dict_pages.items()
    page_array = []
    for i in items:
        page_array.append(i)

    try:
        left = page_array[page - 1][1]
        right = page_array[page + 1][1]
    except IndexError:
        left = page_array[page - 1][1]
        right = page_array[page - page][1]
    return left, right


pages = []
big_array = []
markup_category = types.InlineKeyboardMarkup()

for i in array:
    button = types.InlineKeyboardButton(text="{} {}".format(array_emoji[array.index(i)], i), callback_data="test")
    x = array.index(i)
    pages.append(button)
    if (len(pages) % 6) == 0:
        L = pages[:]
        big_array.append(L)
        pages.clear()


def constructor(value, button_left_right):
    for i in value:
        if len(markup_category["inline_keyboard"]) > 3:
            markup_category["inline_keyboard"] = ""
        x = value.index(i)
        y = x % 2
        if y != 0:
            markup_category.row(value[x - 1], i)
    left_btn = types.InlineKeyboardButton(text="←", callback_data=button_left_right[0])
    right_btn = types.InlineKeyboardButton(text="→", callback_data=button_left_right[1])
    markup_category.row(left_btn, right_btn)
    return markup_category


def markup(page):
    page -= 1
    page_markup = constructor(big_array[page], distributor_pages(page))
    return page_markup






