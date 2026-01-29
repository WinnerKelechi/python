from urllib import request

url = 'https://raw.githubusercontent.com/robertmartin8/MachineLearningStocks/refs/heads/master/stock_prices.csv'
#read file from url
def readfile(url):
    response = request.urlopen(url)
    read = response.read()
    read_str = str(read)
    body = read_str.split('\\n')
    location = 'downloadedfile/' + r'stocks.csv'
    openfile = open(location, 'w')
    for each_line in body:
        openfile.write(each_line + '\n')
    openfile.close()   

readfile(url)