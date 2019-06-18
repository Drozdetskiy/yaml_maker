import yaml


class YamlSerializer(yaml.YAMLObject):
    yaml_tag = u'!Request'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (str, int)):
                setattr(self, key, value)

    @property
    def data(self):
        return yaml.dump(self)

    def __str__(self):
        return yaml.dump(self)

    def represent(self):
        return self.__str__()
