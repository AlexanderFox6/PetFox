
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMATH_OPleftCOMPARISON_OPleftLOGICAL_OPASSIGN ASSIGN_OP BITWISE_OP BOOLEAN BREAK CHAR COMPARISON_OP CONTINUE ELIF ELSE END FLOAT IDENTIFIER KEYWORD LCURLY LOGICAL_OP LPAREN MATH_OP NEWLINE NUMBER RCURLY RPAREN STRING\n    statement : assignment_statement\n              | if_statement\n              | while_statement\n              | expression_statement\n              | BREAK\n              | CONTINUE\n    assignment_statement : IDENTIFIER ASSIGN expression NEWLINE\n    if_statement : if_clause NEWLINE statement_list END\n                 | if_clause NEWLINE statement_list ELIF NEWLINE statement_list END\n                 | if_clause NEWLINE statement_list ELIF NEWLINE statement_list NEWLINE ELSE NEWLINE statement_list END\n    while_statement : while_clause NEWLINE statement_list END\n    if_clause : KEYWORD expression\n              | KEYWORD expression LCURLY NEWLINE statement_list RCURLY\n    \n    statement_list : statement\n                   | statement_list NEWLINE statement\n    while_clause : KEYWORD expressionexpression_statement : expression NEWLINEexpression : LPAREN expression RPAREN\n    expression : expression MATH_OP expression\n               | expression COMPARISON_OP expression\n               | expression LOGICAL_OP expression\n    expression : literal\n    literal : NUMBER\n            | FLOAT\n            | BOOLEAN\n            | CHAR\n            | IDENTIFIER\n            | STRING\n    '
    
_lr_action_items = {'BREAK':([0,25,26,40,44,46,50,53,],[6,6,6,6,6,6,6,6,]),'CONTINUE':([0,25,26,40,44,46,50,53,],[7,7,7,7,7,7,7,7,]),'IDENTIFIER':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[8,28,28,28,28,28,28,8,8,8,8,8,8,8,]),'KEYWORD':([0,25,26,40,44,46,50,53,],[12,12,12,12,12,12,12,12,]),'LPAREN':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'NUMBER':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'FLOAT':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'BOOLEAN':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'CHAR':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'STRING':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'$end':([1,2,3,4,5,6,7,21,39,41,43,51,55,],[0,-1,-2,-3,-4,-5,-6,-17,-7,-8,-11,-9,-10,]),'END':([2,3,4,5,6,7,21,34,35,36,39,41,43,45,48,51,54,55,],[-1,-2,-3,-4,-5,-6,-17,41,-14,43,-7,-8,-11,-15,51,-9,55,-10,]),'ELIF':([2,3,4,5,6,7,21,34,35,39,41,43,45,51,55,],[-1,-2,-3,-4,-5,-6,-17,42,-14,-7,-8,-11,-15,-9,-10,]),'NEWLINE':([2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,19,21,27,28,30,31,32,33,34,35,36,37,38,39,41,42,43,45,47,48,49,51,52,54,55,],[-1,-2,-3,-4,-5,-6,-27,21,25,26,-22,-23,-24,-25,-26,-28,-17,-12,-27,39,-19,-20,-21,40,-14,40,44,-18,-7,-8,46,-11,-15,40,50,-13,-9,53,40,-10,]),'RCURLY':([2,3,4,5,6,7,21,35,39,41,43,45,47,51,55,],[-1,-2,-3,-4,-5,-6,-17,-14,-7,-8,-11,-15,49,-9,-10,]),'ASSIGN':([8,],[20,]),'MATH_OP':([8,9,14,15,16,17,18,19,27,28,29,30,31,32,33,38,],[-27,22,-22,-23,-24,-25,-26,-28,22,-27,22,22,-19,-20,-21,-18,]),'COMPARISON_OP':([8,9,14,15,16,17,18,19,27,28,29,30,31,32,33,38,],[-27,23,-22,-23,-24,-25,-26,-28,23,-27,23,23,23,-20,-21,-18,]),'LOGICAL_OP':([8,9,14,15,16,17,18,19,27,28,29,30,31,32,33,38,],[-27,24,-22,-23,-24,-25,-26,-28,24,-27,24,24,24,24,-21,-18,]),'LCURLY':([14,15,16,17,18,19,27,28,31,32,33,38,],[-22,-23,-24,-25,-26,-28,37,-27,-19,-20,-21,-18,]),'RPAREN':([14,15,16,17,18,19,28,29,31,32,33,38,],[-22,-23,-24,-25,-26,-28,-27,38,-19,-20,-21,-18,]),'ELSE':([50,],[52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,25,26,40,44,46,50,53,],[1,35,35,45,35,35,45,35,]),'assignment_statement':([0,25,26,40,44,46,50,53,],[2,2,2,2,2,2,2,2,]),'if_statement':([0,25,26,40,44,46,50,53,],[3,3,3,3,3,3,3,3,]),'while_statement':([0,25,26,40,44,46,50,53,],[4,4,4,4,4,4,4,4,]),'expression_statement':([0,25,26,40,44,46,50,53,],[5,5,5,5,5,5,5,5,]),'expression':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[9,27,29,30,31,32,33,9,9,9,9,9,9,9,]),'if_clause':([0,25,26,40,44,46,50,53,],[10,10,10,10,10,10,10,10,]),'while_clause':([0,25,26,40,44,46,50,53,],[11,11,11,11,11,11,11,11,]),'literal':([0,12,13,20,22,23,24,25,26,40,44,46,50,53,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'statement_list':([25,26,44,46,53,],[34,36,47,48,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assignment_statement','statement',1,'p_statement','lexer.py',123),
  ('statement -> if_statement','statement',1,'p_statement','lexer.py',124),
  ('statement -> while_statement','statement',1,'p_statement','lexer.py',125),
  ('statement -> expression_statement','statement',1,'p_statement','lexer.py',126),
  ('statement -> BREAK','statement',1,'p_statement','lexer.py',127),
  ('statement -> CONTINUE','statement',1,'p_statement','lexer.py',128),
  ('assignment_statement -> IDENTIFIER ASSIGN expression NEWLINE','assignment_statement',4,'p_assignment_statement','lexer.py',134),
  ('if_statement -> if_clause NEWLINE statement_list END','if_statement',4,'p_if_statement','lexer.py',140),
  ('if_statement -> if_clause NEWLINE statement_list ELIF NEWLINE statement_list END','if_statement',7,'p_if_statement','lexer.py',141),
  ('if_statement -> if_clause NEWLINE statement_list ELIF NEWLINE statement_list NEWLINE ELSE NEWLINE statement_list END','if_statement',11,'p_if_statement','lexer.py',142),
  ('while_statement -> while_clause NEWLINE statement_list END','while_statement',4,'p_while_statement','lexer.py',152),
  ('if_clause -> KEYWORD expression','if_clause',2,'p_if_clause','lexer.py',158),
  ('if_clause -> KEYWORD expression LCURLY NEWLINE statement_list RCURLY','if_clause',6,'p_if_clause','lexer.py',159),
  ('statement_list -> statement','statement_list',1,'p_statement_list','lexer.py',169),
  ('statement_list -> statement_list NEWLINE statement','statement_list',3,'p_statement_list','lexer.py',170),
  ('while_clause -> KEYWORD expression','while_clause',2,'p_while_clause','lexer.py',184),
  ('expression_statement -> expression NEWLINE','expression_statement',2,'p_expression_statement','lexer.py',189),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_grouped','lexer.py',194),
  ('expression -> expression MATH_OP expression','expression',3,'p_expression_binop','lexer.py',200),
  ('expression -> expression COMPARISON_OP expression','expression',3,'p_expression_binop','lexer.py',201),
  ('expression -> expression LOGICAL_OP expression','expression',3,'p_expression_binop','lexer.py',202),
  ('expression -> literal','expression',1,'p_expression_literal','lexer.py',208),
  ('literal -> NUMBER','literal',1,'p_literal','lexer.py',214),
  ('literal -> FLOAT','literal',1,'p_literal','lexer.py',215),
  ('literal -> BOOLEAN','literal',1,'p_literal','lexer.py',216),
  ('literal -> CHAR','literal',1,'p_literal','lexer.py',217),
  ('literal -> IDENTIFIER','literal',1,'p_literal','lexer.py',218),
  ('literal -> STRING','literal',1,'p_literal','lexer.py',219),
]
