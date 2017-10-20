from flask import Flask
# from datetime import datetime
from pyvirtualdisplay import Display
from selenium import webdriver

app = Flask(__name__)

# def get_pic(siteURL):
#   display = Display(visible=0, size=(1024,800))
#   display.start()
#
#   print "Starting display..."
#   browser = webdriver.Firefox()
#   print "Loading site...."
#   browser.get('https://' + siteURL)
#   browser.get_screenshot_as_base64('screenie.txt')
#   return "Saved"

@app.route('/')
def hello():
  display = Display(visible=0, size=(1024,800))
  display.start()

  print "Starting display..."
  browser = webdriver.Firefox()
  print "Loading site...."
  browser.get('https://' + siteURL)
  browser.get_screenshot_as_base64('screenie.txt')
  return "Saved"

@app.route('/<siteURL>')
def get_pic(siteURL):
  display = Display(visible=0, size=(1024,800))
  display.start()

  print "Starting display..."
  browser = webdriver.Firefox()
  print "Loading site...."
  browser.get('https://' + siteURL)
  browser.get_screenshot_as_base64('screenie.txt')
  return "Saved"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
