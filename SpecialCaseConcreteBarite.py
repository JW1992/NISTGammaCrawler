from bs4 import BeautifulSoup
import sqlite3

#The original website had a wrong html format..

html = '''
<html><head>
<title>NIST: X-Ray Mass Attenuation Coefficients - Concrete, Barite</title>
<script type="text/javascript" id="www-widgetapi-script" src="https://s.ytimg.com/yts/jsbin/www-widgetapi-vfl-P7Nkv/www-widgetapi.js" async=""></script><script src="https://www.youtube.com/iframe_api"></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script async="" type="text/javascript" id="_fed_an_ua_tag" src="https://dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=DOC&amp;subagency=NIST&amp;pua=UA-37115410-46&amp;yt=true&amp;exts=ppsx,pps,f90,sch,rtf,wrl,txz,m1v,xlsm,msi,xsd,f,tif,eps,mpg,xml,pl,xlt,c"></script>
</head>

<body bgcolor="white">
<a href="/PhysRefData/XrayMassCoef/cover.html"><img border="0" src="/Images/contents.gif" width="95" height="28" alt="Table of Contents"></a> &nbsp; 
<a href="/PhysRefData/XrayMassCoef/tab4.html">Back to table 4</a>

<p>
</p><div align="center">
<img align="middle" alt="Concrete, Barite graph" src="Graphs/concrba.gif">

<p>
<table cellpadding="0" cellspacing="0" border="0">
<tbody><tr valign="top"><td>

<table cellpadding="1" cellspacing="0" border="0">
<tbody><tr valign="top">
<td colspan="7">
<br>
<div align="center">
<b>Concrete, Barite</b> (Type BA)<br>
<font size="-1" face="Arial, Helvetica, sans-serif">
HTML table format</font></div><br></td>
</tr>

<tr valign="top">
<td colspan="7"><hr size="1" noshade=""></td>
</tr>

<tr valign="top">
<td>&nbsp;</td>
<td rowspan="72" width="20">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
<th scope="col">Energy<sup>&nbsp;</sup></th>
<td rowspan="72">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
<th scope="col"><i>μ</i>/<i>ρ</i><sub>&nbsp;</sub></th>
<td rowspan="72" width="20">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
<th scope="col"><i>μ</i><sub>en</sub>/<i>ρ</i><sub>&nbsp;</sub></th>
</tr>

<tr valign="top" align="center">
<td>&nbsp;</td>
<td><sup>&nbsp;</sup>(MeV)</td>
<td>(cm<sup>2</sup>/g)</td>
<td>(cm<sup>2</sup>/g)</td>
</tr>

<tr valign="top">
<td colspan="7"><hr size="1" noshade=""></td>
</tr>

<tr valign="top" align="right">
<td rowspan="3">&nbsp;</td>  
<td>1.00000E-03</td>  
<td>  6.349E+03</td>  
<td>  6.332E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.03063E-03</td>  
<td>  5.916E+03</td>  
<td>  5.900E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.06220E-03</td>  
<td>  5.507E+03</td>  
<td>  5.492E+03</td>
</tr>

<tr valign="top" align="right">
<td>56 M3</td>  
<td>  1.06220E-03</td>  
<td>  6.009E+03</td>  
<td>  5.992E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>1.09882E-03</td>  
<td>  5.563E+03</td>  
<td>  5.548E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.13670E-03</td>  
<td>  5.150E+03</td>  
<td>  5.135E+03</td>
</tr>

<tr valign="top" align="right">
<td>56 M2</td>  
<td> 1.13670E-03</td>  
<td>  5.350E+03</td>  
<td>  5.335E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>1.21224E-03</td>  
<td>  4.632E+03</td>  
<td>  4.619E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.29280E-03</td>  
<td>  4.001E+03</td>  
<td>  3.990E+03</td>
</tr>

<tr valign="top" align="right">
<td>56 M1</td>  
<td> 1.29280E-03</td>  
<td>  4.126E+03</td>  
<td>  4.114E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>1.29889E-03</td>  
<td>  4.082E+03</td>  
<td>  4.070E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.30500E-03</td>  
<td>  4.038E+03</td>  
<td>  4.026E+03</td>
</tr>

<tr valign="top" align="right">
<td>12 K</td>  
<td>  1.30500E-03</td>  
<td>  4.044E+03</td>  
<td>  4.032E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>1.50000E-03</td>  
<td>  2.917E+03</td>  
<td>  2.908E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.55960E-03</td>  
<td>  2.659E+03</td>  
<td>  2.650E+03</td>
</tr>

<tr valign="top" align="right">
<td>13 K</td>  
<td>  1.55960E-03</td>  
<td>  2.674E+03</td>  
<td>  2.665E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>1.69350E-03</td>  
<td>  2.195E+03</td>  
<td>  2.187E+03</td>
</tr>

<tr valign="top" align="right">
<td>1.83890E-03</td>  
<td>  1.798E+03</td>  
<td>  1.791E+03</td>
</tr>

<tr valign="top" align="right">
<td>14 K</td>  
<td>  1.83890E-03</td>  
<td>  1.828E+03</td>  
<td>  1.820E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>2.00000E-03</td>  
<td>  1.491E+03</td>  
<td>  1.483E+03</td>
</tr>

<tr valign="top" align="right">
<td>2.47200E-03</td>  
<td>  8.795E+02</td>  
<td>  8.738E+02</td>
</tr>

<tr valign="top" align="right">
<td>16 K</td>  
<td>  2.47200E-03</td>  
<td>  1.079E+03</td>  
<td>  1.059E+03</td>
</tr>

<tr valign="top" align="right">
<td rowspan="3">&nbsp;</td>
<td>3.00000E-03</td>  
<td>  6.692E+02</td>  
<td>  6.568E+02</td>
</tr>

<tr valign="top" align="right">
<td>4.00000E-03</td>  
<td>  3.190E+02</td>  
<td>  3.126E+02</td>
</tr>

<tr valign="top" align="right">
<td>4.03810E-03</td>  
<td>  3.113E+02</td>  
<td>  3.050E+02</td>
</tr>

<tr valign="top" align="right">
<td>20 K</td>  
<td>  4.03810E-03</td>  
<td>  3.567E+02</td>  
<td>  3.437E+02</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>5.00000E-03</td>  
<td>  2.048E+02</td>  
<td>  1.973E+02</td>
</tr>

<tr valign="top" align="right">
<td>5.24700E-03</td>  
<td>  1.805E+02</td>  
<td>  1.738E+02</td>
</tr>

<tr valign="top" align="right">
<td>56 L3</td>  
<td> 5.24700E-03</td>  
<td>  3.641E+02</td>  
<td>  3.408E+02</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>5.43204E-03</td>  
<td>  3.352E+02</td>  
<td>  3.141E+02</td>
</tr>

<tr valign="top" align="right">
<td>5.62360E-03</td>  
<td>  3.069E+02</td>  
<td>  2.880E+02</td>
</tr>

<tr valign="top" align="right">
<td>56 L2</td>  
<td> 5.62360E-03</td>  
<td>  3.925E+02</td>  
<td>  3.645E+02</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>5.80333E-03</td>  
<td>  3.633E+02</td>  
<td>  3.379E+02</td>
</tr>

<tr valign="top" align="right">
<td>5.98880E-03</td>  
<td>  3.353E+02</td>  
<td>  3.123E+02</td>
</tr>

<tr valign="top" align="right">
<td>56 L1</td>  
<td> 5.98880E-03</td>  
<td>  3.778E+02</td>  
<td>  3.510E+02</td>
</tr>

<tr valign="top" align="right">
<td rowspan="2">&nbsp;</td>
<td>6.00000E-03</td>  
<td>  3.760E+02</td>  
<td>  3.493E+02</td>
</tr>

<tr valign="top" align="right">
<td>7.11200E-03</td>  
<td>  2.437E+02</td>  
<td>  2.281E+02</td>
</tr>

<tr valign="top" align="right">
<td>26 K</td>  
<td>  7.11200E-03</td>  
<td>  2.605E+02</td>  
<td>  2.398E+02</td>
</tr>

<tr valign="top" align="right">
<td rowspan="6">&nbsp;</td>
<td>8.00000E-03</td>  
<td>  1.925E+02</td>  
<td>  1.782E+02</td>
</tr>

<tr valign="top" align="right">
<td>1.00000E-02</td>  
<td>  1.067E+02</td>  
<td>  9.960E+01</td>
</tr>

<tr valign="top" align="right">
<td>1.50000E-02</td>  
<td>  3.601E+01</td>  
<td>  3.363E+01</td>
</tr>

<tr valign="top" align="right">
<td>2.00000E-02</td>  
<td>  1.655E+01</td>  
<td>  1.527E+01</td>
</tr>

<tr valign="top" align="right">
<td>3.00000E-02</td>  
<td>  5.551E+00</td>  
<td>  4.912E+00</td>
</tr>

<tr valign="top" align="right">
<td>3.74406E-02</td>  
<td>  3.091E+00</td>  
<td>  2.624E+00</td>
</tr>

<tr valign="top" align="right">
<td>56 K</td>  
<td>  3.74406E-02</td>  
<td>  1.407E+01</td>  
<td>  4.746E+00</td>
</tr>

<tr valign="top" align="right">
<td rowspan="24">&nbsp;</td>
<td>4.00000E-02</td>  
<td>  1.185E+01</td>  
<td>  4.439E+00</td>
</tr>

<tr valign="top" align="right">
<td>5.00000E-02</td>  
<td>  6.671E+00</td>  
<td>  3.206E+00</td>
</tr>

<tr valign="top" align="right">
<td>6.00000E-02</td>  
<td>  4.143E+00</td>  
<td>  2.266E+00</td>
</tr>

<tr valign="top" align="right">
<td>8.00000E-02</td>  
<td>  1.968E+00</td>  
<td>  1.211E+00</td>
</tr>

<tr valign="top" align="right">
<td>1.00000E-01</td>  
<td>  1.122E+00</td>  
<td>  7.138E-01</td>
</tr>

<tr valign="top" align="right">
<td>1.50000E-01</td>  
<td>  4.423E-01</td>  
<td>  2.659E-01</td>
</tr>

<tr valign="top" align="right">
<td>2.00000E-01</td>  
<td>  2.568E-01</td>  
<td>  1.369E-01</td>
</tr>

<tr valign="top" align="right">
<td>3.00000E-01</td>  
<td>  1.460E-01</td>  
<td>  6.408E-02</td>
</tr>

<tr valign="top" align="right">
<td>4.00000E-01</td>  
<td>  1.104E-01</td>  
<td>  4.471E-02</td>
</tr>

<tr valign="top" align="right">
<td>5.00000E-01</td>  
<td>  9.309E-02</td>  
<td>  3.718E-02</td>
</tr>

<tr valign="top" align="right">
<td>6.00000E-01</td>  
<td>  8.245E-02</td>  
<td>  3.340E-02</td>
</tr>

<tr valign="top" align="right">
<td>8.00000E-01</td>  
<td>  6.936E-02</td>  
<td>  2.954E-02</td>
</tr>

<tr valign="top" align="right">
<td>1.00000E+00</td>  
<td>  6.112E-02</td>  
<td>  2.736E-02</td>
</tr>

<tr valign="top" align="right">
<td>1.25000E+00</td>  
<td>  5.404E-02</td>  
<td>  2.542E-02</td>
</tr>

<tr valign="top" align="right">
<td>1.50000E+00</td>  
<td>  4.915E-02</td>  
<td>  2.402E-02</td>
</tr>

<tr valign="top" align="right">
<td>2.00000E+00</td>  
<td>  4.296E-02</td>  
<td>  2.226E-02</td>
</tr>

<tr valign="top" align="right">
<td>3.00000E+00</td>  
<td>  3.676E-02</td>  
<td>  2.079E-02</td>
</tr>

<tr valign="top" align="right">
<td>4.00000E+00</td>  
<td>  3.388E-02</td>  
<td>  2.043E-02</td>
</tr>

<tr valign="top" align="right">
<td>5.00000E+00</td>  
<td>  3.240E-02</td>  
<td>  2.049E-02</td>
</tr>

<tr valign="top" align="right">
<td>6.00000E+00</td>  
<td>  3.162E-02</td>  
<td>  2.074E-02</td>
</tr>

<tr valign="top" align="right">
<td>8.00000E+00</td>  
<td>  3.116E-02</td>  
<td>  2.142E-02</td>
</tr>

<tr valign="top" align="right">
<td>1.00000E+01</td>  
<td>  3.138E-02</td>  
<td>  2.213E-02</td>
</tr>

<tr valign="top" align="right">
<td>1.50000E+01</td>  
<td>  3.282E-02</td>  
<td>  2.356E-02</td>
</tr>

<tr valign="top" align="right">
<td>2.00000E+01</td>  
<td>  3.439E-02</td>  
<td>  2.438E-02</td>
</tr>
</tbody></table></td>

<td width="50">&nbsp;</td>

<td><br>
<div align="center">
<b>Concrete, Barite</b> (Type BA)<br>
<font size="-1" face="Arial, Helvetica, sans-serif">ASCII format</font></div>
<pre>________________________________________

         <b>Energy</b><sub>&nbsp;</sub>        <i>μ</i>/<i>ρ</i>       <i>μ</i><sub>en</sub>/<i>ρ</i> 
         <sup>&nbsp;</sup>(MeV)       (cm<sup>2</sup>/g)    (cm<sup>2</sup>/g)
________________________________________

       1.00000E-03  6.349E+03  6.332E+03 
       1.03063E-03  5.916E+03  5.900E+03 
       1.06220E-03  5.507E+03  5.492E+03 
 56 M3 1.06220E-03  6.009E+03  5.992E+03 
       1.09882E-03  5.563E+03  5.548E+03 
       1.13670E-03  5.150E+03  5.135E+03 
 56 M2 1.13670E-03  5.350E+03  5.335E+03 
       1.21224E-03  4.632E+03  4.619E+03 
       1.29280E-03  4.001E+03  3.990E+03 
 56 M1 1.29280E-03  4.126E+03  4.114E+03 
       1.29889E-03  4.082E+03  4.070E+03 
       1.30500E-03  4.038E+03  4.026E+03 
 12 K  1.30500E-03  4.044E+03  4.032E+03 
       1.50000E-03  2.917E+03  2.908E+03 
       1.55960E-03  2.659E+03  2.650E+03 
 13 K  1.55960E-03  2.674E+03  2.665E+03 
       1.69350E-03  2.195E+03  2.187E+03 
       1.83890E-03  1.798E+03  1.791E+03 
 14 K  1.83890E-03  1.828E+03  1.820E+03 
       2.00000E-03  1.491E+03  1.483E+03 
       2.47200E-03  8.795E+02  8.738E+02 
 16 K  2.47200E-03  1.079E+03  1.059E+03 
       3.00000E-03  6.692E+02  6.568E+02 
       4.00000E-03  3.190E+02  3.126E+02 
       4.03810E-03  3.113E+02  3.050E+02 
 20 K  4.03810E-03  3.567E+02  3.437E+02 
       5.00000E-03  2.048E+02  1.973E+02 
       5.24700E-03  1.805E+02  1.738E+02 
 56 L3 5.24700E-03  3.641E+02  3.408E+02 
       5.43204E-03  3.352E+02  3.141E+02 
       5.62360E-03  3.069E+02  2.880E+02 
 56 L2 5.62360E-03  3.925E+02  3.645E+02 
       5.80333E-03  3.633E+02  3.379E+02 
       5.98880E-03  3.353E+02  3.123E+02 
 56 L1 5.98880E-03  3.778E+02  3.510E+02 
       6.00000E-03  3.760E+02  3.493E+02 
       7.11200E-03  2.437E+02  2.281E+02 
 26 K  7.11200E-03  2.605E+02  2.398E+02 
       8.00000E-03  1.925E+02  1.782E+02 
       1.00000E-02  1.067E+02  9.960E+01 
       1.50000E-02  3.601E+01  3.363E+01 
       2.00000E-02  1.655E+01  1.527E+01 
       3.00000E-02  5.551E+00  4.912E+00 
       3.74406E-02  3.091E+00  2.624E+00 
 56 K  3.74406E-02  1.407E+01  4.746E+00 
       4.00000E-02  1.185E+01  4.439E+00 
       5.00000E-02  6.671E+00  3.206E+00 
       6.00000E-02  4.143E+00  2.266E+00 
       8.00000E-02  1.968E+00  1.211E+00 
       1.00000E-01  1.122E+00  7.138E-01 
       1.50000E-01  4.423E-01  2.659E-01 
       2.00000E-01  2.568E-01  1.369E-01 
       3.00000E-01  1.460E-01  6.408E-02 
       4.00000E-01  1.104E-01  4.471E-02 
       5.00000E-01  9.309E-02  3.718E-02 
       6.00000E-01  8.245E-02  3.340E-02 
       8.00000E-01  6.936E-02  2.954E-02 
       1.00000E+00  6.112E-02  2.736E-02 
       1.25000E+00  5.404E-02  2.542E-02 
       1.50000E+00  4.915E-02  2.402E-02 
       2.00000E+00  4.296E-02  2.226E-02 
       3.00000E+00  3.676E-02  2.079E-02 
       4.00000E+00  3.388E-02  2.043E-02 
       5.00000E+00  3.240E-02  2.049E-02 
       6.00000E+00  3.162E-02  2.074E-02 
       8.00000E+00  3.116E-02  2.142E-02 
       1.00000E+01  3.138E-02  2.213E-02 
       1.50000E+01  3.282E-02  2.356E-02 
       2.00000E+01  3.439E-02  2.438E-02 
</pre></td>
</tr></tbody></table></p></div>

<p>
<a href="/PhysRefData/XrayMassCoef/tab4.html">Back to table 4</a>
</p><hr size="1" noshade="">
<a href="/PhysRefData/XrayMassCoef/cover.html"><img border="0" src="/Images/contents.gif" width="95" height="28" alt="Table of Contents"></a>


</body></html>
'''
soup_element = BeautifulSoup(html)
conn = sqlite3.connect('NISTElementsGammaAttenuation.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS ConcreteBarite")
c.execute("CREATE TABLE IF NOT EXISTS ConcreteBarite (absedge text, energy real, attencoeff real)")
c.execute("DELETE FROM ConcreteBarite")
print("Saving data table for ConcreteBarite")

for row in soup_element.find_all('tr', align="right"):
    elements = row.find_all('td', rowspan=False)
    if elements.__len__() == 3:
        # strTemp = "INSERT INTO " + element_name[i] + "  (energy, attencoNISTElementsGammaAttenuation.dbeff) VALUES (" + float(elements[0].string) + ", " + float(elements[1].string) + ")"
        # c.execute(strTemp)
        c.execute("INSERT INTO ConcreteBarite (energy, attencoeff) VALUES (?, ?)",
                  (float(elements[0].string), float(elements[1].string)))
        print("Energy = " + elements[0].string)
    elif elements.__len__() == 4:
        c.execute("INSERT INTO ConcreteBarite (absedge, energy, attencoeff) VALUES (?, ?, ?)",
                  (elements[0].string, float(elements[1].string), float(elements[2].string)))
        print("Energy = " + elements[1].string)
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()