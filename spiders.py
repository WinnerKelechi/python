import requests
from bs4 import BeautifulSoup
#googurl = 'https://www.google.com/search?q=list+of+companies+in+lagos&lr=&sca_esv=d802faf0aaa25922&as_qdr=all&sxsrf=ANbL-n5sFLb48WutcsMkB4YIv1ppPtonSg:1769693882667&udm=1&lsack=umJ7aY64KNOthbIPntynkQI&sa=X&ved=2ahUKEwiO_fK577CSAxXTVkEAHR7uKSIQjGp6BAgqEAE&biw=1100&bih=953&dpr=1&aic=0'


def link_crawler(maxpages):
    page = 1
    while page <= maxpages:
        url = 'https://jiji.ng/cars' 
        get_code = requests.get(url)
        plain_text = get_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('a', {'class':'b-list-advert-base b-list-advert-base--gallery qa-advert-list-item'}):
            href = 'https://jiji.ng/cars' + link.get('href')
            print(href + '\n')
        page += 1
link_crawler(1)
