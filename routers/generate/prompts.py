PROMPT = '''

    Your Task is to convert the following pseudocode into python and execute it to show the result


'''

PSEUDOEXAMPLE = '''


Data(NextFree) = new Item
 
IF NextFree = 1 THEN
        NextFree = NextFree + 1
        EXIT PROCEDURE
END IF
 
ptr=Start
WHILE ptr <> 0
        IF NewItem < Data(ptr) THEN
                Next(NextFree) = ptr
                IF ptr = Start THEN
                       Start = NextFree
                ELSE
                       Next(prevPtr) = NextFree
                END IF
                EXIT WHILE
        ELSE
                prevPtr = ptr
                ptr = Next(ptr)
        END IF
END WHILE
 
IF ptr = 0 THEN
       Next(prevPtr) = NextFree
END IF
NextFree = NextFree + 1



'''