

class yearConverter:
    regex=r'[0-9]{4}'
    def to_python(selfself,value):
        return int(value)
    def to_url(selfself,value):
        return "%04d"