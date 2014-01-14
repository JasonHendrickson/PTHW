# Calculate the gross pay for one week of work
x = float(raw_input("Enter total hours worked:  "))  # x = total hours for the week
h = float(raw_input("Enter total hours of Hazard Pay:  ")) # h = hours of H pay for the week
p = float(raw_input("Enter hourly pay rate:  "))   # p = Pay per hour

# b = 0 #Base hours pay
# o = 0 #Overtime pay
t = 0 #Total pay
f = 0 #final pay, total pay + hazard
#for x in range(0,40):
#	t = x * p
#for x in range(40, 168):
b = p * 40 #calculates pay for base 40 hours
o = ((x-40) * p * 1.5) #calculates pay for overtime hours
a = h * p * .25 #calculates hazard pay
#Final pay
f = b + o + a # calculates total pay
print 'Your base pay is ' + str(b)
print 'Your overtime pay is ' + str(o)
print 'Your hazardous duty pay is ' + str(a)
print 'Your net income is ' + str(f) 
	