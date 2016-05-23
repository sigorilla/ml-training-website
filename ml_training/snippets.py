import re

from django.core.urlresolvers import LocaleRegexURLResolver
from django.utils import translation
from ml_training import settings


class NoPrefixLocaleRegexURLResolver(LocaleRegexURLResolver):
    """
    Source: https://gist.github.com/cauethenorio/4948177
    """

    @property
    def regex(self):
        language_code = translation.get_language()

        if language_code not in self._regex_dict:
            regex_compiled = (re.compile('', re.UNICODE)
                              if language_code == settings.LANGUAGE_CODE
                              else re.compile('^%s/' % language_code, re.UNICODE))

            self._regex_dict[language_code] = regex_compiled
        return self._regex_dict[language_code]


def simple_i18n_patterns(prefix, *args):
    """
    Adds the language code prefix to every URL pattern within this
    function, when the language not is the main language.
    This may only be used in the root URLconf, not in an included URLconf.
    """
    pattern_list = [prefix] + list(args)
    if not settings.USE_I18N:
        return pattern_list
    return [NoPrefixLocaleRegexURLResolver(pattern_list)]
