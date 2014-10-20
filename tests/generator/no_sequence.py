import xcffib
import struct
import six
_events = {}
_errors = {}
class KeymapNotifyEvent(xcffib.Event):
    def __init__(self, unpacker):
        xcffib.Event.__init__(self, unpacker)
        base = unpacker.offset
        unpacker.unpack("x")
        self.keys = xcffib.List(unpacker, "B", 31)
        self.bufsize = unpacker.offset - base
    def pack(self):
        buf = six.BytesIO()
        buf.write(struct.pack("=B", 11))
        buf.write(xcffib.pack_list(self.keys, "B"))
        return buf.getvalue()
_events[11] = KeymapNotifyEvent
xcffib._add_ext(key, no_sequenceExtension, _events, _errors)
