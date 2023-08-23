# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.5.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x08\x99\
/\
****************\
****************\
****************\
****************\
************\x0d\x0a**\
\x0d\x0a** Copyright (\
C) 2013 Digia Pl\
c and/or its sub\
sidiary(-ies).\x0d\x0a\
** Contact: http\
://www.qt-projec\
t.org/legal\x0d\x0a**\x0d\
\x0a** This file is\
 part of the exa\
mples of the Qt \
Toolkit.\x0d\x0a**\x0d\x0a**\
 $QT_BEGIN_LICEN\
SE:BSD$\x0d\x0a** You \
may use this fil\
e under the term\
s of the BSD lic\
ense as follows:\
\x0d\x0a**\x0d\x0a** \x22Redist\
ribution and use\
 in source and b\
inary forms, wit\
h or without\x0d\x0a**\
 modification, a\
re permitted pro\
vided that the f\
ollowing conditi\
ons are\x0d\x0a** met:\
\x0d\x0a**   * Redistr\
ibutions of sour\
ce code must ret\
ain the above co\
pyright\x0d\x0a**     \
notice, this lis\
t of conditions \
and the followin\
g disclaimer.\x0d\x0a*\
*   * Redistribu\
tions in binary \
form must reprod\
uce the above co\
pyright\x0d\x0a**     \
notice, this lis\
t of conditions \
and the followin\
g disclaimer in\x0d\
\x0a**     the docu\
mentation and/or\
 other materials\
 provided with t\
he\x0d\x0a**     distr\
ibution.\x0d\x0a**   *\
 Neither the nam\
e of Digia Plc a\
nd its Subsidiar\
y(-ies) nor the \
names\x0d\x0a**     of\
 its contributor\
s may be used to\
 endorse or prom\
ote products der\
ived\x0d\x0a**     fro\
m this software \
without specific\
 prior written p\
ermission.\x0d\x0a**\x0d\x0a\
**\x0d\x0a** THIS SOFT\
WARE IS PROVIDED\
 BY THE COPYRIGH\
T HOLDERS AND CO\
NTRIBUTORS\x0d\x0a** \x22\
AS IS\x22 AND ANY E\
XPRESS OR IMPLIE\
D WARRANTIES, IN\
CLUDING, BUT NOT\
\x0d\x0a** LIMITED TO,\
 THE IMPLIED WAR\
RANTIES OF MERCH\
ANTABILITY AND F\
ITNESS FOR\x0d\x0a** A\
 PARTICULAR PURP\
OSE ARE DISCLAIM\
ED. IN NO EVENT \
SHALL THE COPYRI\
GHT\x0d\x0a** OWNER OR\
 CONTRIBUTORS BE\
 LIABLE FOR ANY \
DIRECT, INDIRECT\
, INCIDENTAL,\x0d\x0a*\
* SPECIAL, EXEMP\
LARY, OR CONSEQU\
ENTIAL DAMAGES (\
INCLUDING, BUT N\
OT\x0d\x0a** LIMITED T\
O, PROCUREMENT O\
F SUBSTITUTE GOO\
DS OR SERVICES; \
LOSS OF USE,\x0d\x0a**\
 DATA, OR PROFIT\
S; OR BUSINESS I\
NTERRUPTION) HOW\
EVER CAUSED AND \
ON ANY\x0d\x0a** THEOR\
Y OF LIABILITY, \
WHETHER IN CONTR\
ACT, STRICT LIAB\
ILITY, OR TORT\x0d\x0a\
** (INCLUDING NE\
GLIGENCE OR OTHE\
RWISE) ARISING I\
N ANY WAY OUT OF\
 THE USE\x0d\x0a** OF \
THIS SOFTWARE, E\
VEN IF ADVISED O\
F THE POSSIBILIT\
Y OF SUCH DAMAGE\
.\x22\x0d\x0a**\x0d\x0a** $QT_E\
ND_LICENSE$\x0d\x0a**\x0d\
\x0a***************\
****************\
****************\
****************\
*************/\x0d\x0a\
import QtQuick 2\
.0\x0d\x0a\x0d\x0a//![0]\x0d\x0aLi\
stView {\x0d\x0a    wi\
dth: 200; height\
: 250\x0d\x0a\x0d\x0a    mod\
el: myModel\x0d\x0a   \
 delegate: Text \
{ text: \x22Animal:\
 \x22 + type + \x22, \x22\
 + size }\x0d\x0a}\x0d\x0a//\
![0]\x0d\x0a\x0d\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x0f\xca[\xbc\
\x00v\
\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8a\x12\xb9Q\xb8\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
