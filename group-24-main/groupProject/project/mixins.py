from ._compat import PY2, text_type

class UserMixin(object):
    if not PY2:
        __hash__ = object.__hash__

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
            try:
                return text_type(self.id)
            except AttributeError:
                raise NotImplementedError('No `id` attribute - override `get_id`')