import re

#
# sxz-->es

# h-->es(aeioudgkprt+h)
# y-->ies(aeiou+h)
# default --> s



#Way 1
def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'



rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

# Way 2
patterns = \
    (
        ('[sxz]$', '$', 'es'),
        ('[^aeioudgkprt]h$', '$', 'es'),
        ('(qu|[^aeiou])y$', 'y$', 'ies'),
        ('$', '$', 's')
    )


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

rules2 = (build_match_and_apply_functions(pattern, search, replace) for (pattern, search,replace) in patterns)


def plural2(noun):
    for matches_rule,apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':

    # way 1
    a = 'phone'
    print(plural(a))

    # way 2

    b = 'watch'
    print(plural(b))