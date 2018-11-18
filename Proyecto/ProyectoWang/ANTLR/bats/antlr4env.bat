@echo off
set GRAMMAR_NAME=Wang.g4 
set SOURCE=.\src
SET GRAMMAR_PATH=.\grammar
set GRAMMAR=%GRAMMAR_PATH%\%GRAMMAR_NAME%
set PARSER=.\parser

REM loriacarlos@gmail.com
echo *** Setting Environment and Variables for ANTLR4-Python ***
SET ANTLR_JAR=C:\antlr\lib\antlr-4.7.1-complete.jar
SET CLASSPATH=%ANTLR_JAR%;.;%CLASSPATH%
SET PYTHONPATH=%PARSER%\grammar;%SOURCE%;%PYTHONPATH%
REM Antlr4 the tool
doskey antlr4=java -cp %CLASSPATH% org.antlr.v4.Tool $*
REM antlr4 generator for python3 yielding visitor 
set JAVA_CMD=java -cp %CLASSPATH% org.antlr.v4.Tool -Dlanguage=Python3 
set JAVA_CMD_VISITOR=%JAVA_CMD% -no-listener -visitor -o parser $*
doskey antlr4p3=%JAVA_CMD_VISITOR% 
doskey build_parser=%JAVA_CMD_VISITOR% -o %PARSER% %GRAMMAR%
echo VARIABLES
echo *** grammar_path=%GRAMMAR% ***
echo *** parser_path=%PARSER% ***
echo *** classpath=%classpath% ***
echo *** pythonpath=%pythonpath% ***
echo COMMANDS
echo *** Use 'antlr4' for calling directly to antlr4
echo *** Use 'antlr4p3' for generating parsers for python3 target ***
echo *** Use 'build_parser' for generating parser from %grammar% into %PARSER% ***



