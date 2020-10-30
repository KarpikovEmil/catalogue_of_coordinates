        idPoligon = obj.attribute("id")
        statusPoligon = obj.attribute("status")
        points = []

        poligon = PoligonZU(idPoligon, statusPoligon, points)

        geometry = obj.geometry()

        asMuPL = geometry.asMultiPolygon()

        print (asMuPL)
        print (type(asMuPL))
        point = asMuPL[0][0][0]

        print (type(point))

        testPoint = QgsPointXY(
            2281056.58972023613750935, 426858.89793546800501645)

        print (point.compare(testPoint))
        
        print (poligon)