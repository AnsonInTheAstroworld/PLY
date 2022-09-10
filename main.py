import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

def p_expression_plus(p):
    '''expression : expression '+' expression'''
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    '''expression : expression '-' expression'''
    p[0] = p[1] - p[3]

def p_term_times(p):
    '''expression : expression '*' expression'''
    p[0] = p[1] * p[3]

def p_term_div(p):
    '''expression : expression '/' expression'''
    p[0] = p[1] / p[3]

def p_term_mod(p):
   '''expression : expression '%' expression'''
   p[0] = p[1] % p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_float(p):
    "expression : FLOAT"
    p[0] = p[1]

def p_expression_int(p):
    "expression : INT"
    p[0] = p[1]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

