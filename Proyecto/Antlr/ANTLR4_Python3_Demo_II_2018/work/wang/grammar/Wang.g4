/*
@author loriacarlos@gmail.com
@since II-2018
*/
grammar Wang;

assertion: formula ('.' formula)*EOF
;

formula:  sequence ('=>'  sequence)? #FormExpr
   
;
sequence: listexpr?           
;
listexpr: expr (',' expr)*   # SeqExpr
;

expr:   '~' expr              # NotExpr
    |   expr op='&' expr      # AndExpr
    |   expr op='|' expr      # OrExpr
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
IMPLIES: '->'
;
ID  :   [a-z][a-z0-9_]* 
;      
WS  :   [\r\n\t ]+ -> skip
;
ErrorChar : .
;