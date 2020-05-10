#high score

score = [5,6,8,10,1,3,7]
ordem = list(sorted(score, reverse=True))

print("*"*15, "The highest score is:" , max(ordem),"*"*15)

print()

print("1st -",ordem[0:1],)
print("2nd -", ordem[1:2],)
print("3nd -", ordem[2:3],)

print()
print("the last add score:", score[-1] )
