# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2011 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
The special characters tool.
"""

from __future__ import unicode_literals

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QKeySequence

import panels


class CharMap(panels.Panel):
    def __init__(self, mainwindow):
        super(CharMap, self).__init__(mainwindow)
        self.hide()
        self.toggleViewAction().setShortcut(QKeySequence("Meta+Alt+T"))
        mainwindow.addDockWidget(Qt.LeftDockWidgetArea, self)

    def translateUI(self):
        self.setWindowTitle(_("Special Characters"))
        self.toggleViewAction().setText(_("Special Charac&ters"))
        
    def createWidget(self):
        from . import widget
        return widget.Widget(self)

