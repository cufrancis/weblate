# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2014 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db.models import Q
from weblate.trans.management.commands import WeblateLangCommand


class Command(WeblateLangCommand):
    help = 'fixes flags for units'

    def handle(self, *args, **options):
        units = self.get_units(*args, **options).filter(
            Q(has_suggestion=True) |
            Q(has_comment=True) |
            Q(has_failing_check=True)
        )
        for unit in units.iterator():
            if unit.has_suggestion:
                unit.update_has_suggestion()
            if unit.has_comment:
                unit.update_has_comment()
            if unit.has_failing_check:
                unit.update_has_failing_check()