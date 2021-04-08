

class LandVersionConverter:

    def to_python(self, value):
        if value == 'test':
            return value
        elif value == 'origin':
            return value

    def to_url(self, value):
        return value
