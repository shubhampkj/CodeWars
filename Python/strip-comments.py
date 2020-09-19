''' 
4 kyu
Strip Comments
Link: https://www.codewars.com/kata/51c8e37cee245da6b40000bd
'''

######################
# Aman's Approach #
######################

import re

def solution(string,markers):
    
    if '^' in markers or '-' in markers:
        try:
            markers.insert(markers.index("^"), '\\')
            markers.insert(markers.index("-"), '\\')
        except:
            pass

    mark_str = "".join(markers)
    
    if markers != [] and string != '':    
        
        if re.search(fr"\w[{mark_str}].*", string):
            f = re.sub(fr"[{mark_str}].*", '', string)
            return f
        
        elif re.search(fr"\s*[{mark_str}].*", string):
            f = re.sub(fr".?[{mark_str}].*", '', string)
            return f
        
        else:
            return string
            
    elif string == "":
        return ""
    
    else:
        return string


######################
# Shubham's Approach #
######################

import re
regexSymbols = ["*", "+", ".", "?", "\\", "^", "[", "]", "|", "&", "-"]
def escapeSpecial(str):
    if str in regexSymbols:
        return "\\"+str
    else:
        return str

def solution(string,markers):
    if len(markers) == 0:
        return string
    markerRegex = r"\s*[" + "".join(map(escapeSpecial, markers)) + "]\s*"
    return "\n".join([re.split(markerRegex, line)[0] for line in re.split(r"\n", string)])
