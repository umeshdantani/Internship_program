from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content=html_file.read()
    # print(content)

    soap = BeautifulSoup(content,'lxml')
        # print(soap.prettify())
    #tags=soap.find('h3')
    #print(tags)
    #html_tags=soap.find_all('h5')
    #print(html_tags)
    #for list in html_tags:
        #print(list.text)
    cards=soap.find_all('div',class_='card')
    for card in cards:
        #print(card)
        #print(card.h5)
        c_name=card.h5.text
        c_price=card.a.text.split()[-1]
        #print(c_price)
        #print(c_name)
        #print(f"{c_name} costs {c_price}")

