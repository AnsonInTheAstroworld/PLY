
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightUMINUSFLOAT INTexpression : expression '+' expressionexpression : expression '-' expressionexpression : expression '*' expressionexpression : expression '/' expressionexpression : expression '%' expressionexpression : '-' expression %prec UMINUSexpression : FLOATexpression : INTexpression : '(' expression ')'"
    
_lr_action_items = {'-':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[2,7,2,-7,-8,2,2,2,2,2,2,-6,7,-1,-2,-3,-4,7,-9,]),'FLOAT':([0,2,5,6,7,8,9,10,],[3,3,3,3,3,3,3,3,]),'INT':([0,2,5,6,7,8,9,10,],[4,4,4,4,4,4,4,4,]),'(':([0,2,5,6,7,8,9,10,],[5,5,5,5,5,5,5,5,]),'$end':([1,3,4,11,13,14,15,16,17,18,],[0,-7,-8,-6,-1,-2,-3,-4,-5,-9,]),'+':([1,3,4,11,12,13,14,15,16,17,18,],[6,-7,-8,-6,6,-1,-2,-3,-4,6,-9,]),'*':([1,3,4,11,12,13,14,15,16,17,18,],[8,-7,-8,-6,8,8,8,-3,-4,8,-9,]),'/':([1,3,4,11,12,13,14,15,16,17,18,],[9,-7,-8,-6,9,9,9,-3,-4,9,-9,]),'%':([1,3,4,11,12,13,14,15,16,17,18,],[10,-7,-8,-6,10,-1,-2,-3,-4,10,-9,]),')':([3,4,11,12,13,14,15,16,17,18,],[-7,-8,-6,18,-1,-2,-3,-4,-5,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,5,6,7,8,9,10,],[1,11,12,13,14,15,16,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression + expression','expression',3,'p_expression_plus','main.py',11),
  ('expression -> expression - expression','expression',3,'p_expression_minus','main.py',15),
  ('expression -> expression * expression','expression',3,'p_term_times','main.py',19),
  ('expression -> expression / expression','expression',3,'p_term_div','main.py',23),
  ('expression -> expression % expression','expression',3,'p_term_mod','main.py',27),
  ('expression -> - expression','expression',2,'p_expression_uminus','main.py',31),
  ('expression -> FLOAT','expression',1,'p_expression_float','main.py',35),
  ('expression -> INT','expression',1,'p_expression_int','main.py',39),
  ('expression -> ( expression )','expression',3,'p_expression_group','main.py',43),
]
