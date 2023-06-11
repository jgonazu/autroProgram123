import sys
from bs4 import BeautifulSoup
from torpy.http.requests import TorRequests


def scraper():
    grab = None
    lista = ""
    #global contenido
    print('scraper : INFO : stay in tune...', flush=True)

    while grab is None:
        try:
            with TorRequests() as tor_requests:
                with tor_requests.get_session() as sess:
                    grab = sess.get("https://elcano.top")
                    print(grab)
        except:
            print("scraper : ERROR : line 25")
            sys.exit(1)

    soup = BeautifulSoup(grab.text, 'html.parser')
    for enlace in soup.find_all('a'):
        acelink = enlace.get('href')
        canal = enlace.text
        if not str(acelink).startswith("acestream://") or canal == "aquÃ­":
            pass
        else:
            link = str(acelink).replace("acestream://", "")
            lista += str((canal + "\n" + link + "\n"))

            contenido = ((lista.replace(u'\xa0', u' ')).strip())

    if contenido != "":
        #print(contenido, flush=True)
        print("scraper : OK : channels retrieved")
    else:
        print("scraper : ERROR : channels could not be retrieved")
        #scraper()
        sys.exit(0)

    return contenido

#scraper()
