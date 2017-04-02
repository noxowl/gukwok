from flask import abort
from hannakageul import convert as kageul

__all__ = ('codec')

def codec(source, target, request):
    processor = char_processor.get_encoder(source)
    return processor.decode_to(target, request)

class char_processor(object):
    encoders = None

    def __init__(self, encoder_name):
        """

        :param encoder_name:
        """
        self.encoder_name = encoder_name


    def decode_to(self, arg, request):
        method = getattr(self, arg, lambda: "nothing")
        return method(request)


    def euccn(self, request):
        pass


    def eucjp(self, request):
        pass


    def euckr(self, request):
        pass


    def jis(self, request):
        pass


    def sjis(self, request):
        pass


    def utf8(self, request):
        pass


    @classmethod
    def get_encoder(self, encoder_name):
        if self.encoders is None:
            self.encoders = {}
            for encoder_class in self.__subclasses__():
                encoder = encoder_class()
                self.encoders[encoder.encoder_name] = encoder
        return self.encoders[encoder_name]


class euckr_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(euckr_processor, self).__init__('euckr')
        self.encoder_name = 'euckr'


    def euccn(self, request):
        return kageul.euckr.euccn(request)


    def eucjp(self, request):
        return kageul.euckr.eucjp(request)


    def euckr(self, request):
        abort(400)


    def jis(self, request):
        return kageul.euckr.jis(request)


    def sjis(self, request):
        return kageul.euckr.sjis(request)


    def utf8(self, request):
        return kageul.euckr.utf8(request)

class sjis_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(sjis_processor, self).__init__('sjis')
        self.encoder_name = 'sjis'


    def euccn(self, request):
        return kageul.sjis.euccn(request)


    def eucjp(self, request):
        return kageul.sjis.eucjp(request)


    def euckr(self, request):
        return kageul.sjis.euckr(request)


    def jis(self, request):
        return kageul.sjis.jis(request)


    def sjis(self, request):
        abort(400)


    def utf8(self, request):
        return kageul.sjis.utf8(request)


