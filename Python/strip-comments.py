''' 
4 kyu
Strip Comments
Link: https://www.codewars.com/kata/51c8e37cee245da6b40000bd
'''

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
