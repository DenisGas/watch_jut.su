# Watch jut.su

Work in pairs with my [Chrome extension](https://github.com/DenisGas/jut.su_next-series) and opens jut.su video in fullscreen

❗ Works only on Windows PC.

## I use 

python -v 3.11

selenium -v 4.9.1

---

## Install

You need install python, selenium web driver

[python download](https://www.python.org/downloads/)

After installing python

---

In cmd 

```cmd
pip install selenium
```

## Config

In "config.ini"

```ini
chrome_data_dir = C:\Users\YOU_PC_NAME\AppData\Local\Google\Chrome\User Data
```
Specify the path to the folder where you have chrome installed.

---

In "config.ini"
```ini
chrome_profile = PYTHON 
```
if you did not have a profile in chrome with this name, it will be created, you can also put your own profile



## Use

When you downloaded the folder with the code and made the config,
you need to open main.py - ***If chrome is already open, then close it, otherwise it will not work.***
If you did everything right, it will start and open jut.su

in extension "jut.su_next-series" you need **ON** checkbox to "One click to FullScreen(Overlay)"
and reload page

![preview img](./preview/extenstion_checkbox.png)


## Preview


![preview gif](./preview/how_work.gif)