from ast import *
def adump(node, annotate_fields=True, include_attributes=False):
    """
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.  If annotate_fields is true (by default),
    the returned string will show the names and the values for fields.
    If annotate_fields is false, the result string will be more compact by
    omitting unambiguous field names.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    include_attributes can be set to true.
    """
    def _format(node):
        if isinstance(node, AST):
            args = []
            keywords = annotate_fields
            for field in node._fields:
                try:
                    value = getattr(node, field)
                except AttributeError:
                    keywords = True
                else:
                    if keywords:
                        args.append('%s=%s' % (field, _format(value)))
                    else:
                        args.append(_format(value))
            if include_attributes and node._attributes:
                for a in node._attributes:
                    try:
                        args.append('%s=%s' % (a, _format(getattr(node, a))))
                    except AttributeError:
                        pass
            return 'ast.%s(%s)' % (node.__class__.__name__, ', '.join(args))
        elif isinstance(node, list):
            return '[%s]' % ', '.join(_format(x) for x in node)
        return repr(node)
    if not isinstance(node, AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)
    return _format(node)
