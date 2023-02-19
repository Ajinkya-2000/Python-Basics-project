import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter Github username :")

url = 'https://github.com/' + github_user

r = requests.get(url)                                  # Sending request to that url
s = bs(r.content,'html.parser')                        # Getting html source code
profile_img = s.find('img',{'alt':'Avatar'})['src']    # Finding the profile image 


print("Below is the link to open the profil pic of the Github User")
print(profile_img)                                     # Displaying the link to get the profile image


