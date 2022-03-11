gender = 'm'

match gender:
case 'm':
        print ('Dear mister,')
case 'f':
        print ('Dear madame,')
case _: # the underscore character is used as a catch-all.
        print ('Dear you,')