import requests
import webbrowser

filePath = 'test.png'
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']

# chrome_path = '/usr/bin/google-chrome %s' # Chrome on Linux
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s' # Chrome on Mac
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

webbrowser.get(chrome_path).open(fetchUrl)
