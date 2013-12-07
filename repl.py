import ast
import traceback

repl_scope = {}

while True:
    s = raw_input(">>> ")
    parse_s = None
    
    try:
        parse_s = ast.parse(s)
    except Exception, error:
        print traceback.format_exc()
        continue

    is_exec = False
    for i in ast.walk(parse_s):
        if type(i) == ast.Exec:
            print "No Exec Allowed!"
            is_exec = True
            break
    
    if is_exec:
    	continue

    try:
        try:
            print eval(s, repl_scope) or ""
        except SyntaxError:
            exec s in repl_scope
    except Exception, error:
        print traceback.format_exc()


