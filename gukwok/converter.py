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


class euccn_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(euccn_processor, self).__init__('euccn')
        self.encoder_name = 'euccn'

    def euccn(self, request):
        abort(400)

    def eucjp(self, request):
        return kageul.euccn.eucjp(request)

    def euckr(self, request):
        return kageul.euccn.euckr(request)

    def jis(self, request):
        return kageul.euccn.jis(request)

    def sjis(self, request):
        return kageul.euccn.sjis(request)

    def utf8(self, request):
        return kageul.euccn.utf8(request)


class eucjp_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(eucjp_processor, self).__init__('eucjp')
        self.encoder_name = 'eucjp'

    def euccn(self, request):
        return kageul.eucjp.euccn(request)

    def eucjp(self, request):
        abort(400)

    def euckr(self, request):
        return kageul.eucjp.euckr(request)

    def jis(self, request):
        return kageul.eucjp.jis(request)

    def sjis(self, request):
        return kageul.eucjp.sjis(request)

    def utf8(self, request):
        return kageul.eucjp.utf8(request)


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


class jis_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(jis_processor, self).__init__('jis')
        self.encoder_name = 'jis'

    def euccn(self, request):
        return kageul.jis.euccn(request)

    def eucjp(self, request):
        return kageul.jis.eucjp(request)

    def euckr(self, request):
        return kageul.jis.euckr(request)

    def jis(self, request):
        abort(400)

    def sjis(self, request):
        return kageul.jis.sjis(request)

    def utf8(self, request):
        return kageul.jis.utf8(request)


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


class utf8_processor(char_processor):
    def __init__(self):
        """

        :param encoder_name:
        """
        super(utf8_processor, self).__init__('utf8')
        self.encoder_name = 'utf8'

    def euccn(self, request):
        return kageul.utf8.euccn(request)

    def eucjp(self, request):
        return kageul.utf8.eucjp(request)

    def euckr(self, request):
        return kageul.utf8.euckr(request)

    def jis(self, request):
        return kageul.utf8.jis(request)

    def sjis(self, request):
        return kageul.utf8.sjis(request)

    def utf8(self, request):
        abort(400)
