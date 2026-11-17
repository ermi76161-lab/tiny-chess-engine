import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
T=[[5*(ord(c)-75)for c in s]for s in("KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKK","ACEECGKLELMNEKNOELNOEKMNCGKKACEE","GIIIILKKIMMMIKMMILLMIKLMIKKKGIII","KKKLJKKKJKKKJKKKJKKKJKKKLMMMKKKK")]
NO=(14,18,31,33,-14,-18,-31,-33)
KO=(1,15,16,17,-1,-15,-16,-17)
BD=(15,17,-15,-17)
RD=(1,-1,16,-16)
J=(0,0,NO,BD,RD,BD+RD,KO)
CA=((1,4,6,7),(2,4,2,0),(4,116,118,119),(8,116,114,112))
E={0:2,7:1,112:8,119:4}
B=[0]*128
S=0;C=0;Y=0;K=[0,0];W=[];N=[0];H=set()
M=25*10**4
L="abcdefgh"
class X(Exception):pass
def v(p,s):
 t=abs(p)
 if p<0:s^=112
 r=s>>4;f=s&7
 z=V[t]+T[min(t-1,3)][r*4+min(f,7-f)]if t<6 else 0
 return z if p>0 else -z
def Q():
 return(tuple(B),S)
def A(s,y):
 w=1-2*y
 for o in(15,17):
  t=s+o*(2*y-1)
  if not t&136 and B[t]==w:return 1
 for t in(2,3,4,6):
  for o in J[t]:
   q=s+o
   while not q&136:
    z=B[q]
    if z:
     if z*w>0 and(abs(z)==t or t>2 and abs(z)==5):return 1
     break
    if t in(2,6):break
    q+=o
 return 0
def g(c):
 m=[];D=1-2*S
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or p*D<0:continue
  t=abs(p)
  if t==1:
   d=16-32*S;r7=7-7*S
   for f in(-1,0,1):
    o=s+d+f
    if o&136:continue
    q=B[o]
    if f and q and q*D<0 or not f and not q and not c:
     m+=[s|o<<7|5<<14,s|o<<7|2<<14]if(o>>4)==r7 else[s|o<<7]
     if not f and(s>>4)==1+5*S and not B[s+2*d]:m.append(s|(s+2*d)<<7)
  else:
   for o in J[t]:
    q=s+o
    while not q&136:
     z=B[q]
     if z:
      if z*D<0:m.append(s|q<<7)
      break
     if not c:m.append(s|q<<7)
     if t==2 or t==6:break
     q+=o
   if t==6 and not c:
    for x,k,j,r in CA[S*2:S*2+2]:
     if C&x and B[r]==4*D:
      d=1 if j>k else -1
      if not B[k+d]and not B[j]and(d>0 or not B[j-1])and not A(k,1-S)and not A(k+d,1-S)and not A(j,1-S):m.append(k|j<<7)
 return m
def k(m):
 global S,C,Y
 f=m&127;t=(m>>7)&127;r=(m>>14)&7
 p=B[f];q=B[t]
 W.append((m,p,q,C,Y,S))
 Y-=v(p,f)
 if q:Y-=v(q,t)
 B[f]=0
 p=r*p if r else p
 B[t]=p;Y+=v(p,t)
 if abs(p)==6:
  K[S]=t;C&=~(3<<(2*S))
  if abs(t-f)==2:
   a=f+3 if t>f else f-4;D=f+1 if t>f else f-1
   z=B[a];B[a]=0;B[D]=z;Y-=v(z,a);Y+=v(z,D)
 C&=~E.get(f,0);C&=~E.get(t,0)
 S^=1
def n():
 global S,C,Y
 m,p,q,C,Y,S=W.pop()
 f=m&127;t=(m>>7)&127
 if abs(p)==6:
  K[S]=f
  if abs(t-f)==2:B[f+1 if t>f else f-1]=0;B[f+3 if t>f else f-4]=4 if S==0 else -4
 B[f]=p;B[t]=q
def F(f):
 global S,C,Y
 B[:]=[0]*128;Y=0
 x=f.split();r=7;y=0
 for ch in x[0]:
  if ch=='/':r-=1;y=0
  elif ch.isdigit():y+=int(ch)
  else:
   z="PNBRQK".index(ch.upper())+1;q=z if ch.isupper() else -z;B[r*16+y]=q;Y+=v(q,r*16+y)
   if z==6:K[0 if q>0 else 1]=r*16+y
   y+=1
 S=x[1]=='b';C=0
 for i,z in enumerate("KQkq"):
  C|=(z in x[2])<<i
 W.clear()
def w(m):
 f=(ord(m[0])-97)|((int(m[1])-1)<<4);t=(ord(m[2])-97)|((int(m[3])-1)<<4)
 return f|t<<7|("  nbrq".index(m[4])if m[4:]else 0)<<14
def o(m):
 f=m&127;t=(m>>7)&127;r=(m>>14)&7
 return L[f&7]+str((f>>4)+1)+L[t&7]+str((t>>4)+1)+"  nbrq"[r].strip()
def O(m):
 t=(m>>7)&127;z=B[t]
 return(10**5+10*V[abs(z)])if z else 0
def s(a,b,d,y):
 N[0]+=1
 if N[0]>M:raise X
 q=d<=0
 if q:
  z=Y if S==0 else -Y
  if z>=b:return b
  if z>a:a=z
 c=A(K[S],1-S)
 z=g(0 if not q or c else 1)
 z.sort(key=O,reverse=True)
 B2=-M;l=0
 for m in z:
  k(m)
  if A(K[1-S],S):n();continue
  l+=1
  z2=-s(-b,-a,d-1,y+1)
  n()
  B2=max(B2,z2);a=max(a,z2)
  if a>=b:break
 if not l and(not q or c):return-M+y if c else 0
 return a if q else B2
def R(L):
 z=[w(m)for m in L]
 z.sort(key=O,reverse=True)
 b=z[0];N[0]=0
 for d in range(1,65):
  try:
   A2=-M;C2=0
   for m in z:
    k(m);x=-s(-M,M,d-1,1)
    if Q()in H:x=min(x,0)
    n()
    if x>A2:A2=x;C2=m
   b=C2
  except X:break
 return o(b)
def P(p,b):
 return json.load(u.urlopen(U+p,json.dumps(b).encode()))
while 1:
 z=P("/game",{})
 if z["status"]=="done":break
 while z["status"]=="your_move":
  F("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq");H.clear();H.add(Q())
  for mv in z["moves"]:
   k(w(mv));H.add(Q())
  F(z["fen"])
  z=P("/move",{"game":z["game"],"move":R(z["legal_moves"])})
