fun ordena (a:real,b:real,c:real) = if a < b andalso a < c then
if b < c then [a,b,c] else [a,c,b] 
else 
if b < a andalso b < c then 
if a < c then [b,a,c] else [b,c,a]
else if c<a
andalso c<b then if a<b then [c,a,b] else [c,b,a] else [a,b,c];
