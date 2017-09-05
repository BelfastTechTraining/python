import re
string = 'The quick brown fox jumps over the laxy dog.'

print('search:      {0}'.format(re.search('The quick brown fox', string)))
print('search_gr0:  {0}'.format(re.search('The quick brown fox', string).group(0)))

print('match:       {0}'.format(re.match('quick (brown) fox', string)))
print('match_gr0:   {0}'.format(re.match('\S* quick (brown) fox', string).group(0)))
print('match_gr1:   {0}'.format(re.match('\S* quick (brown) fox', string).group(1)))

regex = re.compile('^[\S\s]*(over) (the)[\s\S]*')
print('compiled_match_gr0:  {0}'.format(regex.match(string).group(0)))
print('compiled_match_gr1:  {0}'.format(regex.match(string).group(1)))
print('compiled_match_gr2:  {0}'.format(regex.match(string).group(2)))
