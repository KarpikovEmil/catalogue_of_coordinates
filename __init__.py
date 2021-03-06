# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CatalogueOfCoordinates
                                 A QGIS plugin
 Catalogue Of Coordinates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-10-16
        copyright            : (C) 2020 by EmilKarpikov
        email                : karpikovemil2013@yandex.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CatalogueOfCoordinates class from file CatalogueOfCoordinates.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    import sys, os
    sys.path.insert(0, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), ''))+'//env//Lib//site-packages')
    from .catalogue_of_coordinates import CatalogueOfCoordinates
    return CatalogueOfCoordinates(iface)
