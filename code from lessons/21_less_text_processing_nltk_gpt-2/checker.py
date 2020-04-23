import language_check


tool = language_check.LanguageTool('ru-RU')

sent = 'Вы наверняка видели десятки других курсов по программированию на Питоне в ' \
       'интернете. А кто-то из вас возможно пробовал проходить их, но так и не закончил, ' \
       'потому что очень сложно изучать что-то, что не применяется на практике.'


matches = tool.check(sent)

print(matches)

breakpoint()