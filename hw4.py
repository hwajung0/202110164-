def rep_char(c,n):
    print(c*n)
def draw_line_string(m):
    msg1='Hello {m}'
    msg2='Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr+2)
    print(f' Hello {m},')
    print(' Welcome to Seoul.')
    rep_char('-',nstr+2)
    

msg=input('Input his/her name:')
draw_line_string(msg)
