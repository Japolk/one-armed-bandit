my_paytable = {('JP', 'JP', 'JP'):                  2000,
               ('7','7', '7'):                      330,
               ('3bar', '3bar', '3bar'):            120,
               ('2bar', '2bar', '2bar'):            60,
               ('bar', 'bar', 'bar'):               30,
               ('any_bar', 'any_bar', 'any_bar'):   16,
               ('cherry', 'cherry', 'cherry'):      16,
               ('cherry', 'cherry', 'any'):         8,
               ('cherry', 'any', 'any'):            4,
               }


my_reel_1 = {range(1,73+1):     'blank',
             range(74,78+1):    'cherry',
             range(79,94+1):    'bar',
             range(95,107+1):   '2bar',
             range(108,118+1):  '3bar',
             range(119,126+1):  '7',
             range(127,128+1):  'JP',
             }

my_reel_2 = {range(1,73+1):     'blank',
             range(74,78+1):    'cherry',
             range(79,94+1):    'bar',
             range(95,107+1):   '2bar',
             range(108,118+1):  '3bar',
             range(119,126+1):  '7',
             range(127,128+1):  'JP',
             }
my_reel_3 = {range(1,73+1):     'blank',
             range(74,78+1):    'cherry',
             range(79,94+1):    'bar',
             range(95,107+1):   '2bar',
             range(108,118+1):  '3bar',
             range(119,126+1):  '7',
             range(127,128+1):  'JP',
             }
my_virtual_stops = 128

my_symbols_to_unicode = {'blank':  ' ',
                      'cherry': u'\U0001F352',
                      'bar':    '―',
                      '2bar':   '=',
                      '3bar':   '☰',
                      '7':      '7',
                      'JP':     u'\U0001F4B0',
                   }