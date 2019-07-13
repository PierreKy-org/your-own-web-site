
def ajout_element():
    fd = open('index.html', 'r')
    oui = fd.readlines()
    fd.close()
    print(oui)
    for i in range(len(oui)):
        if '<h1>' in oui[i]:
            print( "CA EXISTE")
            oui.insert(i+1, "<p>CACA PISSOU</p>\n")
    fd = open('index.html', 'w')
    oui = "".join(oui)
    fd.write(oui)
    fd.close()

    
def base_html():
    fd = open('index.html', 'w')
    fd.write("<!doctype html>\n\t<html lang='fr'>\n\t\t<head>\n\t\t\t<meta charset='utf-8'>\n\t\t\t<title>Titre de la page</title>\n\t\t\t<link rel='stylesheet' href='style.css'>\n\t\t\t<script src='script.js'></script>\n\t\t</head>\n\t\t<body>")
    fd.write("\n\t\t\t<h1>test</h1>\n\t\t</body>\n\t</html>")
    fd.close()
    choix = input("Voulez-vous ajouter un élément à la page ?")
    if choix == "oui":
        ajout_element()


if __name__ == '__main__':
    base_html()
