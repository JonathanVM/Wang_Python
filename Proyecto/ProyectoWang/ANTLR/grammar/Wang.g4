/*
@author loriacarlos@gmail.com
@since II-2018
*/
grammar Wang;

assertion: formula ('.' formula)*EOF
;

formula:  premises ('=>'  conclusions)? #FormExpr
   
;
premises : sequence
;
conclusions : sequence
;
sequence: listexpr?           
;
listexpr: expr (',' expr)*   # SeqExpr
;

expr:   '~' expr              # NotExpr
    |   expr op='&' expr      # AndExpr
    |   expr op='|' expr      # OrExpr
	|   expr op='<->' expr    # BiconditionalExpr
    | <assoc=right>  
      expr op='->' expr       # ImplyExpr
    |   ID                    # Id
    |   '(' expr ')'          # Parens

;
COMMA : ','
;
DOT : '.'
;
LEADSTO : '=>'
;
NOT : '~'
;
AND : '&' 
; 
OR :  '|' 
;
BICONDITIONAL : '<->'
;
IMPLIES: '->'
;
ID  :   [a-z][a-z0-9_]* 
;      
WS  :   [\r\n\t ]+ -> skip
;
ErrorChar : .
;