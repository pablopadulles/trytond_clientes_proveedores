from stdnum import get_cc_module
import stdnum.exceptions
from sql import Null, Column, Literal
from sql.functions import CharLength, Substring, Position
from sql.operators import Equal

from trytond.i18n import gettext
from trytond.model import (ModelView, ModelSQL, MultiValueMixin, ValueMixin,
    DeactivableMixin, fields, Unique, sequence_ordered, Exclude)

from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pyson import Eval, Bool, Not
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from trytond import backend
from trytond.tools.multivalue import migrate_property
from trytond.tools import lstrip_wildcard
from datetime import datetime, timedelta
import random

class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    cliente = fields.Boolean('Cliente')
    proveedor = fields.Boolean('Proveedor')

    def get_random_telefono(self):
        lista = []
        for contact in self.contact_mechanisms:
            if contact.type == 'mobile':
                lista.append(contact)
        if lista:
            res = lista.pop(random.randint(0, len(lista) - 1))
            return res.value
        return None
