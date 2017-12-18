import requests
import sqlite3
from lxml import html
from bs4 import BeautifulSoup
import time

URL_BASE = "https://physics.nist.gov/PhysRefData/XrayMassCoef/"

#Return the elements abbrev
def no_align_no_rowspan_no_href(tag):
    #return not tag.has_attr('align') and not tag.has_attr('rowspan') and not tag.has_attr('href')
    return not tag.has_attr('href')

def main():
    session_requests = requests.session()

    element_name = []
    element_symbol = []
    element_href = []
    atom_number = []
    # Get login csrf token
    #result = session_requests.get(LOGIN_URL)
    result = session_requests.get(URL_BASE+"tab4.html")
    soup = BeautifulSoup(result.text, "html.parser")
    #Debug-JW-Nov25: Print all the link addresses to-be appended
    for link in soup.body.center.table.find_all(href=True):
        #print(link.get('href'))
        #print(link.string)
        element_href.append(link.get('href'))
        element_name.append(str(link.contents[link.__len__()-1]).replace(', ', '').replace(' ','').replace('-','').replace('/','').replace('"','').replace('(','').replace(')',''))

    # Debug-JW-Nov25: Print all the element atom numbers and abbrevs
    # x = 0   #This is really stupid...
    # for link in soup.body.center.table.find_all(align="right"):
    #    x+=1
    #    #print(link.string)
    #    #print(link.next_sibling.next_sibling.next_sibling.next_sibling.string)
    #    atom_number.append(link.string)
    #    if x<=4:
    #        element_symbol.append(link.next_sibling.next_sibling.next_sibling.next_sibling.string)
    #    else:
    #        element_symbol.append(link.next_sibling.next_sibling.string)
    #elementsBodyTag = soup.body.center.table.tbody

    #for row in soup.find_all('tr'):
    #    elements = row.find_all('td', rowspan=False)
    #    print(elements[1].text)
    #    print(elements[4].text)
    #    print(elements[7].text)
    #    print(elements[10].text)

    conn = sqlite3.connect('NISTElementsGammaAttenuation.db')
    c = conn.cursor()

    # Create table
    c.execute('''DROP TABLE IF EXISTS materials''')
    c.execute('''CREATE TABLE IF NOT EXISTS materials
                     (name text)''')
    # Clear table
    c.execute('''DELETE FROM materials''')
    # Insert a row of data
    for i in range(0, 48):
        c.execute("INSERT INTO materials VALUES (?)", (element_name[i], ))
    # Save (commit) the changes

    for i in range(38,39):
        result_element = session_requests.get(URL_BASE+element_href[i])
        soup_element = BeautifulSoup(result_element.text, "html.parser")
        # tagTemp = soup_element.body.div.p.table.tr.table
        tagTemp = soup_element.body.table
        # Create table
        c.execute("DROP TABLE IF EXISTS " + element_name[i])
        c.execute("CREATE TABLE IF NOT EXISTS " + element_name[i] +" (absedge text, energy real, attencoeff real)")
        c.execute("DELETE FROM " + element_name[i])

        print("Saving data table for "+element_name[i])

        # for row in tagTemp.find_all('tr', )[5:]:
        # for row in tagTemp.find_all('tr', align = "right"):
        #For a few materials the formatting is not consistent
        for row in soup_element.find_all('tr', align="right"):
            elements = row.find_all('td', rowspan=False)
            if elements.__len__() == 3:
                #strTemp = "INSERT INTO " + element_name[i] + "  (energy, attencoNISTElementsGammaAttenuation.dbeff) VALUES (" + float(elements[0].string) + ", " + float(elements[1].string) + ")"
                #c.execute(strTemp)
                c.execute("INSERT INTO {} (energy, attencoeff) VALUES (?, ?)".format(element_name[i].replace(', ', '')), (float(elements[0].string), float(elements[1].string)))
                print("Energy = " + elements[0].string)
            elif elements.__len__() == 4:
                c.execute("INSERT INTO {} (absedge, energy, attencoeff) VALUES (?, ?, ?)".format(element_name[i]),
                          (elements[0].string, float(elements[1].string), float(elements[2].string)))
                print("Energy = " + elements[1].string)
        time.sleep(2)

    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

if __name__ == '__main__':
    main()