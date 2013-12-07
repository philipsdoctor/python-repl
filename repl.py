import ast

while True:
    s = raw_input(">>> ")    
    print ast.parse(s)

#    isstatement= False
#    try:
#        code = compile(s, '<stdin>', 'eval')
#    except SyntaxError:
#        isstatement = True
#        code = compile(s, '<stdin>', 'exec')

    try:
        print eval(s) or ""
    except SyntaxError:
    	exec s
#    if isstatement:
#        exec s
#    else:
#        print eval(s) or ""


