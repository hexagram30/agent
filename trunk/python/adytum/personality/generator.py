def clean_name(string):
    return string

class BasePerson(object):
    
    def __init__(self, param_dict={}):
        for key, val in param_dict.items():
            setattr(self, key, val)

        self.__type = {}
       
    def setType(self, key, value):
        if key == 'myersbriggs':
            from adytum.personality.myersbriggs import checkTemperament
            value = checkTemperament(value)
        else:
            raise "PersonalityError: unknown type '%s'." % key
        self.__type.update({key:value})

    def getType(self, key):
        return self.__type[key]

    def getCompatibility(self, compat_type, value):
        compat_type = clean_name(compat_type)
        if not self.getType(compat_type):
            raise "PersonalityError: type '%s' not set." % compat_type
        if compat_type == 'myersbriggs':
            from adytum.personality.myersbriggs import getCompatibilityScale
            return getCompatibilityScale(self.getType(compat_type), value)
        elif compat_type == 'complete':
            pass
        else:
            raise "PersonalityError: unknown compatibility type '%s'." % compat_type
