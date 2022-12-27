
l=12
b=36
#top part
for a in range(1,l,2):
   print((".|."*a).center(b,"-"))
#middle part
print("WELCOME".center(b,"-"))
#bottom part
for a in reversed(range(1,l,2)):
   print((".|."*a).center(b,"-"))