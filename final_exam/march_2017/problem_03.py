trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num_int = int(us_num)

    if 0 <= us_num_int <= 10:
        return trans[us_num]
    elif 11 <= us_num_int <= 19:
        return '{} {}'.format(trans['10'], trans[us_num[-1]])
    elif us_num_int % 10 == 0:
        return '{} {}'.format(trans[us_num[0]], trans['10'])
    else:
        return '{} {} {}'.format(
            trans[us_num[0]], trans['10'], trans[us_num[-1]])
