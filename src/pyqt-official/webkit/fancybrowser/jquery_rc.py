# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.5.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\xdf\xb8\
/\
*\x0d\x0a * jQuery Jav\
aScript Library \
v1.3.2\x0d\x0a * http:\
//jquery.com/\x0d\x0a \
*\x0d\x0a * Copyright \
(c) 2009 John Re\
sig\x0d\x0a * Dual lic\
ensed under the \
MIT and GPL lice\
nses.\x0d\x0a * http:/\
/docs.jquery.com\
/License\x0d\x0a *\x0d\x0a *\
 Date: 2009-02-1\
9 17:34:21 -0500\
 (Thu, 19 Feb 20\
09)\x0d\x0a * Revision\
: 6246\x0d\x0a */\x0d\x0a(fu\
nction(){var l=t\
his,g,y=l.jQuery\
,p=l.$,o=l.jQuer\
y=l.$=function(E\
,F){return new o\
.fn.init(E,F)},D\
=/^[^<]*(<(.|\x5cs)\
+>)[^>]*$|^#([\x5cw\
-]+)$/,f=/^.[^:#\
\x5c[\x5c.,]*$/;o.fn=o\
.prototype={init\
:function(E,H){E\
=E||document;if(\
E.nodeType){this\
[0]=E;this.lengt\
h=1;this.context\
=E;return this}i\
f(typeof E===\x22st\
ring\x22){var G=D.e\
xec(E);if(G&&(G[\
1]||!H)){if(G[1]\
){E=o.clean([G[1\
]],H)}else{var I\
=document.getEle\
mentById(G[3]);i\
f(I&&I.id!=G[3])\
{return o().find\
(E)}var F=o(I||[\
]);F.context=doc\
ument;F.selector\
=E;return F}}els\
e{return o(H).fi\
nd(E)}}else{if(o\
.isFunction(E)){\
return o(documen\
t).ready(E)}}if(\
E.selector&&E.co\
ntext){this.sele\
ctor=E.selector;\
this.context=E.c\
ontext}return th\
is.setArray(o.is\
Array(E)?E:o.mak\
eArray(E))},sele\
ctor:\x22\x22,jquery:\x22\
1.3.2\x22,size:func\
tion(){return th\
is.length},get:f\
unction(E){retur\
n E===g?Array.pr\
ototype.slice.ca\
ll(this):this[E]\
},pushStack:func\
tion(F,H,E){var \
G=o(F);G.prevObj\
ect=this;G.conte\
xt=this.context;\
if(H===\x22find\x22){G\
.selector=this.s\
elector+(this.se\
lector?\x22 \x22:\x22\x22)+E\
}else{if(H){G.se\
lector=this.sele\
ctor+\x22.\x22+H+\x22(\x22+E\
+\x22)\x22}}return G},\
setArray:functio\
n(E){this.length\
=0;Array.prototy\
pe.push.apply(th\
is,E);return thi\
s},each:function\
(F,E){return o.e\
ach(this,F,E)},i\
ndex:function(E)\
{return o.inArra\
y(E&&E.jquery?E[\
0]:E,this)},attr\
:function(F,H,G)\
{var E=F;if(type\
of F===\x22string\x22)\
{if(H===g){retur\
n this[0]&&o[G||\
\x22attr\x22](this[0],\
F)}else{E={};E[F\
]=H}}return this\
.each(function(I\
){for(F in E){o.\
attr(G?this.styl\
e:this,F,o.prop(\
this,E[F],G,I,F)\
)}})},css:functi\
on(E,F){if((E==\x22\
width\x22||E==\x22heig\
ht\x22)&&parseFloat\
(F)<0){F=g}retur\
n this.attr(E,F,\
\x22curCSS\x22)},text:\
function(F){if(t\
ypeof F!==\x22objec\
t\x22&&F!=null){ret\
urn this.empty()\
.append((this[0]\
&&this[0].ownerD\
ocument||documen\
t).createTextNod\
e(F))}var E=\x22\x22;o\
.each(F||this,fu\
nction(){o.each(\
this.childNodes,\
function(){if(th\
is.nodeType!=8){\
E+=this.nodeType\
!=1?this.nodeVal\
ue:o.fn.text([th\
is])}})});return\
 E},wrapAll:func\
tion(E){if(this[\
0]){var F=o(E,th\
is[0].ownerDocum\
ent).clone();if(\
this[0].parentNo\
de){F.insertBefo\
re(this[0])}F.ma\
p(function(){var\
 G=this;while(G.\
firstChild){G=G.\
firstChild}retur\
n G}).append(thi\
s)}return this},\
wrapInner:functi\
on(E){return thi\
s.each(function(\
){o(this).conten\
ts().wrapAll(E)}\
)},wrap:function\
(E){return this.\
each(function(){\
o(this).wrapAll(\
E)})},append:fun\
ction(){return t\
his.domManip(arg\
uments,true,func\
tion(E){if(this.\
nodeType==1){thi\
s.appendChild(E)\
}})},prepend:fun\
ction(){return t\
his.domManip(arg\
uments,true,func\
tion(E){if(this.\
nodeType==1){thi\
s.insertBefore(E\
,this.firstChild\
)}})},before:fun\
ction(){return t\
his.domManip(arg\
uments,false,fun\
ction(E){this.pa\
rentNode.insertB\
efore(E,this)})}\
,after:function(\
){return this.do\
mManip(arguments\
,false,function(\
E){this.parentNo\
de.insertBefore(\
E,this.nextSibli\
ng)})},end:funct\
ion(){return thi\
s.prevObject||o(\
[])},push:[].pus\
h,sort:[].sort,s\
plice:[].splice,\
find:function(E)\
{if(this.length=\
==1){var F=this.\
pushStack([],\x22fi\
nd\x22,E);F.length=\
0;o.find(E,this[\
0],F);return F}e\
lse{return this.\
pushStack(o.uniq\
ue(o.map(this,fu\
nction(G){return\
 o.find(E,G)})),\
\x22find\x22,E)}},clon\
e:function(G){va\
r E=this.map(fun\
ction(){if(!o.su\
pport.noCloneEve\
nt&&!o.isXMLDoc(\
this)){var I=thi\
s.outerHTML;if(!\
I){var J=this.ow\
nerDocument.crea\
teElement(\x22div\x22)\
;J.appendChild(t\
his.cloneNode(tr\
ue));I=J.innerHT\
ML}return o.clea\
n([I.replace(/ j\
Query\x5cd+=\x22(?:\x5cd+\
|null)\x22/g,\x22\x22).re\
place(/^\x5cs*/,\x22\x22)\
])[0]}else{retur\
n this.cloneNode\
(true)}});if(G==\
=true){var H=thi\
s.find(\x22*\x22).andS\
elf(),F=0;E.find\
(\x22*\x22).andSelf().\
each(function(){\
if(this.nodeName\
!==H[F].nodeName\
){return}var I=o\
.data(H[F],\x22even\
ts\x22);for(var K i\
n I){for(var J i\
n I[K]){o.event.\
add(this,K,I[K][\
J],I[K][J].data)\
}}F++})}return E\
},filter:functio\
n(E){return this\
.pushStack(o.isF\
unction(E)&&o.gr\
ep(this,function\
(G,F){return E.c\
all(G,F)})||o.mu\
ltiFilter(E,o.gr\
ep(this,function\
(F){return F.nod\
eType===1})),\x22fi\
lter\x22,E)},closes\
t:function(E){va\
r G=o.expr.match\
.POS.test(E)?o(E\
):null,F=0;retur\
n this.map(funct\
ion(){var H=this\
;while(H&&H.owne\
rDocument){if(G?\
G.index(H)>-1:o(\
H).is(E)){o.data\
(H,\x22closest\x22,F);\
return H}H=H.par\
entNode;F++}})},\
not:function(E){\
if(typeof E===\x22s\
tring\x22){if(f.tes\
t(E)){return thi\
s.pushStack(o.mu\
ltiFilter(E,this\
,true),\x22not\x22,E)}\
else{E=o.multiFi\
lter(E,this)}}va\
r F=E.length&&E[\
E.length-1]!==g&\
&!E.nodeType;ret\
urn this.filter(\
function(){retur\
n F?o.inArray(th\
is,E)<0:this!=E}\
)},add:function(\
E){return this.p\
ushStack(o.uniqu\
e(o.merge(this.g\
et(),typeof E===\
\x22string\x22?o(E):o.\
makeArray(E))))}\
,is:function(E){\
return !!E&&o.mu\
ltiFilter(E,this\
).length>0},hasC\
lass:function(E)\
{return !!E&&thi\
s.is(\x22.\x22+E)},val\
:function(K){if(\
K===g){var E=thi\
s[0];if(E){if(o.\
nodeName(E,\x22opti\
on\x22)){return(E.a\
ttributes.value|\
|{}).specified?E\
.value:E.text}if\
(o.nodeName(E,\x22s\
elect\x22)){var I=E\
.selectedIndex,L\
=[],M=E.options,\
H=E.type==\x22selec\
t-one\x22;if(I<0){r\
eturn null}for(v\
ar F=H?I:0,J=H?I\
+1:M.length;F<J;\
F++){var G=M[F];\
if(G.selected){K\
=o(G).val();if(H\
){return K}L.pus\
h(K)}}return L}r\
eturn(E.value||\x22\
\x22).replace(/\x5cr/g\
,\x22\x22)}return g}if\
(typeof K===\x22num\
ber\x22){K+=\x22\x22}retu\
rn this.each(fun\
ction(){if(this.\
nodeType!=1){ret\
urn}if(o.isArray\
(K)&&/radio|chec\
kbox/.test(this.\
type)){this.chec\
ked=(o.inArray(t\
his.value,K)>=0|\
|o.inArray(this.\
name,K)>=0)}else\
{if(o.nodeName(t\
his,\x22select\x22)){v\
ar N=o.makeArray\
(K);o(\x22option\x22,t\
his).each(functi\
on(){this.select\
ed=(o.inArray(th\
is.value,N)>=0||\
o.inArray(this.t\
ext,N)>=0)});if(\
!N.length){this.\
selectedIndex=-1\
}}else{this.valu\
e=K}}})},html:fu\
nction(E){return\
 E===g?(this[0]?\
this[0].innerHTM\
L.replace(/ jQue\
ry\x5cd+=\x22(?:\x5cd+|nu\
ll)\x22/g,\x22\x22):null)\
:this.empty().ap\
pend(E)},replace\
With:function(E)\
{return this.aft\
er(E).remove()},\
eq:function(E){r\
eturn this.slice\
(E,+E+1)},slice:\
function(){retur\
n this.pushStack\
(Array.prototype\
.slice.apply(thi\
s,arguments),\x22sl\
ice\x22,Array.proto\
type.slice.call(\
arguments).join(\
\x22,\x22))},map:funct\
ion(E){return th\
is.pushStack(o.m\
ap(this,function\
(G,F){return E.c\
all(G,F,G)}))},a\
ndSelf:function(\
){return this.ad\
d(this.prevObjec\
t)},domManip:fun\
ction(J,M,L){if(\
this[0]){var I=(\
this[0].ownerDoc\
ument||this[0]).\
createDocumentFr\
agment(),F=o.cle\
an(J,(this[0].ow\
nerDocument||thi\
s[0]),I),H=I.fir\
stChild;if(H){fo\
r(var G=0,E=this\
.length;G<E;G++)\
{L.call(K(this[G\
],H),this.length\
>1||G>0?I.cloneN\
ode(true):I)}}if\
(F){o.each(F,z)}\
}return this;fun\
ction K(N,O){ret\
urn M&&o.nodeNam\
e(N,\x22table\x22)&&o.\
nodeName(O,\x22tr\x22)\
?(N.getElementsB\
yTagName(\x22tbody\x22\
)[0]||N.appendCh\
ild(N.ownerDocum\
ent.createElemen\
t(\x22tbody\x22))):N}}\
};o.fn.init.prot\
otype=o.fn;funct\
ion z(E,F){if(F.\
src){o.ajax({url\
:F.src,async:fal\
se,dataType:\x22scr\
ipt\x22})}else{o.gl\
obalEval(F.text|\
|F.textContent||\
F.innerHTML||\x22\x22)\
}if(F.parentNode\
){F.parentNode.r\
emoveChild(F)}}f\
unction e(){retu\
rn +new Date}o.e\
xtend=o.fn.exten\
d=function(){var\
 J=arguments[0]|\
|{},H=1,I=argume\
nts.length,E=fal\
se,G;if(typeof J\
===\x22boolean\x22){E=\
J;J=arguments[1]\
||{};H=2}if(type\
of J!==\x22object\x22&\
&!o.isFunction(J\
)){J={}}if(I==H)\
{J=this;--H}for(\
;H<I;H++){if((G=\
arguments[H])!=n\
ull){for(var F i\
n G){var K=J[F],\
L=G[F];if(J===L)\
{continue}if(E&&\
L&&typeof L===\x22o\
bject\x22&&!L.nodeT\
ype){J[F]=o.exte\
nd(E,K||(L.lengt\
h!=null?[]:{}),L\
)}else{if(L!==g)\
{J[F]=L}}}}}retu\
rn J};var b=/z-?\
index|font-?weig\
ht|opacity|zoom|\
line-?height/i,q\
=document.defaul\
tView||{},s=Obje\
ct.prototype.toS\
tring;o.extend({\
noConflict:funct\
ion(E){l.$=p;if(\
E){l.jQuery=y}re\
turn o},isFuncti\
on:function(E){r\
eturn s.call(E)=\
==\x22[object Funct\
ion]\x22},isArray:f\
unction(E){retur\
n s.call(E)===\x22[\
object Array]\x22},\
isXMLDoc:functio\
n(E){return E.no\
deType===9&&E.do\
cumentElement.no\
deName!==\x22HTML\x22|\
|!!E.ownerDocume\
nt&&o.isXMLDoc(E\
.ownerDocument)}\
,globalEval:func\
tion(G){if(G&&/\x5c\
S/.test(G)){var \
F=document.getEl\
ementsByTagName(\
\x22head\x22)[0]||docu\
ment.documentEle\
ment,E=document.\
createElement(\x22s\
cript\x22);E.type=\x22\
text/javascript\x22\
;if(o.support.sc\
riptEval){E.appe\
ndChild(document\
.createTextNode(\
G))}else{E.text=\
G}F.insertBefore\
(E,F.firstChild)\
;F.removeChild(E\
)}},nodeName:fun\
ction(F,E){retur\
n F.nodeName&&F.\
nodeName.toUpper\
Case()==E.toUppe\
rCase()},each:fu\
nction(G,K,F){va\
r E,H=0,I=G.leng\
th;if(F){if(I===\
g){for(E in G){i\
f(K.apply(G[E],F\
)===false){break\
}}}else{for(;H<I\
;){if(K.apply(G[\
H++],F)===false)\
{break}}}}else{i\
f(I===g){for(E i\
n G){if(K.call(G\
[E],E,G[E])===fa\
lse){break}}}els\
e{for(var J=G[0]\
;H<I&&K.call(J,H\
,J)!==false;J=G[\
++H]){}}}return \
G},prop:function\
(H,I,G,F,E){if(o\
.isFunction(I)){\
I=I.call(H,F)}re\
turn typeof I===\
\x22number\x22&&G==\x22cu\
rCSS\x22&&!b.test(E\
)?I+\x22px\x22:I},clas\
sName:{add:funct\
ion(E,F){o.each(\
(F||\x22\x22).split(/\x5c\
s+/),function(G,\
H){if(E.nodeType\
==1&&!o.classNam\
e.has(E.classNam\
e,H)){E.classNam\
e+=(E.className?\
\x22 \x22:\x22\x22)+H}})},re\
move:function(E,\
F){if(E.nodeType\
==1){E.className\
=F!==g?o.grep(E.\
className.split(\
/\x5cs+/),function(\
G){return !o.cla\
ssName.has(F,G)}\
).join(\x22 \x22):\x22\x22}}\
,has:function(F,\
E){return F&&o.i\
nArray(E,(F.clas\
sName||F).toStri\
ng().split(/\x5cs+/\
))>-1}},swap:fun\
ction(H,G,I){var\
 E={};for(var F \
in G){E[F]=H.sty\
le[F];H.style[F]\
=G[F]}I.call(H);\
for(var F in G){\
H.style[F]=E[F]}\
},css:function(H\
,F,J,E){if(F==\x22w\
idth\x22||F==\x22heigh\
t\x22){var L,G={pos\
ition:\x22absolute\x22\
,visibility:\x22hid\
den\x22,display:\x22bl\
ock\x22},K=F==\x22widt\
h\x22?[\x22Left\x22,\x22Righ\
t\x22]:[\x22Top\x22,\x22Bott\
om\x22];function I(\
){L=F==\x22width\x22?H\
.offsetWidth:H.o\
ffsetHeight;if(E\
===\x22border\x22){ret\
urn}o.each(K,fun\
ction(){if(!E){L\
-=parseFloat(o.c\
urCSS(H,\x22padding\
\x22+this,true))||0\
}if(E===\x22margin\x22\
){L+=parseFloat(\
o.curCSS(H,\x22marg\
in\x22+this,true))|\
|0}else{L-=parse\
Float(o.curCSS(H\
,\x22border\x22+this+\x22\
Width\x22,true))||0\
}})}if(H.offsetW\
idth!==0){I()}el\
se{o.swap(H,G,I)\
}return Math.max\
(0,Math.round(L)\
)}return o.curCS\
S(H,F,J)},curCSS\
:function(I,F,G)\
{var L,E=I.style\
;if(F==\x22opacity\x22\
&&!o.support.opa\
city){L=o.attr(E\
,\x22opacity\x22);retu\
rn L==\x22\x22?\x221\x22:L}i\
f(F.match(/float\
/i)){F=w}if(!G&&\
E&&E[F]){L=E[F]}\
else{if(q.getCom\
putedStyle){if(F\
.match(/float/i)\
){F=\x22float\x22}F=F.\
replace(/([A-Z])\
/g,\x22-$1\x22).toLowe\
rCase();var M=q.\
getComputedStyle\
(I,null);if(M){L\
=M.getPropertyVa\
lue(F)}if(F==\x22op\
acity\x22&&L==\x22\x22){L\
=\x221\x22}}else{if(I.\
currentStyle){va\
r J=F.replace(/\x5c\
-(\x5cw)/g,function\
(N,O){return O.t\
oUpperCase()});L\
=I.currentStyle[\
F]||I.currentSty\
le[J];if(!/^\x5cd+(\
px)?$/i.test(L)&\
&/^\x5cd/.test(L)){\
var H=E.left,K=I\
.runtimeStyle.le\
ft;I.runtimeStyl\
e.left=I.current\
Style.left;E.lef\
t=L||0;L=E.pixel\
Left+\x22px\x22;E.left\
=H;I.runtimeStyl\
e.left=K}}}}retu\
rn L},clean:func\
tion(F,K,I){K=K|\
|document;if(typ\
eof K.createElem\
ent===\x22undefined\
\x22){K=K.ownerDocu\
ment||K[0]&&K[0]\
.ownerDocument||\
document}if(!I&&\
F.length===1&&ty\
peof F[0]===\x22str\
ing\x22){var H=/^<(\
\x5cw+)\x5cs*\x5c/?>$/.ex\
ec(F[0]);if(H){r\
eturn[K.createEl\
ement(H[1])]}}va\
r G=[],E=[],L=K.\
createElement(\x22d\
iv\x22);o.each(F,fu\
nction(P,S){if(t\
ypeof S===\x22numbe\
r\x22){S+=\x22\x22}if(!S)\
{return}if(typeo\
f S===\x22string\x22){\
S=S.replace(/(<(\
\x5cw+)[^>]*?)\x5c/>/g\
,function(U,V,T)\
{return T.match(\
/^(abbr|br|col|i\
mg|input|link|me\
ta|param|hr|area\
|embed)$/i)?U:V+\
\x22></\x22+T+\x22>\x22});va\
r O=S.replace(/^\
\x5cs+/,\x22\x22).substri\
ng(0,10).toLower\
Case();var Q=!O.\
indexOf(\x22<opt\x22)&\
&[1,\x22<select mul\
tiple='multiple'\
>\x22,\x22</select>\x22]|\
|!O.indexOf(\x22<le\
g\x22)&&[1,\x22<fields\
et>\x22,\x22</fieldset\
>\x22]||O.match(/^<\
(thead|tbody|tfo\
ot|colg|cap)/)&&\
[1,\x22<table>\x22,\x22</\
table>\x22]||!O.ind\
exOf(\x22<tr\x22)&&[2,\
\x22<table><tbody>\x22\
,\x22</tbody></tabl\
e>\x22]||(!O.indexO\
f(\x22<td\x22)||!O.ind\
exOf(\x22<th\x22))&&[3\
,\x22<table><tbody>\
<tr>\x22,\x22</tr></tb\
ody></table>\x22]||\
!O.indexOf(\x22<col\
\x22)&&[2,\x22<table><\
tbody></tbody><c\
olgroup>\x22,\x22</col\
group></table>\x22]\
||!o.support.htm\
lSerialize&&[1,\x22\
div<div>\x22,\x22</div\
>\x22]||[0,\x22\x22,\x22\x22];L\
.innerHTML=Q[1]+\
S+Q[2];while(Q[0\
]--){L=L.lastChi\
ld}if(!o.support\
.tbody){var R=/<\
tbody/i.test(S),\
N=!O.indexOf(\x22<t\
able\x22)&&!R?L.fir\
stChild&&L.first\
Child.childNodes\
:Q[1]==\x22<table>\x22\
&&!R?L.childNode\
s:[];for(var M=N\
.length-1;M>=0;-\
-M){if(o.nodeNam\
e(N[M],\x22tbody\x22)&\
&!N[M].childNode\
s.length){N[M].p\
arentNode.remove\
Child(N[M])}}}if\
(!o.support.lead\
ingWhitespace&&/\
^\x5cs/.test(S)){L.\
insertBefore(K.c\
reateTextNode(S.\
match(/^\x5cs*/)[0]\
),L.firstChild)}\
S=o.makeArray(L.\
childNodes)}if(S\
.nodeType){G.pus\
h(S)}else{G=o.me\
rge(G,S)}});if(I\
){for(var J=0;G[\
J];J++){if(o.nod\
eName(G[J],\x22scri\
pt\x22)&&(!G[J].typ\
e||G[J].type.toL\
owerCase()===\x22te\
xt/javascript\x22))\
{E.push(G[J].par\
entNode?G[J].par\
entNode.removeCh\
ild(G[J]):G[J])}\
else{if(G[J].nod\
eType===1){G.spl\
ice.apply(G,[J+1\
,0].concat(o.mak\
eArray(G[J].getE\
lementsByTagName\
(\x22script\x22))))}I.\
appendChild(G[J]\
)}}return E}retu\
rn G},attr:funct\
ion(J,G,K){if(!J\
||J.nodeType==3|\
|J.nodeType==8){\
return g}var H=!\
o.isXMLDoc(J),L=\
K!==g;G=H&&o.pro\
ps[G]||G;if(J.ta\
gName){var F=/hr\
ef|src|style/.te\
st(G);if(G==\x22sel\
ected\x22&&J.parent\
Node){J.parentNo\
de.selectedIndex\
}if(G in J&&H&&!\
F){if(L){if(G==\x22\
type\x22&&o.nodeNam\
e(J,\x22input\x22)&&J.\
parentNode){thro\
w\x22type property \
can't be changed\
\x22}J[G]=K}if(o.no\
deName(J,\x22form\x22)\
&&J.getAttribute\
Node(G)){return \
J.getAttributeNo\
de(G).nodeValue}\
if(G==\x22tabIndex\x22\
){var I=J.getAtt\
ributeNode(\x22tabI\
ndex\x22);return I&\
&I.specified?I.v\
alue:J.nodeName.\
match(/(button|i\
nput|object|sele\
ct|textarea)/i)?\
0:J.nodeName.mat\
ch(/^(a|area)$/i\
)&&J.href?0:g}re\
turn J[G]}if(!o.\
support.style&&H\
&&G==\x22style\x22){re\
turn o.attr(J.st\
yle,\x22cssText\x22,K)\
}if(L){J.setAttr\
ibute(G,\x22\x22+K)}va\
r E=!o.support.h\
refNormalized&&H\
&&F?J.getAttribu\
te(G,2):J.getAtt\
ribute(G);return\
 E===null?g:E}if\
(!o.support.opac\
ity&&G==\x22opacity\
\x22){if(L){J.zoom=\
1;J.filter=(J.fi\
lter||\x22\x22).replac\
e(/alpha\x5c([^)]*\x5c\
)/,\x22\x22)+(parseInt\
(K)+\x22\x22==\x22NaN\x22?\x22\x22\
:\x22alpha(opacity=\
\x22+K*100+\x22)\x22)}ret\
urn J.filter&&J.\
filter.indexOf(\x22\
opacity=\x22)>=0?(p\
arseFloat(J.filt\
er.match(/opacit\
y=([^)]*)/)[1])/\
100)+\x22\x22:\x22\x22}G=G.r\
eplace(/-([a-z])\
/ig,function(M,N\
){return N.toUpp\
erCase()});if(L)\
{J[G]=K}return J\
[G]},trim:functi\
on(E){return(E||\
\x22\x22).replace(/^\x5cs\
+|\x5cs+$/g,\x22\x22)},ma\
keArray:function\
(G){var E=[];if(\
G!=null){var F=G\
.length;if(F==nu\
ll||typeof G===\x22\
string\x22||o.isFun\
ction(G)||G.setI\
nterval){E[0]=G}\
else{while(F){E[\
--F]=G[F]}}}retu\
rn E},inArray:fu\
nction(G,H){for(\
var E=0,F=H.leng\
th;E<F;E++){if(H\
[E]===G){return \
E}}return -1},me\
rge:function(H,E\
){var F=0,G,I=H.\
length;if(!o.sup\
port.getAll){whi\
le((G=E[F++])!=n\
ull){if(G.nodeTy\
pe!=8){H[I++]=G}\
}}else{while((G=\
E[F++])!=null){H\
[I++]=G}}return \
H},unique:functi\
on(K){var F=[],E\
={};try{for(var \
G=0,H=K.length;G\
<H;G++){var J=o.\
data(K[G]);if(!E\
[J]){E[J]=true;F\
.push(K[G])}}}ca\
tch(I){F=K}retur\
n F},grep:functi\
on(F,J,E){var G=\
[];for(var H=0,I\
=F.length;H<I;H+\
+){if(!E!=!J(F[H\
],H)){G.push(F[H\
])}}return G},ma\
p:function(E,J){\
var F=[];for(var\
 G=0,H=E.length;\
G<H;G++){var I=J\
(E[G],G);if(I!=n\
ull){F[F.length]\
=I}}return F.con\
cat.apply([],F)}\
});var C=navigat\
or.userAgent.toL\
owerCase();o.bro\
wser={version:(C\
.match(/.+(?:rv|\
it|ra|ie)[\x5c/: ](\
[\x5cd.]+)/)||[0,\x220\
\x22])[1],safari:/w\
ebkit/.test(C),o\
pera:/opera/.tes\
t(C),msie:/msie/\
.test(C)&&!/oper\
a/.test(C),mozil\
la:/mozilla/.tes\
t(C)&&!/(compati\
ble|webkit)/.tes\
t(C)};o.each({pa\
rent:function(E)\
{return E.parent\
Node},parents:fu\
nction(E){return\
 o.dir(E,\x22parent\
Node\x22)},next:fun\
ction(E){return \
o.nth(E,2,\x22nextS\
ibling\x22)},prev:f\
unction(E){retur\
n o.nth(E,2,\x22pre\
viousSibling\x22)},\
nextAll:function\
(E){return o.dir\
(E,\x22nextSibling\x22\
)},prevAll:funct\
ion(E){return o.\
dir(E,\x22previousS\
ibling\x22)},siblin\
gs:function(E){r\
eturn o.sibling(\
E.parentNode.fir\
stChild,E)},chil\
dren:function(E)\
{return o.siblin\
g(E.firstChild)}\
,contents:functi\
on(E){return o.n\
odeName(E,\x22ifram\
e\x22)?E.contentDoc\
ument||E.content\
Window.document:\
o.makeArray(E.ch\
ildNodes)}},func\
tion(E,F){o.fn[E\
]=function(G){va\
r H=o.map(this,F\
);if(G&&typeof G\
==\x22string\x22){H=o.\
multiFilter(G,H)\
}return this.pus\
hStack(o.unique(\
H),E,G)}});o.eac\
h({appendTo:\x22app\
end\x22,prependTo:\x22\
prepend\x22,insertB\
efore:\x22before\x22,i\
nsertAfter:\x22afte\
r\x22,replaceAll:\x22r\
eplaceWith\x22},fun\
ction(E,F){o.fn[\
E]=function(G){v\
ar J=[],L=o(G);f\
or(var K=0,H=L.l\
ength;K<H;K++){v\
ar I=(K>0?this.c\
lone(true):this)\
.get();o.fn[F].a\
pply(o(L[K]),I);\
J=J.concat(I)}re\
turn this.pushSt\
ack(J,E,G)}});o.\
each({removeAttr\
:function(E){o.a\
ttr(this,E,\x22\x22);i\
f(this.nodeType=\
=1){this.removeA\
ttribute(E)}},ad\
dClass:function(\
E){o.className.a\
dd(this,E)},remo\
veClass:function\
(E){o.className.\
remove(this,E)},\
toggleClass:func\
tion(F,E){if(typ\
eof E!==\x22boolean\
\x22){E=!o.classNam\
e.has(this,F)}o.\
className[E?\x22add\
\x22:\x22remove\x22](this\
,F)},remove:func\
tion(E){if(!E||o\
.filter(E,[this]\
).length){o(\x22*\x22,\
this).add([this]\
).each(function(\
){o.event.remove\
(this);o.removeD\
ata(this)});if(t\
his.parentNode){\
this.parentNode.\
removeChild(this\
)}}},empty:funct\
ion(){o(this).ch\
ildren().remove(\
);while(this.fir\
stChild){this.re\
moveChild(this.f\
irstChild)}}},fu\
nction(E,F){o.fn\
[E]=function(){r\
eturn this.each(\
F,arguments)}});\
function j(E,F){\
return E[0]&&par\
seInt(o.curCSS(E\
[0],F,true),10)|\
|0}var h=\x22jQuery\
\x22+e(),v=0,A={};o\
.extend({cache:{\
},data:function(\
F,E,G){F=F==l?A:\
F;var H=F[h];if(\
!H){H=F[h]=++v}i\
f(E&&!o.cache[H]\
){o.cache[H]={}}\
if(G!==g){o.cach\
e[H][E]=G}return\
 E?o.cache[H][E]\
:H},removeData:f\
unction(F,E){F=F\
==l?A:F;var H=F[\
h];if(E){if(o.ca\
che[H]){delete o\
.cache[H][E];E=\x22\
\x22;for(E in o.cac\
he[H]){break}if(\
!E){o.removeData\
(F)}}}else{try{d\
elete F[h]}catch\
(G){if(F.removeA\
ttribute){F.remo\
veAttribute(h)}}\
delete o.cache[H\
]}},queue:functi\
on(F,E,H){if(F){\
E=(E||\x22fx\x22)+\x22que\
ue\x22;var G=o.data\
(F,E);if(!G||o.i\
sArray(H)){G=o.d\
ata(F,E,o.makeAr\
ray(H))}else{if(\
H){G.push(H)}}}r\
eturn G},dequeue\
:function(H,G){v\
ar E=o.queue(H,G\
),F=E.shift();if\
(!G||G===\x22fx\x22){F\
=E[0]}if(F!==g){\
F.call(H)}}});o.\
fn.extend({data:\
function(E,G){va\
r H=E.split(\x22.\x22)\
;H[1]=H[1]?\x22.\x22+H\
[1]:\x22\x22;if(G===g)\
{var F=this.trig\
gerHandler(\x22getD\
ata\x22+H[1]+\x22!\x22,[H\
[0]]);if(F===g&&\
this.length){F=o\
.data(this[0],E)\
}return F===g&&H\
[1]?this.data(H[\
0]):F}else{retur\
n this.trigger(\x22\
setData\x22+H[1]+\x22!\
\x22,[H[0],G]).each\
(function(){o.da\
ta(this,E,G)})}}\
,removeData:func\
tion(E){return t\
his.each(functio\
n(){o.removeData\
(this,E)})},queu\
e:function(E,F){\
if(typeof E!==\x22s\
tring\x22){F=E;E=\x22f\
x\x22}if(F===g){ret\
urn o.queue(this\
[0],E)}return th\
is.each(function\
(){var G=o.queue\
(this,E,F);if(E=\
=\x22fx\x22&&G.length=\
=1){G[0].call(th\
is)}})},dequeue:\
function(E){retu\
rn this.each(fun\
ction(){o.dequeu\
e(this,E)})}});\x0d\
\x0a/*\x0d\x0a * Sizzle C\
SS Selector Engi\
ne - v0.9.3\x0d\x0a * \
 Copyright 2009,\
 The Dojo Founda\
tion\x0d\x0a *  Releas\
ed under the MIT\
, BSD, and GPL L\
icenses.\x0d\x0a *  Mo\
re information: \
http://sizzlejs.\
com/\x0d\x0a */\x0d\x0a(func\
tion(){var R=/((\
?:\x5c((?:\x5c([^()]+\x5c\
)|[^()]+)+\x5c)|\x5c[(\
?:\x5c[[^[\x5c]]*\x5c]|['\
\x22][^'\x22]*['\x22]|[^[\
\x5c]'\x22]+)+\x5c]|\x5c\x5c.|[\
^ >+~,(\x5c[\x5c\x5c]+)+|\
[>+~])(\x5cs*,\x5cs*)?\
/g,L=0,H=Object.\
prototype.toStri\
ng;var F=functio\
n(Y,U,ab,ac){ab=\
ab||[];U=U||docu\
ment;if(U.nodeTy\
pe!==1&&U.nodeTy\
pe!==9){return[]\
}if(!Y||typeof Y\
!==\x22string\x22){ret\
urn ab}var Z=[],\
W,af,ai,T,ad,V,X\
=true;R.lastInde\
x=0;while((W=R.e\
xec(Y))!==null){\
Z.push(W[1]);if(\
W[2]){V=RegExp.r\
ightContext;brea\
k}}if(Z.length>1\
&&M.exec(Y)){if(\
Z.length===2&&I.\
relative[Z[0]]){\
af=J(Z[0]+Z[1],U\
)}else{af=I.rela\
tive[Z[0]]?[U]:F\
(Z.shift(),U);wh\
ile(Z.length){Y=\
Z.shift();if(I.r\
elative[Y]){Y+=Z\
.shift()}af=J(Y,\
af)}}}else{var a\
e=ac?{expr:Z.pop\
(),set:E(ac)}:F.\
find(Z.pop(),Z.l\
ength===1&&U.par\
entNode?U.parent\
Node:U,Q(U));af=\
F.filter(ae.expr\
,ae.set);if(Z.le\
ngth>0){ai=E(af)\
}else{X=false}wh\
ile(Z.length){va\
r ah=Z.pop(),ag=\
ah;if(!I.relativ\
e[ah]){ah=\x22\x22}els\
e{ag=Z.pop()}if(\
ag==null){ag=U}I\
.relative[ah](ai\
,ag,Q(U))}}if(!a\
i){ai=af}if(!ai)\
{throw\x22Syntax er\
ror, unrecognize\
d expression: \x22+\
(ah||Y)}if(H.cal\
l(ai)===\x22[object\
 Array]\x22){if(!X)\
{ab.push.apply(a\
b,ai)}else{if(U.\
nodeType===1){fo\
r(var aa=0;ai[aa\
]!=null;aa++){if\
(ai[aa]&&(ai[aa]\
===true||ai[aa].\
nodeType===1&&K(\
U,ai[aa]))){ab.p\
ush(af[aa])}}}el\
se{for(var aa=0;\
ai[aa]!=null;aa+\
+){if(ai[aa]&&ai\
[aa].nodeType===\
1){ab.push(af[aa\
])}}}}}else{E(ai\
,ab)}if(V){F(V,U\
,ab,ac);if(G){ha\
sDuplicate=false\
;ab.sort(G);if(h\
asDuplicate){for\
(var aa=1;aa<ab.\
length;aa++){if(\
ab[aa]===ab[aa-1\
]){ab.splice(aa-\
-,1)}}}}}return \
ab};F.matches=fu\
nction(T,U){retu\
rn F(T,null,null\
,U)};F.find=func\
tion(aa,T,ab){va\
r Z,X;if(!aa){re\
turn[]}for(var W\
=0,V=I.order.len\
gth;W<V;W++){var\
 Y=I.order[W],X;\
if((X=I.match[Y]\
.exec(aa))){var \
U=RegExp.leftCon\
text;if(U.substr\
(U.length-1)!==\x22\
\x5c\x5c\x22){X[1]=(X[1]|\
|\x22\x22).replace(/\x5c\x5c\
/g,\x22\x22);Z=I.find[\
Y](X,T,ab);if(Z!\
=null){aa=aa.rep\
lace(I.match[Y],\
\x22\x22);break}}}}if(\
!Z){Z=T.getEleme\
ntsByTagName(\x22*\x22\
)}return{set:Z,e\
xpr:aa}};F.filte\
r=function(ad,ac\
,ag,W){var V=ad,\
ai=[],aa=ac,Y,T,\
Z=ac&&ac[0]&&Q(a\
c[0]);while(ad&&\
ac.length){for(v\
ar ab in I.filte\
r){if((Y=I.match\
[ab].exec(ad))!=\
null){var U=I.fi\
lter[ab],ah,af;T\
=false;if(aa==ai\
){ai=[]}if(I.pre\
Filter[ab]){Y=I.\
preFilter[ab](Y,\
aa,ag,ai,W,Z);if\
(!Y){T=ah=true}e\
lse{if(Y===true)\
{continue}}}if(Y\
){for(var X=0;(a\
f=aa[X])!=null;X\
++){if(af){ah=U(\
af,Y,X,aa);var a\
e=W^!!ah;if(ag&&\
ah!=null){if(ae)\
{T=true}else{aa[\
X]=false}}else{i\
f(ae){ai.push(af\
);T=true}}}}}if(\
ah!==g){if(!ag){\
aa=ai}ad=ad.repl\
ace(I.match[ab],\
\x22\x22);if(!T){retur\
n[]}break}}}if(a\
d==V){if(T==null\
){throw\x22Syntax e\
rror, unrecogniz\
ed expression: \x22\
+ad}else{break}}\
V=ad}return aa};\
var I=F.selector\
s={order:[\x22ID\x22,\x22\
NAME\x22,\x22TAG\x22],mat\
ch:{ID:/#((?:[\x5cw\
\x5cu00c0-\x5cuFFFF_-]\
|\x5c\x5c.)+)/,CLASS:/\
\x5c.((?:[\x5cw\x5cu00c0-\
\x5cuFFFF_-]|\x5c\x5c.)+)\
/,NAME:/\x5c[name=[\
'\x22]*((?:[\x5cw\x5cu00c\
0-\x5cuFFFF_-]|\x5c\x5c.)\
+)['\x22]*\x5c]/,ATTR:\
/\x5c[\x5cs*((?:[\x5cw\x5cu0\
0c0-\x5cuFFFF_-]|\x5c\x5c\
.)+)\x5cs*(?:(\x5cS?=)\
\x5cs*(['\x22]*)(.*?)\x5c\
3|)\x5cs*\x5c]/,TAG:/^\
((?:[\x5cw\x5cu00c0-\x5cu\
FFFF\x5c*_-]|\x5c\x5c.)+)\
/,CHILD:/:(only|\
nth|last|first)-\
child(?:\x5c((even|\
odd|[\x5cdn+-]*)\x5c))\
?/,POS:/:(nth|eq\
|gt|lt|first|las\
t|even|odd)(?:\x5c(\
(\x5cd*)\x5c))?(?=[^-]\
|$)/,PSEUDO:/:((\
?:[\x5cw\x5cu00c0-\x5cuFF\
FF_-]|\x5c\x5c.)+)(?:\x5c\
((['\x22]*)((?:\x5c([^\
\x5c)]+\x5c)|[^\x5c2\x5c(\x5c)]\
*)+)\x5c2\x5c))?/},att\
rMap:{\x22class\x22:\x22c\
lassName\x22,\x22for\x22:\
\x22htmlFor\x22},attrH\
andle:{href:func\
tion(T){return T\
.getAttribute(\x22h\
ref\x22)}},relative\
:{\x22+\x22:function(a\
a,T,Z){var X=typ\
eof T===\x22string\x22\
,ab=X&&!/\x5cW/.tes\
t(T),Y=X&&!ab;if\
(ab&&!Z){T=T.toU\
pperCase()}for(v\
ar W=0,V=aa.leng\
th,U;W<V;W++){if\
((U=aa[W])){whil\
e((U=U.previousS\
ibling)&&U.nodeT\
ype!==1){}aa[W]=\
Y||U&&U.nodeName\
===T?U||false:U=\
==T}}if(Y){F.fil\
ter(T,aa,true)}}\
,\x22>\x22:function(Z,\
U,aa){var X=type\
of U===\x22string\x22;\
if(X&&!/\x5cW/.test\
(U)){U=aa?U:U.to\
UpperCase();for(\
var V=0,T=Z.leng\
th;V<T;V++){var \
Y=Z[V];if(Y){var\
 W=Y.parentNode;\
Z[V]=W.nodeName=\
==U?W:false}}}el\
se{for(var V=0,T\
=Z.length;V<T;V+\
+){var Y=Z[V];if\
(Y){Z[V]=X?Y.par\
entNode:Y.parent\
Node===U}}if(X){\
F.filter(U,Z,tru\
e)}}},\x22\x22:functio\
n(W,U,Y){var V=L\
++,T=S;if(!U.mat\
ch(/\x5cW/)){var X=\
U=Y?U:U.toUpperC\
ase();T=P}T(\x22par\
entNode\x22,U,V,W,X\
,Y)},\x22~\x22:functio\
n(W,U,Y){var V=L\
++,T=S;if(typeof\
 U===\x22string\x22&&!\
U.match(/\x5cW/)){v\
ar X=U=Y?U:U.toU\
pperCase();T=P}T\
(\x22previousSiblin\
g\x22,U,V,W,X,Y)}},\
find:{ID:functio\
n(U,V,W){if(type\
of V.getElementB\
yId!==\x22undefined\
\x22&&!W){var T=V.g\
etElementById(U[\
1]);return T?[T]\
:[]}},NAME:funct\
ion(V,Y,Z){if(ty\
peof Y.getElemen\
tsByName!==\x22unde\
fined\x22){var U=[]\
,X=Y.getElements\
ByName(V[1]);for\
(var W=0,T=X.len\
gth;W<T;W++){if(\
X[W].getAttribut\
e(\x22name\x22)===V[1]\
){U.push(X[W])}}\
return U.length=\
==0?null:U}},TAG\
:function(T,U){r\
eturn U.getEleme\
ntsByTagName(T[1\
])}},preFilter:{\
CLASS:function(W\
,U,V,T,Z,aa){W=\x22\
 \x22+W[1].replace(\
/\x5c\x5c/g,\x22\x22)+\x22 \x22;if\
(aa){return W}fo\
r(var X=0,Y;(Y=U\
[X])!=null;X++){\
if(Y){if(Z^(Y.cl\
assName&&(\x22 \x22+Y.\
className+\x22 \x22).i\
ndexOf(W)>=0)){i\
f(!V){T.push(Y)}\
}else{if(V){U[X]\
=false}}}}return\
 false},ID:funct\
ion(T){return T[\
1].replace(/\x5c\x5c/g\
,\x22\x22)},TAG:functi\
on(U,T){for(var \
V=0;T[V]===false\
;V++){}return T[\
V]&&Q(T[V])?U[1]\
:U[1].toUpperCas\
e()},CHILD:funct\
ion(T){if(T[1]==\
\x22nth\x22){var U=/(-\
?)(\x5cd*)n((?:\x5c+|-\
)?\x5cd*)/.exec(T[2\
]==\x22even\x22&&\x222n\x22|\
|T[2]==\x22odd\x22&&\x222\
n+1\x22||!/\x5cD/.test\
(T[2])&&\x220n+\x22+T[\
2]||T[2]);T[2]=(\
U[1]+(U[2]||1))-\
0;T[3]=U[3]-0}T[\
0]=L++;return T}\
,ATTR:function(X\
,U,V,T,Y,Z){var \
W=X[1].replace(/\
\x5c\x5c/g,\x22\x22);if(!Z&&\
I.attrMap[W]){X[\
1]=I.attrMap[W]}\
if(X[2]===\x22~=\x22){\
X[4]=\x22 \x22+X[4]+\x22 \
\x22}return X},PSEU\
DO:function(X,U,\
V,T,Y){if(X[1]==\
=\x22not\x22){if(X[3].\
match(R).length>\
1||/^\x5cw/.test(X[\
3])){X[3]=F(X[3]\
,null,null,U)}el\
se{var W=F.filte\
r(X[3],U,V,true^\
Y);if(!V){T.push\
.apply(T,W)}retu\
rn false}}else{i\
f(I.match.POS.te\
st(X[0])||I.matc\
h.CHILD.test(X[0\
])){return true}\
}return X},POS:f\
unction(T){T.uns\
hift(true);retur\
n T}},filters:{e\
nabled:function(\
T){return T.disa\
bled===false&&T.\
type!==\x22hidden\x22}\
,disabled:functi\
on(T){return T.d\
isabled===true},\
checked:function\
(T){return T.che\
cked===true},sel\
ected:function(T\
){T.parentNode.s\
electedIndex;ret\
urn T.selected==\
=true},parent:fu\
nction(T){return\
 !!T.firstChild}\
,empty:function(\
T){return !T.fir\
stChild},has:fun\
ction(V,U,T){ret\
urn !!F(T[3],V).\
length},header:f\
unction(T){retur\
n/h\x5cd/i.test(T.n\
odeName)},text:f\
unction(T){retur\
n\x22text\x22===T.type\
},radio:function\
(T){return\x22radio\
\x22===T.type},chec\
kbox:function(T)\
{return\x22checkbox\
\x22===T.type},file\
:function(T){ret\
urn\x22file\x22===T.ty\
pe},password:fun\
ction(T){return\x22\
password\x22===T.ty\
pe},submit:funct\
ion(T){return\x22su\
bmit\x22===T.type},\
image:function(T\
){return\x22image\x22=\
==T.type},reset:\
function(T){retu\
rn\x22reset\x22===T.ty\
pe},button:funct\
ion(T){return\x22bu\
tton\x22===T.type||\
T.nodeName.toUpp\
erCase()===\x22BUTT\
ON\x22},input:funct\
ion(T){return/in\
put|select|texta\
rea|button/i.tes\
t(T.nodeName)}},\
setFilters:{firs\
t:function(U,T){\
return T===0},la\
st:function(V,U,\
T,W){return U===\
W.length-1},even\
:function(U,T){r\
eturn T%2===0},o\
dd:function(U,T)\
{return T%2===1}\
,lt:function(V,U\
,T){return U<T[3\
]-0},gt:function\
(V,U,T){return U\
>T[3]-0},nth:fun\
ction(V,U,T){ret\
urn T[3]-0==U},e\
q:function(V,U,T\
){return T[3]-0=\
=U}},filter:{PSE\
UDO:function(Z,V\
,W,aa){var U=V[1\
],X=I.filters[U]\
;if(X){return X(\
Z,W,V,aa)}else{i\
f(U===\x22contains\x22\
){return(Z.textC\
ontent||Z.innerT\
ext||\x22\x22).indexOf\
(V[3])>=0}else{i\
f(U===\x22not\x22){var\
 Y=V[3];for(var \
W=0,T=Y.length;W\
<T;W++){if(Y[W]=\
==Z){return fals\
e}}return true}}\
}},CHILD:functio\
n(T,W){var Z=W[1\
],U=T;switch(Z){\
case\x22only\x22:case\x22\
first\x22:while(U=U\
.previousSibling\
){if(U.nodeType=\
==1){return fals\
e}}if(Z==\x22first\x22\
){return true}U=\
T;case\x22last\x22:whi\
le(U=U.nextSibli\
ng){if(U.nodeTyp\
e===1){return fa\
lse}}return true\
;case\x22nth\x22:var V\
=W[2],ac=W[3];if\
(V==1&&ac==0){re\
turn true}var Y=\
W[0],ab=T.parent\
Node;if(ab&&(ab.\
sizcache!==Y||!T\
.nodeIndex)){var\
 X=0;for(U=ab.fi\
rstChild;U;U=U.n\
extSibling){if(U\
.nodeType===1){U\
.nodeIndex=++X}}\
ab.sizcache=Y}va\
r aa=T.nodeIndex\
-ac;if(V==0){ret\
urn aa==0}else{r\
eturn(aa%V==0&&a\
a/V>=0)}}},ID:fu\
nction(U,T){retu\
rn U.nodeType===\
1&&U.getAttribut\
e(\x22id\x22)===T},TAG\
:function(U,T){r\
eturn(T===\x22*\x22&&U\
.nodeType===1)||\
U.nodeName===T},\
CLASS:function(U\
,T){return(\x22 \x22+(\
U.className||U.g\
etAttribute(\x22cla\
ss\x22))+\x22 \x22).index\
Of(T)>-1},ATTR:f\
unction(Y,W){var\
 V=W[1],T=I.attr\
Handle[V]?I.attr\
Handle[V](Y):Y[V\
]!=null?Y[V]:Y.g\
etAttribute(V),Z\
=T+\x22\x22,X=W[2],U=W\
[4];return T==nu\
ll?X===\x22!=\x22:X===\
\x22=\x22?Z===U:X===\x22*\
=\x22?Z.indexOf(U)>\
=0:X===\x22~=\x22?(\x22 \x22\
+Z+\x22 \x22).indexOf(\
U)>=0:!U?Z&&T!==\
false:X===\x22!=\x22?Z\
!=U:X===\x22^=\x22?Z.i\
ndexOf(U)===0:X=\
==\x22$=\x22?Z.substr(\
Z.length-U.lengt\
h)===U:X===\x22|=\x22?\
Z===U||Z.substr(\
0,U.length+1)===\
U+\x22-\x22:false},POS\
:function(X,U,V,\
Y){var T=U[2],W=\
I.setFilters[T];\
if(W){return W(X\
,V,U,Y)}}}};var \
M=I.match.POS;fo\
r(var O in I.mat\
ch){I.match[O]=R\
egExp(I.match[O]\
.source+/(?![^\x5c[\
]*\x5c])(?![^\x5c(]*\x5c)\
)/.source)}var E\
=function(U,T){U\
=Array.prototype\
.slice.call(U);i\
f(T){T.push.appl\
y(T,U);return T}\
return U};try{Ar\
ray.prototype.sl\
ice.call(documen\
t.documentElemen\
t.childNodes)}ca\
tch(N){E=functio\
n(X,W){var U=W||\
[];if(H.call(X)=\
==\x22[object Array\
]\x22){Array.protot\
ype.push.apply(U\
,X)}else{if(type\
of X.length===\x22n\
umber\x22){for(var \
V=0,T=X.length;V\
<T;V++){U.push(X\
[V])}}else{for(v\
ar V=0;X[V];V++)\
{U.push(X[V])}}}\
return U}}var G;\
if(document.docu\
mentElement.comp\
areDocumentPosit\
ion){G=function(\
U,T){var V=U.com\
pareDocumentPosi\
tion(T)&4?-1:U==\
=T?0:1;if(V===0)\
{hasDuplicate=tr\
ue}return V}}els\
e{if(\x22sourceInde\
x\x22 in document.d\
ocumentElement){\
G=function(U,T){\
var V=U.sourceIn\
dex-T.sourceInde\
x;if(V===0){hasD\
uplicate=true}re\
turn V}}else{if(\
document.createR\
ange){G=function\
(W,U){var V=W.ow\
nerDocument.crea\
teRange(),T=U.ow\
nerDocument.crea\
teRange();V.sele\
ctNode(W);V.coll\
apse(true);T.sel\
ectNode(U);T.col\
lapse(true);var \
X=V.compareBound\
aryPoints(Range.\
START_TO_END,T);\
if(X===0){hasDup\
licate=true}retu\
rn X}}}}(functio\
n(){var U=docume\
nt.createElement\
(\x22form\x22),V=\x22scri\
pt\x22+(new Date).g\
etTime();U.inner\
HTML=\x22<input nam\
e='\x22+V+\x22'/>\x22;var\
 T=document.docu\
mentElement;T.in\
sertBefore(U,T.f\
irstChild);if(!!\
document.getElem\
entById(V)){I.fi\
nd.ID=function(X\
,Y,Z){if(typeof \
Y.getElementById\
!==\x22undefined\x22&&\
!Z){var W=Y.getE\
lementById(X[1])\
;return W?W.id==\
=X[1]||typeof W.\
getAttributeNode\
!==\x22undefined\x22&&\
W.getAttributeNo\
de(\x22id\x22).nodeVal\
ue===X[1]?[W]:g:\
[]}};I.filter.ID\
=function(Y,W){v\
ar X=typeof Y.ge\
tAttributeNode!=\
=\x22undefined\x22&&Y.\
getAttributeNode\
(\x22id\x22);return Y.\
nodeType===1&&X&\
&X.nodeValue===W\
}}T.removeChild(\
U)})();(function\
(){var T=documen\
t.createElement(\
\x22div\x22);T.appendC\
hild(document.cr\
eateComment(\x22\x22))\
;if(T.getElement\
sByTagName(\x22*\x22).\
length>0){I.find\
.TAG=function(U,\
Y){var X=Y.getEl\
ementsByTagName(\
U[1]);if(U[1]===\
\x22*\x22){var W=[];fo\
r(var V=0;X[V];V\
++){if(X[V].node\
Type===1){W.push\
(X[V])}}X=W}retu\
rn X}}T.innerHTM\
L=\x22<a href='#'><\
/a>\x22;if(T.firstC\
hild&&typeof T.f\
irstChild.getAtt\
ribute!==\x22undefi\
ned\x22&&T.firstChi\
ld.getAttribute(\
\x22href\x22)!==\x22#\x22){I\
.attrHandle.href\
=function(U){ret\
urn U.getAttribu\
te(\x22href\x22,2)}}})\
();if(document.q\
uerySelectorAll)\
{(function(){var\
 T=F,U=document.\
createElement(\x22d\
iv\x22);U.innerHTML\
=\x22<p class='TEST\
'></p>\x22;if(U.que\
rySelectorAll&&U\
.querySelectorAl\
l(\x22.TEST\x22).lengt\
h===0){return}F=\
function(Y,X,V,W\
){X=X||document;\
if(!W&&X.nodeTyp\
e===9&&!Q(X)){tr\
y{return E(X.que\
rySelectorAll(Y)\
,V)}catch(Z){}}r\
eturn T(Y,X,V,W)\
};F.find=T.find;\
F.filter=T.filte\
r;F.selectors=T.\
selectors;F.matc\
hes=T.matches})(\
)}if(document.ge\
tElementsByClass\
Name&&document.d\
ocumentElement.g\
etElementsByClas\
sName){(function\
(){var T=documen\
t.createElement(\
\x22div\x22);T.innerHT\
ML=\x22<div class='\
test e'></div><d\
iv class='test'>\
</div>\x22;if(T.get\
ElementsByClassN\
ame(\x22e\x22).length=\
==0){return}T.la\
stChild.classNam\
e=\x22e\x22;if(T.getEl\
ementsByClassNam\
e(\x22e\x22).length===\
1){return}I.orde\
r.splice(1,0,\x22CL\
ASS\x22);I.find.CLA\
SS=function(U,V,\
W){if(typeof V.g\
etElementsByClas\
sName!==\x22undefin\
ed\x22&&!W){return \
V.getElementsByC\
lassName(U[1])}}\
})()}function P(\
U,Z,Y,ad,aa,ac){\
var ab=U==\x22previ\
ousSibling\x22&&!ac\
;for(var W=0,V=a\
d.length;W<V;W++\
){var T=ad[W];if\
(T){if(ab&&T.nod\
eType===1){T.siz\
cache=Y;T.sizset\
=W}T=T[U];var X=\
false;while(T){i\
f(T.sizcache===Y\
){X=ad[T.sizset]\
;break}if(T.node\
Type===1&&!ac){T\
.sizcache=Y;T.si\
zset=W}if(T.node\
Name===Z){X=T;br\
eak}T=T[U]}ad[W]\
=X}}}function S(\
U,Z,Y,ad,aa,ac){\
var ab=U==\x22previ\
ousSibling\x22&&!ac\
;for(var W=0,V=a\
d.length;W<V;W++\
){var T=ad[W];if\
(T){if(ab&&T.nod\
eType===1){T.siz\
cache=Y;T.sizset\
=W}T=T[U];var X=\
false;while(T){i\
f(T.sizcache===Y\
){X=ad[T.sizset]\
;break}if(T.node\
Type===1){if(!ac\
){T.sizcache=Y;T\
.sizset=W}if(typ\
eof Z!==\x22string\x22\
){if(T===Z){X=tr\
ue;break}}else{i\
f(F.filter(Z,[T]\
).length>0){X=T;\
break}}}T=T[U]}a\
d[W]=X}}}var K=d\
ocument.compareD\
ocumentPosition?\
function(U,T){re\
turn U.compareDo\
cumentPosition(T\
)&16}:function(U\
,T){return U!==T\
&&(U.contains?U.\
contains(T):true\
)};var Q=functio\
n(T){return T.no\
deType===9&&T.do\
cumentElement.no\
deName!==\x22HTML\x22|\
|!!T.ownerDocume\
nt&&Q(T.ownerDoc\
ument)};var J=fu\
nction(T,aa){var\
 W=[],X=\x22\x22,Y,V=a\
a.nodeType?[aa]:\
aa;while((Y=I.ma\
tch.PSEUDO.exec(\
T))){X+=Y[0];T=T\
.replace(I.match\
.PSEUDO,\x22\x22)}T=I.\
relative[T]?T+\x22*\
\x22:T;for(var Z=0,\
U=V.length;Z<U;Z\
++){F(T,V[Z],W)}\
return F.filter(\
X,W)};o.find=F;o\
.filter=F.filter\
;o.expr=F.select\
ors;o.expr[\x22:\x22]=\
o.expr.filters;F\
.selectors.filte\
rs.hidden=functi\
on(T){return T.o\
ffsetWidth===0||\
T.offsetHeight==\
=0};F.selectors.\
filters.visible=\
function(T){retu\
rn T.offsetWidth\
>0||T.offsetHeig\
ht>0};F.selector\
s.filters.animat\
ed=function(T){r\
eturn o.grep(o.t\
imers,function(U\
){return T===U.e\
lem}).length};o.\
multiFilter=func\
tion(V,T,U){if(U\
){V=\x22:not(\x22+V+\x22)\
\x22}return F.match\
es(V,T)};o.dir=f\
unction(V,U){var\
 T=[],W=V[U];whi\
le(W&&W!=documen\
t){if(W.nodeType\
==1){T.push(W)}W\
=W[U]}return T};\
o.nth=function(X\
,T,V,W){T=T||1;v\
ar U=0;for(;X;X=\
X[V]){if(X.nodeT\
ype==1&&++U==T){\
break}}return X}\
;o.sibling=funct\
ion(V,U){var T=[\
];for(;V;V=V.nex\
tSibling){if(V.n\
odeType==1&&V!=U\
){T.push(V)}}ret\
urn T};return;l.\
Sizzle=F})();o.e\
vent={add:functi\
on(I,F,H,K){if(I\
.nodeType==3||I.\
nodeType==8){ret\
urn}if(I.setInte\
rval&&I!=l){I=l}\
if(!H.guid){H.gu\
id=this.guid++}i\
f(K!==g){var G=H\
;H=this.proxy(G)\
;H.data=K}var E=\
o.data(I,\x22events\
\x22)||o.data(I,\x22ev\
ents\x22,{}),J=o.da\
ta(I,\x22handle\x22)||\
o.data(I,\x22handle\
\x22,function(){ret\
urn typeof o!==\x22\
undefined\x22&&!o.e\
vent.triggered?o\
.event.handle.ap\
ply(arguments.ca\
llee.elem,argume\
nts):g});J.elem=\
I;o.each(F.split\
(/\x5cs+/),function\
(M,N){var O=N.sp\
lit(\x22.\x22);N=O.shi\
ft();H.type=O.sl\
ice().sort().joi\
n(\x22.\x22);var L=E[N\
];if(o.event.spe\
cialAll[N]){o.ev\
ent.specialAll[N\
].setup.call(I,K\
,O)}if(!L){L=E[N\
]={};if(!o.event\
.special[N]||o.e\
vent.special[N].\
setup.call(I,K,O\
)===false){if(I.\
addEventListener\
){I.addEventList\
ener(N,J,false)}\
else{if(I.attach\
Event){I.attachE\
vent(\x22on\x22+N,J)}}\
}}L[H.guid]=H;o.\
event.global[N]=\
true});I=null},g\
uid:1,global:{},\
remove:function(\
K,H,J){if(K.node\
Type==3||K.nodeT\
ype==8){return}v\
ar G=o.data(K,\x22e\
vents\x22),F,E;if(G\
){if(H===g||(typ\
eof H===\x22string\x22\
&&H.charAt(0)==\x22\
.\x22)){for(var I i\
n G){this.remove\
(K,I+(H||\x22\x22))}}e\
lse{if(H.type){J\
=H.handler;H=H.t\
ype}o.each(H.spl\
it(/\x5cs+/),functi\
on(M,O){var Q=O.\
split(\x22.\x22);O=Q.s\
hift();var N=Reg\
Exp(\x22(^|\x5c\x5c.)\x22+Q.\
slice().sort().j\
oin(\x22.*\x5c\x5c.\x22)+\x22(\x5c\
\x5c.|$)\x22);if(G[O])\
{if(J){delete G[\
O][J.guid]}else{\
for(var P in G[O\
]){if(N.test(G[O\
][P].type)){dele\
te G[O][P]}}}if(\
o.event.specialA\
ll[O]){o.event.s\
pecialAll[O].tea\
rdown.call(K,Q)}\
for(F in G[O]){b\
reak}if(!F){if(!\
o.event.special[\
O]||o.event.spec\
ial[O].teardown.\
call(K,Q)===fals\
e){if(K.removeEv\
entListener){K.r\
emoveEventListen\
er(O,o.data(K,\x22h\
andle\x22),false)}e\
lse{if(K.detachE\
vent){K.detachEv\
ent(\x22on\x22+O,o.dat\
a(K,\x22handle\x22))}}\
}F=null;delete G\
[O]}}})}for(F in\
 G){break}if(!F)\
{var L=o.data(K,\
\x22handle\x22);if(L){\
L.elem=null}o.re\
moveData(K,\x22even\
ts\x22);o.removeDat\
a(K,\x22handle\x22)}}}\
,trigger:functio\
n(I,K,H,E){var G\
=I.type||I;if(!E\
){I=typeof I===\x22\
object\x22?I[h]?I:o\
.extend(o.Event(\
G),I):o.Event(G)\
;if(G.indexOf(\x22!\
\x22)>=0){I.type=G=\
G.slice(0,-1);I.\
exclusive=true}i\
f(!H){I.stopProp\
agation();if(thi\
s.global[G]){o.e\
ach(o.cache,func\
tion(){if(this.e\
vents&&this.even\
ts[G]){o.event.t\
rigger(I,K,this.\
handle.elem)}})}\
}if(!H||H.nodeTy\
pe==3||H.nodeTyp\
e==8){return g}I\
.result=g;I.targ\
et=H;K=o.makeArr\
ay(K);K.unshift(\
I)}I.currentTarg\
et=H;var J=o.dat\
a(H,\x22handle\x22);if\
(J){J.apply(H,K)\
}if((!H[G]||(o.n\
odeName(H,\x22a\x22)&&\
G==\x22click\x22))&&H[\
\x22on\x22+G]&&H[\x22on\x22+\
G].apply(H,K)===\
false){I.result=\
false}if(!E&&H[G\
]&&!I.isDefaultP\
revented()&&!(o.\
nodeName(H,\x22a\x22)&\
&G==\x22click\x22)){th\
is.triggered=tru\
e;try{H[G]()}cat\
ch(L){}}this.tri\
ggered=false;if(\
!I.isPropagation\
Stopped()){var F\
=H.parentNode||H\
.ownerDocument;i\
f(F){o.event.tri\
gger(I,K,F,true)\
}}},handle:funct\
ion(K){var J,E;K\
=arguments[0]=o.\
event.fix(K||l.e\
vent);K.currentT\
arget=this;var L\
=K.type.split(\x22.\
\x22);K.type=L.shif\
t();J=!L.length&\
&!K.exclusive;va\
r I=RegExp(\x22(^|\x5c\
\x5c.)\x22+L.slice().s\
ort().join(\x22.*\x5c\x5c\
.\x22)+\x22(\x5c\x5c.|$)\x22);E\
=(o.data(this,\x22e\
vents\x22)||{})[K.t\
ype];for(var G i\
n E){var H=E[G];\
if(J||I.test(H.t\
ype)){K.handler=\
H;K.data=H.data;\
var F=H.apply(th\
is,arguments);if\
(F!==g){K.result\
=F;if(F===false)\
{K.preventDefaul\
t();K.stopPropag\
ation()}}if(K.is\
ImmediatePropaga\
tionStopped()){b\
reak}}}},props:\x22\
altKey attrChang\
e attrName bubbl\
es button cancel\
able charCode cl\
ientX clientY ct\
rlKey currentTar\
get data detail \
eventPhase fromE\
lement handler k\
eyCode metaKey n\
ewValue original\
Target pageX pag\
eY prevValue rel\
atedNode related\
Target screenX s\
creenY shiftKey \
srcElement targe\
t toElement view\
 wheelDelta whic\
h\x22.split(\x22 \x22),fi\
x:function(H){if\
(H[h]){return H}\
var F=H;H=o.Even\
t(F);for(var G=t\
his.props.length\
,J;G;){J=this.pr\
ops[--G];H[J]=F[\
J]}if(!H.target)\
{H.target=H.srcE\
lement||document\
}if(H.target.nod\
eType==3){H.targ\
et=H.target.pare\
ntNode}if(!H.rel\
atedTarget&&H.fr\
omElement){H.rel\
atedTarget=H.fro\
mElement==H.targ\
et?H.toElement:H\
.fromElement}if(\
H.pageX==null&&H\
.clientX!=null){\
var I=document.d\
ocumentElement,E\
=document.body;H\
.pageX=H.clientX\
+(I&&I.scrollLef\
t||E&&E.scrollLe\
ft||0)-(I.client\
Left||0);H.pageY\
=H.clientY+(I&&I\
.scrollTop||E&&E\
.scrollTop||0)-(\
I.clientTop||0)}\
if(!H.which&&((H\
.charCode||H.cha\
rCode===0)?H.cha\
rCode:H.keyCode)\
){H.which=H.char\
Code||H.keyCode}\
if(!H.metaKey&&H\
.ctrlKey){H.meta\
Key=H.ctrlKey}if\
(!H.which&&H.but\
ton){H.which=(H.\
button&1?1:(H.bu\
tton&2?3:(H.butt\
on&4?2:0)))}retu\
rn H},proxy:func\
tion(F,E){E=E||f\
unction(){return\
 F.apply(this,ar\
guments)};E.guid\
=F.guid=F.guid||\
E.guid||this.gui\
d++;return E},sp\
ecial:{ready:{se\
tup:B,teardown:f\
unction(){}}},sp\
ecialAll:{live:{\
setup:function(E\
,F){o.event.add(\
this,F[0],c)},te\
ardown:function(\
G){if(G.length){\
var E=0,F=RegExp\
(\x22(^|\x5c\x5c.)\x22+G[0]+\
\x22(\x5c\x5c.|$)\x22);o.eac\
h((o.data(this,\x22\
events\x22).live||{\
}),function(){if\
(F.test(this.typ\
e)){E++}});if(E<\
1){o.event.remov\
e(this,G[0],c)}}\
}}}};o.Event=fun\
ction(E){if(!thi\
s.preventDefault\
){return new o.E\
vent(E)}if(E&&E.\
type){this.origi\
nalEvent=E;this.\
type=E.type}else\
{this.type=E}thi\
s.timeStamp=e();\
this[h]=true};fu\
nction k(){retur\
n false}function\
 u(){return true\
}o.Event.prototy\
pe={preventDefau\
lt:function(){th\
is.isDefaultPrev\
ented=u;var E=th\
is.originalEvent\
;if(!E){return}i\
f(E.preventDefau\
lt){E.preventDef\
ault()}E.returnV\
alue=false},stop\
Propagation:func\
tion(){this.isPr\
opagationStopped\
=u;var E=this.or\
iginalEvent;if(!\
E){return}if(E.s\
topPropagation){\
E.stopPropagatio\
n()}E.cancelBubb\
le=true},stopImm\
ediatePropagatio\
n:function(){thi\
s.isImmediatePro\
pagationStopped=\
u;this.stopPropa\
gation()},isDefa\
ultPrevented:k,i\
sPropagationStop\
ped:k,isImmediat\
ePropagationStop\
ped:k};var a=fun\
ction(F){var E=F\
.relatedTarget;w\
hile(E&&E!=this)\
{try{E=E.parentN\
ode}catch(G){E=t\
his}}if(E!=this)\
{F.type=F.data;o\
.event.handle.ap\
ply(this,argumen\
ts)}};o.each({mo\
useover:\x22mouseen\
ter\x22,mouseout:\x22m\
ouseleave\x22},func\
tion(F,E){o.even\
t.special[E]={se\
tup:function(){o\
.event.add(this,\
F,a,E)},teardown\
:function(){o.ev\
ent.remove(this,\
F,a)}}});o.fn.ex\
tend({bind:funct\
ion(F,G,E){retur\
n F==\x22unload\x22?th\
is.one(F,G,E):th\
is.each(function\
(){o.event.add(t\
his,F,E||G,E&&G)\
})},one:function\
(G,H,F){var E=o.\
event.proxy(F||H\
,function(I){o(t\
his).unbind(I,E)\
;return(F||H).ap\
ply(this,argumen\
ts)});return thi\
s.each(function(\
){o.event.add(th\
is,G,E,F&&H)})},\
unbind:function(\
F,E){return this\
.each(function()\
{o.event.remove(\
this,F,E)})},tri\
gger:function(E,\
F){return this.e\
ach(function(){o\
.event.trigger(E\
,F,this)})},trig\
gerHandler:funct\
ion(E,G){if(this\
[0]){var F=o.Eve\
nt(E);F.preventD\
efault();F.stopP\
ropagation();o.e\
vent.trigger(F,G\
,this[0]);return\
 F.result}},togg\
le:function(G){v\
ar E=arguments,F\
=1;while(F<E.len\
gth){o.event.pro\
xy(G,E[F++])}ret\
urn this.click(o\
.event.proxy(G,f\
unction(H){this.\
lastToggle=(this\
.lastToggle||0)%\
F;H.preventDefau\
lt();return E[th\
is.lastToggle++]\
.apply(this,argu\
ments)||false}))\
},hover:function\
(E,F){return thi\
s.mouseenter(E).\
mouseleave(F)},r\
eady:function(E)\
{B();if(o.isRead\
y){E.call(docume\
nt,o)}else{o.rea\
dyList.push(E)}r\
eturn this},live\
:function(G,F){v\
ar E=o.event.pro\
xy(F);E.guid+=th\
is.selector+G;o(\
document).bind(i\
(G,this.selector\
),this.selector,\
E);return this},\
die:function(F,E\
){o(document).un\
bind(i(F,this.se\
lector),E?{guid:\
E.guid+this.sele\
ctor+F}:null);re\
turn this}});fun\
ction c(H){var E\
=RegExp(\x22(^|\x5c\x5c.)\
\x22+H.type+\x22(\x5c\x5c.|$\
)\x22),G=true,F=[];\
o.each(o.data(th\
is,\x22events\x22).liv\
e||[],function(I\
,J){if(E.test(J.\
type)){var K=o(H\
.target).closest\
(J.data)[0];if(K\
){F.push({elem:K\
,fn:J})}}});F.so\
rt(function(J,I)\
{return o.data(J\
.elem,\x22closest\x22)\
-o.data(I.elem,\x22\
closest\x22)});o.ea\
ch(F,function(){\
if(this.fn.call(\
this.elem,H,this\
.fn.data)===fals\
e){return(G=fals\
e)}});return G}f\
unction i(F,E){r\
eturn[\x22live\x22,F,E\
.replace(/\x5c./g,\x22\
`\x22).replace(/ /g\
,\x22|\x22)].join(\x22.\x22)\
}o.extend({isRea\
dy:false,readyLi\
st:[],ready:func\
tion(){if(!o.isR\
eady){o.isReady=\
true;if(o.readyL\
ist){o.each(o.re\
adyList,function\
(){this.call(doc\
ument,o)});o.rea\
dyList=null}o(do\
cument).triggerH\
andler(\x22ready\x22)}\
}});var x=false;\
function B(){if(\
x){return}x=true\
;if(document.add\
EventListener){d\
ocument.addEvent\
Listener(\x22DOMCon\
tentLoaded\x22,func\
tion(){document.\
removeEventListe\
ner(\x22DOMContentL\
oaded\x22,arguments\
.callee,false);o\
.ready()},false)\
}else{if(documen\
t.attachEvent){d\
ocument.attachEv\
ent(\x22onreadystat\
echange\x22,functio\
n(){if(document.\
readyState===\x22co\
mplete\x22){documen\
t.detachEvent(\x22o\
nreadystatechang\
e\x22,arguments.cal\
lee);o.ready()}}\
);if(document.do\
cumentElement.do\
Scroll&&l==l.top\
){(function(){if\
(o.isReady){retu\
rn}try{document.\
documentElement.\
doScroll(\x22left\x22)\
}catch(E){setTim\
eout(arguments.c\
allee,0);return}\
o.ready()})()}}}\
o.event.add(l,\x22l\
oad\x22,o.ready)}o.\
each((\x22blur,focu\
s,load,resize,sc\
roll,unload,clic\
k,dblclick,mouse\
down,mouseup,mou\
semove,mouseover\
,mouseout,mousee\
nter,mouseleave,\
change,select,su\
bmit,keydown,key\
press,keyup,erro\
r\x22).split(\x22,\x22),f\
unction(F,E){o.f\
n[E]=function(G)\
{return G?this.b\
ind(E,G):this.tr\
igger(E)}});o(l)\
.bind(\x22unload\x22,f\
unction(){for(va\
r E in o.cache){\
if(E!=1&&o.cache\
[E].handle){o.ev\
ent.remove(o.cac\
he[E].handle.ele\
m)}}});(function\
(){o.support={};\
var F=document.d\
ocumentElement,G\
=document.create\
Element(\x22script\x22\
),K=document.cre\
ateElement(\x22div\x22\
),J=\x22script\x22+(ne\
w Date).getTime(\
);K.style.displa\
y=\x22none\x22;K.inner\
HTML='   <link/>\
<table></table><\
a href=\x22/a\x22 styl\
e=\x22color:red;flo\
at:left;opacity:\
.5;\x22>a</a><selec\
t><option>text</\
option></select>\
<object><param/>\
</object>';var H\
=K.getElementsBy\
TagName(\x22*\x22),E=K\
.getElementsByTa\
gName(\x22a\x22)[0];if\
(!H||!H.length||\
!E){return}o.sup\
port={leadingWhi\
tespace:K.firstC\
hild.nodeType==3\
,tbody:!K.getEle\
mentsByTagName(\x22\
tbody\x22).length,o\
bjectAll:!!K.get\
ElementsByTagNam\
e(\x22object\x22)[0].g\
etElementsByTagN\
ame(\x22*\x22).length,\
htmlSerialize:!!\
K.getElementsByT\
agName(\x22link\x22).l\
ength,style:/red\
/.test(E.getAttr\
ibute(\x22style\x22)),\
hrefNormalized:E\
.getAttribute(\x22h\
ref\x22)===\x22/a\x22,opa\
city:E.style.opa\
city===\x220.5\x22,css\
Float:!!E.style.\
cssFloat,scriptE\
val:false,noClon\
eEvent:true,boxM\
odel:null};G.typ\
e=\x22text/javascri\
pt\x22;try{G.append\
Child(document.c\
reateTextNode(\x22w\
indow.\x22+J+\x22=1;\x22)\
)}catch(I){}F.in\
sertBefore(G,F.f\
irstChild);if(l[\
J]){o.support.sc\
riptEval=true;de\
lete l[J]}F.remo\
veChild(G);if(K.\
attachEvent&&K.f\
ireEvent){K.atta\
chEvent(\x22onclick\
\x22,function(){o.s\
upport.noCloneEv\
ent=false;K.deta\
chEvent(\x22onclick\
\x22,arguments.call\
ee)});K.cloneNod\
e(true).fireEven\
t(\x22onclick\x22)}o(f\
unction(){var L=\
document.createE\
lement(\x22div\x22);L.\
style.width=L.st\
yle.paddingLeft=\
\x221px\x22;document.b\
ody.appendChild(\
L);o.boxModel=o.\
support.boxModel\
=L.offsetWidth==\
=2;document.body\
.removeChild(L).\
style.display=\x22n\
one\x22})})();var w\
=o.support.cssFl\
oat?\x22cssFloat\x22:\x22\
styleFloat\x22;o.pr\
ops={\x22for\x22:\x22html\
For\x22,\x22class\x22:\x22cl\
assName\x22,\x22float\x22\
:w,cssFloat:w,st\
yleFloat:w,reado\
nly:\x22readOnly\x22,m\
axlength:\x22maxLen\
gth\x22,cellspacing\
:\x22cellSpacing\x22,r\
owspan:\x22rowSpan\x22\
,tabindex:\x22tabIn\
dex\x22};o.fn.exten\
d({_load:o.fn.lo\
ad,load:function\
(G,J,K){if(typeo\
f G!==\x22string\x22){\
return this._loa\
d(G)}var I=G.ind\
exOf(\x22 \x22);if(I>=\
0){var E=G.slice\
(I,G.length);G=G\
.slice(0,I)}var \
H=\x22GET\x22;if(J){if\
(o.isFunction(J)\
){K=J;J=null}els\
e{if(typeof J===\
\x22object\x22){J=o.pa\
ram(J);H=\x22POST\x22}\
}}var F=this;o.a\
jax({url:G,type:\
H,dataType:\x22html\
\x22,data:J,complet\
e:function(M,L){\
if(L==\x22success\x22|\
|L==\x22notmodified\
\x22){F.html(E?o(\x22<\
div/>\x22).append(M\
.responseText.re\
place(/<script(.\
|\x5cs)*?\x5c/script>/\
g,\x22\x22)).find(E):M\
.responseText)}i\
f(K){F.each(K,[M\
.responseText,L,\
M])}}});return t\
his},serialize:f\
unction(){return\
 o.param(this.se\
rializeArray())}\
,serializeArray:\
function(){retur\
n this.map(funct\
ion(){return thi\
s.elements?o.mak\
eArray(this.elem\
ents):this}).fil\
ter(function(){r\
eturn this.name&\
&!this.disabled&\
&(this.checked||\
/select|textarea\
/i.test(this.nod\
eName)||/text|hi\
dden|password|se\
arch/i.test(this\
.type))}).map(fu\
nction(E,F){var \
G=o(this).val();\
return G==null?n\
ull:o.isArray(G)\
?o.map(G,functio\
n(I,H){return{na\
me:F.name,value:\
I}}):{name:F.nam\
e,value:G}}).get\
()}});o.each(\x22aj\
axStart,ajaxStop\
,ajaxComplete,aj\
axError,ajaxSucc\
ess,ajaxSend\x22.sp\
lit(\x22,\x22),functio\
n(E,F){o.fn[F]=f\
unction(G){retur\
n this.bind(F,G)\
}});var r=e();o.\
extend({get:func\
tion(E,G,H,F){if\
(o.isFunction(G)\
){H=G;G=null}ret\
urn o.ajax({type\
:\x22GET\x22,url:E,dat\
a:G,success:H,da\
taType:F})},getS\
cript:function(E\
,F){return o.get\
(E,null,F,\x22scrip\
t\x22)},getJSON:fun\
ction(E,F,G){ret\
urn o.get(E,F,G,\
\x22json\x22)},post:fu\
nction(E,G,H,F){\
if(o.isFunction(\
G)){H=G;G={}}ret\
urn o.ajax({type\
:\x22POST\x22,url:E,da\
ta:G,success:H,d\
ataType:F})},aja\
xSetup:function(\
E){o.extend(o.aj\
axSettings,E)},a\
jaxSettings:{url\
:location.href,g\
lobal:true,type:\
\x22GET\x22,contentTyp\
e:\x22application/x\
-www-form-urlenc\
oded\x22,processDat\
a:true,async:tru\
e,xhr:function()\
{return l.Active\
XObject?new Acti\
veXObject(\x22Micro\
soft.XMLHTTP\x22):n\
ew XMLHttpReques\
t()},accepts:{xm\
l:\x22application/x\
ml, text/xml\x22,ht\
ml:\x22text/html\x22,s\
cript:\x22text/java\
script, applicat\
ion/javascript\x22,\
json:\x22applicatio\
n/json, text/jav\
ascript\x22,text:\x22t\
ext/plain\x22,_defa\
ult:\x22*/*\x22}},last\
Modified:{},ajax\
:function(M){M=o\
.extend(true,M,o\
.extend(true,{},\
o.ajaxSettings,M\
));var W,F=/=\x5c?(\
&|$)/g,R,V,G=M.t\
ype.toUpperCase(\
);if(M.data&&M.p\
rocessData&&type\
of M.data!==\x22str\
ing\x22){M.data=o.p\
aram(M.data)}if(\
M.dataType==\x22jso\
np\x22){if(G==\x22GET\x22\
){if(!M.url.matc\
h(F)){M.url+=(M.\
url.match(/\x5c?/)?\
\x22&\x22:\x22?\x22)+(M.json\
p||\x22callback\x22)+\x22\
=?\x22}}else{if(!M.\
data||!M.data.ma\
tch(F)){M.data=(\
M.data?M.data+\x22&\
\x22:\x22\x22)+(M.jsonp||\
\x22callback\x22)+\x22=?\x22\
}}M.dataType=\x22js\
on\x22}if(M.dataTyp\
e==\x22json\x22&&(M.da\
ta&&M.data.match\
(F)||M.url.match\
(F))){W=\x22jsonp\x22+\
r++;if(M.data){M\
.data=(M.data+\x22\x22\
).replace(F,\x22=\x22+\
W+\x22$1\x22)}M.url=M.\
url.replace(F,\x22=\
\x22+W+\x22$1\x22);M.data\
Type=\x22script\x22;l[\
W]=function(X){V\
=X;I();L();l[W]=\
g;try{delete l[W\
]}catch(Y){}if(H\
){H.removeChild(\
T)}}}if(M.dataTy\
pe==\x22script\x22&&M.\
cache==null){M.c\
ache=false}if(M.\
cache===false&&G\
==\x22GET\x22){var E=e\
();var U=M.url.r\
eplace(/(\x5c?|&)_=\
.*?(&|$)/,\x22$1_=\x22\
+E+\x22$2\x22);M.url=U\
+((U==M.url)?(M.\
url.match(/\x5c?/)?\
\x22&\x22:\x22?\x22)+\x22_=\x22+E:\
\x22\x22)}if(M.data&&G\
==\x22GET\x22){M.url+=\
(M.url.match(/\x5c?\
/)?\x22&\x22:\x22?\x22)+M.da\
ta;M.data=null}i\
f(M.global&&!o.a\
ctive++){o.event\
.trigger(\x22ajaxSt\
art\x22)}var Q=/^(\x5c\
w+:)?\x5c/\x5c/([^\x5c/?#\
]+)/.exec(M.url)\
;if(M.dataType==\
\x22script\x22&&G==\x22GE\
T\x22&&Q&&(Q[1]&&Q[\
1]!=location.pro\
tocol||Q[2]!=loc\
ation.host)){var\
 H=document.getE\
lementsByTagName\
(\x22head\x22)[0];var \
T=document.creat\
eElement(\x22script\
\x22);T.src=M.url;i\
f(M.scriptCharse\
t){T.charset=M.s\
criptCharset}if(\
!W){var O=false;\
T.onload=T.onrea\
dystatechange=fu\
nction(){if(!O&&\
(!this.readyStat\
e||this.readySta\
te==\x22loaded\x22||th\
is.readyState==\x22\
complete\x22)){O=tr\
ue;I();L();T.onl\
oad=T.onreadysta\
techange=null;H.\
removeChild(T)}}\
}H.appendChild(T\
);return g}var K\
=false;var J=M.x\
hr();if(M.userna\
me){J.open(G,M.u\
rl,M.async,M.use\
rname,M.password\
)}else{J.open(G,\
M.url,M.async)}t\
ry{if(M.data){J.\
setRequestHeader\
(\x22Content-Type\x22,\
M.contentType)}i\
f(M.ifModified){\
J.setRequestHead\
er(\x22If-Modified-\
Since\x22,o.lastMod\
ified[M.url]||\x22T\
hu, 01 Jan 1970 \
00:00:00 GMT\x22)}J\
.setRequestHeade\
r(\x22X-Requested-W\
ith\x22,\x22XMLHttpReq\
uest\x22);J.setRequ\
estHeader(\x22Accep\
t\x22,M.dataType&&M\
.accepts[M.dataT\
ype]?M.accepts[M\
.dataType]+\x22, */\
*\x22:M.accepts._de\
fault)}catch(S){\
}if(M.beforeSend\
&&M.beforeSend(J\
,M)===false){if(\
M.global&&!--o.a\
ctive){o.event.t\
rigger(\x22ajaxStop\
\x22)}J.abort();ret\
urn false}if(M.g\
lobal){o.event.t\
rigger(\x22ajaxSend\
\x22,[J,M])}var N=f\
unction(X){if(J.\
readyState==0){i\
f(P){clearInterv\
al(P);P=null;if(\
M.global&&!--o.a\
ctive){o.event.t\
rigger(\x22ajaxStop\
\x22)}}}else{if(!K&\
&J&&(J.readyStat\
e==4||X==\x22timeou\
t\x22)){K=true;if(P\
){clearInterval(\
P);P=null}R=X==\x22\
timeout\x22?\x22timeou\
t\x22:!o.httpSucces\
s(J)?\x22error\x22:M.i\
fModified&&o.htt\
pNotModified(J,M\
.url)?\x22notmodifi\
ed\x22:\x22success\x22;if\
(R==\x22success\x22){t\
ry{V=o.httpData(\
J,M.dataType,M)}\
catch(Z){R=\x22pars\
ererror\x22}}if(R==\
\x22success\x22){var Y\
;try{Y=J.getResp\
onseHeader(\x22Last\
-Modified\x22)}catc\
h(Z){}if(M.ifMod\
ified&&Y){o.last\
Modified[M.url]=\
Y}if(!W){I()}}el\
se{o.handleError\
(M,J,R)}L();if(X\
){J.abort()}if(M\
.async){J=null}}\
}};if(M.async){v\
ar P=setInterval\
(N,13);if(M.time\
out>0){setTimeou\
t(function(){if(\
J&&!K){N(\x22timeou\
t\x22)}},M.timeout)\
}}try{J.send(M.d\
ata)}catch(S){o.\
handleError(M,J,\
null,S)}if(!M.as\
ync){N()}functio\
n I(){if(M.succe\
ss){M.success(V,\
R)}if(M.global){\
o.event.trigger(\
\x22ajaxSuccess\x22,[J\
,M])}}function L\
(){if(M.complete\
){M.complete(J,R\
)}if(M.global){o\
.event.trigger(\x22\
ajaxComplete\x22,[J\
,M])}if(M.global\
&&!--o.active){o\
.event.trigger(\x22\
ajaxStop\x22)}}retu\
rn J},handleErro\
r:function(F,H,E\
,G){if(F.error){\
F.error(H,E,G)}i\
f(F.global){o.ev\
ent.trigger(\x22aja\
xError\x22,[H,F,G])\
}},active:0,http\
Success:function\
(F){try{return !\
F.status&&locati\
on.protocol==\x22fi\
le:\x22||(F.status>\
=200&&F.status<3\
00)||F.status==3\
04||F.status==12\
23}catch(E){}ret\
urn false},httpN\
otModified:funct\
ion(G,E){try{var\
 H=G.getResponse\
Header(\x22Last-Mod\
ified\x22);return G\
.status==304||H=\
=o.lastModified[\
E]}catch(F){}ret\
urn false},httpD\
ata:function(J,H\
,G){var F=J.getR\
esponseHeader(\x22c\
ontent-type\x22),E=\
H==\x22xml\x22||!H&&F&\
&F.indexOf(\x22xml\x22\
)>=0,I=E?J.respo\
nseXML:J.respons\
eText;if(E&&I.do\
cumentElement.ta\
gName==\x22parserer\
ror\x22){throw\x22pars\
ererror\x22}if(G&&G\
.dataFilter){I=G\
.dataFilter(I,H)\
}if(typeof I===\x22\
string\x22){if(H==\x22\
script\x22){o.globa\
lEval(I)}if(H==\x22\
json\x22){I=l[\x22eval\
\x22](\x22(\x22+I+\x22)\x22)}}r\
eturn I},param:f\
unction(E){var G\
=[];function H(I\
,J){G[G.length]=\
encodeURICompone\
nt(I)+\x22=\x22+encode\
URIComponent(J)}\
if(o.isArray(E)|\
|E.jquery){o.eac\
h(E,function(){H\
(this.name,this.\
value)})}else{fo\
r(var F in E){if\
(o.isArray(E[F])\
){o.each(E[F],fu\
nction(){H(F,thi\
s)})}else{H(F,o.\
isFunction(E[F])\
?E[F]():E[F])}}}\
return G.join(\x22&\
\x22).replace(/%20/\
g,\x22+\x22)}});var m=\
{},n,d=[[\x22height\
\x22,\x22marginTop\x22,\x22m\
arginBottom\x22,\x22pa\
ddingTop\x22,\x22paddi\
ngBottom\x22],[\x22wid\
th\x22,\x22marginLeft\x22\
,\x22marginRight\x22,\x22\
paddingLeft\x22,\x22pa\
ddingRight\x22],[\x22o\
pacity\x22]];functi\
on t(F,E){var G=\
{};o.each(d.conc\
at.apply([],d.sl\
ice(0,E)),functi\
on(){G[this]=F})\
;return G}o.fn.e\
xtend({show:func\
tion(J,L){if(J){\
return this.anim\
ate(t(\x22show\x22,3),\
J,L)}else{for(va\
r H=0,F=this.len\
gth;H<F;H++){var\
 E=o.data(this[H\
],\x22olddisplay\x22);\
this[H].style.di\
splay=E||\x22\x22;if(o\
.css(this[H],\x22di\
splay\x22)===\x22none\x22\
){var G=this[H].\
tagName,K;if(m[G\
]){K=m[G]}else{v\
ar I=o(\x22<\x22+G+\x22 /\
>\x22).appendTo(\x22bo\
dy\x22);K=I.css(\x22di\
splay\x22);if(K===\x22\
none\x22){K=\x22block\x22\
}I.remove();m[G]\
=K}o.data(this[H\
],\x22olddisplay\x22,K\
)}}for(var H=0,F\
=this.length;H<F\
;H++){this[H].st\
yle.display=o.da\
ta(this[H],\x22oldd\
isplay\x22)||\x22\x22}ret\
urn this}},hide:\
function(H,I){if\
(H){return this.\
animate(t(\x22hide\x22\
,3),H,I)}else{fo\
r(var G=0,F=this\
.length;G<F;G++)\
{var E=o.data(th\
is[G],\x22olddispla\
y\x22);if(!E&&E!==\x22\
none\x22){o.data(th\
is[G],\x22olddispla\
y\x22,o.css(this[G]\
,\x22display\x22))}}fo\
r(var G=0,F=this\
.length;G<F;G++)\
{this[G].style.d\
isplay=\x22none\x22}re\
turn this}},_tog\
gle:o.fn.toggle,\
toggle:function(\
G,F){var E=typeo\
f G===\x22boolean\x22;\
return o.isFunct\
ion(G)&&o.isFunc\
tion(F)?this._to\
ggle.apply(this,\
arguments):G==nu\
ll||E?this.each(\
function(){var H\
=E?G:o(this).is(\
\x22:hidden\x22);o(thi\
s)[H?\x22show\x22:\x22hid\
e\x22]()}):this.ani\
mate(t(\x22toggle\x22,\
3),G,F)},fadeTo:\
function(E,G,F){\
return this.anim\
ate({opacity:G},\
E,F)},animate:fu\
nction(I,F,H,G){\
var E=o.speed(F,\
H,G);return this\
[E.queue===false\
?\x22each\x22:\x22queue\x22]\
(function(){var \
K=o.extend({},E)\
,M,L=this.nodeTy\
pe==1&&o(this).i\
s(\x22:hidden\x22),J=t\
his;for(M in I){\
if(I[M]==\x22hide\x22&\
&L||I[M]==\x22show\x22\
&&!L){return K.c\
omplete.call(thi\
s)}if((M==\x22heigh\
t\x22||M==\x22width\x22)&\
&this.style){K.d\
isplay=o.css(thi\
s,\x22display\x22);K.o\
verflow=this.sty\
le.overflow}}if(\
K.overflow!=null\
){this.style.ove\
rflow=\x22hidden\x22}K\
.curAnim=o.exten\
d({},I);o.each(I\
,function(O,S){v\
ar R=new o.fx(J,\
K,O);if(/toggle|\
show|hide/.test(\
S)){R[S==\x22toggle\
\x22?L?\x22show\x22:\x22hide\
\x22:S](I)}else{var\
 Q=S.toString().\
match(/^([+-]=)?\
([\x5cd+-.]+)(.*)$/\
),T=R.cur(true)|\
|0;if(Q){var N=p\
arseFloat(Q[2]),\
P=Q[3]||\x22px\x22;if(\
P!=\x22px\x22){J.style\
[O]=(N||1)+P;T=(\
(N||1)/R.cur(tru\
e))*T;J.style[O]\
=T+P}if(Q[1]){N=\
((Q[1]==\x22-=\x22?-1:\
1)*N)+T}R.custom\
(T,N,P)}else{R.c\
ustom(T,S,\x22\x22)}}}\
);return true})}\
,stop:function(F\
,E){var G=o.time\
rs;if(F){this.qu\
eue([])}this.eac\
h(function(){for\
(var H=G.length-\
1;H>=0;H--){if(G\
[H].elem==this){\
if(E){G[H](true)\
}G.splice(H,1)}}\
});if(!E){this.d\
equeue()}return \
this}});o.each({\
slideDown:t(\x22sho\
w\x22,1),slideUp:t(\
\x22hide\x22,1),slideT\
oggle:t(\x22toggle\x22\
,1),fadeIn:{opac\
ity:\x22show\x22},fade\
Out:{opacity:\x22hi\
de\x22}},function(E\
,F){o.fn[E]=func\
tion(G,H){return\
 this.animate(F,\
G,H)}});o.extend\
({speed:function\
(G,H,F){var E=ty\
peof G===\x22object\
\x22?G:{complete:F|\
|!F&&H||o.isFunc\
tion(G)&&G,durat\
ion:G,easing:F&&\
H||H&&!o.isFunct\
ion(H)&&H};E.dur\
ation=o.fx.off?0\
:typeof E.durati\
on===\x22number\x22?E.\
duration:o.fx.sp\
eeds[E.duration]\
||o.fx.speeds._d\
efault;E.old=E.c\
omplete;E.comple\
te=function(){if\
(E.queue!==false\
){o(this).dequeu\
e()}if(o.isFunct\
ion(E.old)){E.ol\
d.call(this)}};r\
eturn E},easing:\
{linear:function\
(G,H,E,F){return\
 E+F*G},swing:fu\
nction(G,H,E,F){\
return((-Math.co\
s(G*Math.PI)/2)+\
0.5)*F+E}},timer\
s:[],fx:function\
(F,E,G){this.opt\
ions=E;this.elem\
=F;this.prop=G;i\
f(!E.orig){E.ori\
g={}}}});o.fx.pr\
ototype={update:\
function(){if(th\
is.options.step)\
{this.options.st\
ep.call(this.ele\
m,this.now,this)\
}(o.fx.step[this\
.prop]||o.fx.ste\
p._default)(this\
);if((this.prop=\
=\x22height\x22||this.\
prop==\x22width\x22)&&\
this.elem.style)\
{this.elem.style\
.display=\x22block\x22\
}},cur:function(\
F){if(this.elem[\
this.prop]!=null\
&&(!this.elem.st\
yle||this.elem.s\
tyle[this.prop]=\
=null)){return t\
his.elem[this.pr\
op]}var E=parseF\
loat(o.css(this.\
elem,this.prop,F\
));return E&&E>-\
10000?E:parseFlo\
at(o.curCSS(this\
.elem,this.prop)\
)||0},custom:fun\
ction(I,H,G){thi\
s.startTime=e();\
this.start=I;thi\
s.end=H;this.uni\
t=G||this.unit||\
\x22px\x22;this.now=th\
is.start;this.po\
s=this.state=0;v\
ar E=this;functi\
on F(J){return E\
.step(J)}F.elem=\
this.elem;if(F()\
&&o.timers.push(\
F)&&!n){n=setInt\
erval(function()\
{var K=o.timers;\
for(var J=0;J<K.\
length;J++){if(!\
K[J]()){K.splice\
(J--,1)}}if(!K.l\
ength){clearInte\
rval(n);n=g}},13\
)}},show:functio\
n(){this.options\
.orig[this.prop]\
=o.attr(this.ele\
m.style,this.pro\
p);this.options.\
show=true;this.c\
ustom(this.prop=\
=\x22width\x22||this.p\
rop==\x22height\x22?1:\
0,this.cur());o(\
this.elem).show(\
)},hide:function\
(){this.options.\
orig[this.prop]=\
o.attr(this.elem\
.style,this.prop\
);this.options.h\
ide=true;this.cu\
stom(this.cur(),\
0)},step:functio\
n(H){var G=e();i\
f(H||G>=this.opt\
ions.duration+th\
is.startTime){th\
is.now=this.end;\
this.pos=this.st\
ate=1;this.updat\
e();this.options\
.curAnim[this.pr\
op]=true;var E=t\
rue;for(var F in\
 this.options.cu\
rAnim){if(this.o\
ptions.curAnim[F\
]!==true){E=fals\
e}}if(E){if(this\
.options.display\
!=null){this.ele\
m.style.overflow\
=this.options.ov\
erflow;this.elem\
.style.display=t\
his.options.disp\
lay;if(o.css(thi\
s.elem,\x22display\x22\
)==\x22none\x22){this.\
elem.style.displ\
ay=\x22block\x22}}if(t\
his.options.hide\
){o(this.elem).h\
ide()}if(this.op\
tions.hide||this\
.options.show){f\
or(var I in this\
.options.curAnim\
){o.attr(this.el\
em.style,I,this.\
options.orig[I])\
}}this.options.c\
omplete.call(thi\
s.elem)}return f\
alse}else{var J=\
G-this.startTime\
;this.state=J/th\
is.options.durat\
ion;this.pos=o.e\
asing[this.optio\
ns.easing||(o.ea\
sing.swing?\x22swin\
g\x22:\x22linear\x22)](th\
is.state,J,0,1,t\
his.options.dura\
tion);this.now=t\
his.start+((this\
.end-this.start)\
*this.pos);this.\
update()}return \
true}};o.extend(\
o.fx,{speeds:{sl\
ow:600,fast:200,\
_default:400},st\
ep:{opacity:func\
tion(E){o.attr(E\
.elem.style,\x22opa\
city\x22,E.now)},_d\
efault:function(\
E){if(E.elem.sty\
le&&E.elem.style\
[E.prop]!=null){\
E.elem.style[E.p\
rop]=E.now+E.uni\
t}else{E.elem[E.\
prop]=E.now}}}})\
;if(document.doc\
umentElement.get\
BoundingClientRe\
ct){o.fn.offset=\
function(){if(!t\
his[0]){return{t\
op:0,left:0}}if(\
this[0]===this[0\
].ownerDocument.\
body){return o.o\
ffset.bodyOffset\
(this[0])}var G=\
this[0].getBound\
ingClientRect(),\
J=this[0].ownerD\
ocument,F=J.body\
,E=J.documentEle\
ment,L=E.clientT\
op||F.clientTop|\
|0,K=E.clientLef\
t||F.clientLeft|\
|0,I=G.top+(self\
.pageYOffset||o.\
boxModel&&E.scro\
llTop||F.scrollT\
op)-L,H=G.left+(\
self.pageXOffset\
||o.boxModel&&E.\
scrollLeft||F.sc\
rollLeft)-K;retu\
rn{top:I,left:H}\
}}else{o.fn.offs\
et=function(){if\
(!this[0]){retur\
n{top:0,left:0}}\
if(this[0]===thi\
s[0].ownerDocume\
nt.body){return \
o.offset.bodyOff\
set(this[0])}o.o\
ffset.initialize\
d||o.offset.init\
ialize();var J=t\
his[0],G=J.offse\
tParent,F=J,O=J.\
ownerDocument,M,\
H=O.documentElem\
ent,K=O.body,L=O\
.defaultView,E=L\
.getComputedStyl\
e(J,null),N=J.of\
fsetTop,I=J.offs\
etLeft;while((J=\
J.parentNode)&&J\
!==K&&J!==H){M=L\
.getComputedStyl\
e(J,null);N-=J.s\
crollTop,I-=J.sc\
rollLeft;if(J===\
G){N+=J.offsetTo\
p,I+=J.offsetLef\
t;if(o.offset.do\
esNotAddBorder&&\
!(o.offset.doesA\
ddBorderForTable\
AndCells&&/^t(ab\
le|d|h)$/i.test(\
J.tagName))){N+=\
parseInt(M.borde\
rTopWidth,10)||0\
,I+=parseInt(M.b\
orderLeftWidth,1\
0)||0}F=G,G=J.of\
fsetParent}if(o.\
offset.subtracts\
BorderForOverflo\
wNotVisible&&M.o\
verflow!==\x22visib\
le\x22){N+=parseInt\
(M.borderTopWidt\
h,10)||0,I+=pars\
eInt(M.borderLef\
tWidth,10)||0}E=\
M}if(E.position=\
==\x22relative\x22||E.\
position===\x22stat\
ic\x22){N+=K.offset\
Top,I+=K.offsetL\
eft}if(E.positio\
n===\x22fixed\x22){N+=\
Math.max(H.scrol\
lTop,K.scrollTop\
),I+=Math.max(H.\
scrollLeft,K.scr\
ollLeft)}return{\
top:N,left:I}}}o\
.offset={initial\
ize:function(){i\
f(this.initializ\
ed){return}var L\
=document.body,F\
=document.create\
Element(\x22div\x22),H\
,G,N,I,M,E,J=L.s\
tyle.marginTop,K\
='<div style=\x22po\
sition:absolute;\
top:0;left:0;mar\
gin:0;border:5px\
 solid #000;padd\
ing:0;width:1px;\
height:1px;\x22><di\
v></div></div><t\
able style=\x22posi\
tion:absolute;to\
p:0;left:0;margi\
n:0;border:5px s\
olid #000;paddin\
g:0;width:1px;he\
ight:1px;\x22 cellp\
adding=\x220\x22 cells\
pacing=\x220\x22><tr><\
td></td></tr></t\
able>';M={positi\
on:\x22absolute\x22,to\
p:0,left:0,margi\
n:0,border:0,wid\
th:\x221px\x22,height:\
\x221px\x22,visibility\
:\x22hidden\x22};for(E\
 in M){F.style[E\
]=M[E]}F.innerHT\
ML=K;L.insertBef\
ore(F,L.firstChi\
ld);H=F.firstChi\
ld,G=H.firstChil\
d,I=H.nextSiblin\
g.firstChild.fir\
stChild;this.doe\
sNotAddBorder=(G\
.offsetTop!==5);\
this.doesAddBord\
erForTableAndCel\
ls=(I.offsetTop=\
==5);H.style.ove\
rflow=\x22hidden\x22,H\
.style.position=\
\x22relative\x22;this.\
subtractsBorderF\
orOverflowNotVis\
ible=(G.offsetTo\
p===-5);L.style.\
marginTop=\x221px\x22;\
this.doesNotIncl\
udeMarginInBodyO\
ffset=(L.offsetT\
op===0);L.style.\
marginTop=J;L.re\
moveChild(F);thi\
s.initialized=tr\
ue},bodyOffset:f\
unction(E){o.off\
set.initialized|\
|o.offset.initia\
lize();var G=E.o\
ffsetTop,F=E.off\
setLeft;if(o.off\
set.doesNotInclu\
deMarginInBodyOf\
fset){G+=parseIn\
t(o.curCSS(E,\x22ma\
rginTop\x22,true),1\
0)||0,F+=parseIn\
t(o.curCSS(E,\x22ma\
rginLeft\x22,true),\
10)||0}return{to\
p:G,left:F}}};o.\
fn.extend({posit\
ion:function(){v\
ar I=0,H=0,F;if(\
this[0]){var G=t\
his.offsetParent\
(),J=this.offset\
(),E=/^body|html\
$/i.test(G[0].ta\
gName)?{top:0,le\
ft:0}:G.offset()\
;J.top-=j(this,\x22\
marginTop\x22);J.le\
ft-=j(this,\x22marg\
inLeft\x22);E.top+=\
j(G,\x22borderTopWi\
dth\x22);E.left+=j(\
G,\x22borderLeftWid\
th\x22);F={top:J.to\
p-E.top,left:J.l\
eft-E.left}}retu\
rn F},offsetPare\
nt:function(){va\
r E=this[0].offs\
etParent||docume\
nt.body;while(E&\
&(!/^body|html$/\
i.test(E.tagName\
)&&o.css(E,\x22posi\
tion\x22)==\x22static\x22\
)){E=E.offsetPar\
ent}return o(E)}\
});o.each([\x22Left\
\x22,\x22Top\x22],functio\
n(F,E){var G=\x22sc\
roll\x22+E;o.fn[G]=\
function(H){if(!\
this[0]){return \
null}return H!==\
g?this.each(func\
tion(){this==l||\
this==document?l\
.scrollTo(!F?H:o\
(l).scrollLeft()\
,F?H:o(l).scroll\
Top()):this[G]=H\
}):this[0]==l||t\
his[0]==document\
?self[F?\x22pageYOf\
fset\x22:\x22pageXOffs\
et\x22]||o.boxModel\
&&document.docum\
entElement[G]||d\
ocument.body[G]:\
this[0][G]}});o.\
each([\x22Height\x22,\x22\
Width\x22],function\
(I,G){var E=I?\x22L\
eft\x22:\x22Top\x22,H=I?\x22\
Right\x22:\x22Bottom\x22,\
F=G.toLowerCase(\
);o.fn[\x22inner\x22+G\
]=function(){ret\
urn this[0]?o.cs\
s(this[0],F,fals\
e,\x22padding\x22):nul\
l};o.fn[\x22outer\x22+\
G]=function(K){r\
eturn this[0]?o.\
css(this[0],F,fa\
lse,K?\x22margin\x22:\x22\
border\x22):null};v\
ar J=G.toLowerCa\
se();o.fn[J]=fun\
ction(K){return \
this[0]==l?docum\
ent.compatMode==\
\x22CSS1Compat\x22&&do\
cument.documentE\
lement[\x22client\x22+\
G]||document.bod\
y[\x22client\x22+G]:th\
is[0]==document?\
Math.max(documen\
t.documentElemen\
t[\x22client\x22+G],do\
cument.body[\x22scr\
oll\x22+G],document\
.documentElement\
[\x22scroll\x22+G],doc\
ument.body[\x22offs\
et\x22+G],document.\
documentElement[\
\x22offset\x22+G]):K==\
=g?(this.length?\
o.css(this[0],J)\
:null):this.css(\
J,typeof K===\x22st\
ring\x22?K:K+\x22px\x22)}\
})})();\
"

qt_resource_name = b"\
\x00\x0d\
\x06+\x87\xd3\
\x00j\
\x00q\x00u\x00e\x00r\x00y\x00.\x00m\x00i\x00n\x00.\x00j\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8a\x12\xb9R6\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
