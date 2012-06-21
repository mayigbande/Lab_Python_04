groceries=['bananas','strawberries','apples','bread']
groceries.append('champagne')
for i in range(len(groceries)):
    print groceries[i]
print "........................."
groceries.remove('bread')
for i in groceries:
    print i
print "........................."
store={'apple':'a','strawberries':'s','bags':'b','rings':'r'}
print store['apple']
print ".........................."
store_prices={'Apple':'7.3','Bananas':'5.5','Bread':'1.0','Carrots':'10.0','Champagne':'20.90',
              'Strawberries':'32.6'}
print store_prices['Apple']
store_prices['Strawberries']='63.43'
print store_prices['Strawberries']
store_prices['Chicken']='6.5'
print store_prices['Chicken']
print '.........................'
in_stock=['Apple','Bananas','Bread','Carrots','Champagne','Strawberries']
always_in_stock=('Apple','Bananas','Bread','Carrots','Champagne','Strawberries')
print 'Come to shoprite! We always sell:'
for i in always_in_stock:
    print i
print "......................."
