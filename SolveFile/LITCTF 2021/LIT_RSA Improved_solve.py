from Crypto.Util.number import*

n = 10588750243470683238253385410274703579658358849388292003988652883382013203466393057371661939626562904071765474423122767301289214711332944602077015274586262780328721640431549232327069314664449442016399
e = 65537
ct = 5995952936037255929781924635247478684210608634033130708312547257115162490907542249878843535087479397093661825467058312432783733583919194527896596274111265902276347768535338414466405501311805051241244

phi = 10588750167918674960883789143045660643158993347687045875869450214066147676028772573481938133525034199329131417297302524527283825948454308111292333014318829278789943716483882085733933207158521856000000
d = pow(e,-1,phi)
print(long_to_bytes(pow(ct,d,n)))
