from qgis.core import *


class PoligonZU:

    def __init__(self, idPoligon, status, pointsPoligon, pointsHole):
        self.id = idPoligon
        self.status = status
        self.pointsPoligon = pointsPoligon
        self.pointsHole = pointsHole


class PointValue:

    def __init__(self, idPoint, coordinates):
        self.id = idPoint
        self.coordinates = coordinates


class Model:

    def numeration(layer):

        allPoligons = []
        allPoints = []
        i = 1
        j = 1
        layerFeat = layer.getFeatures()
        for obj in layerFeat:

            idPoligon = obj.attribute("id")
            statusPoligon = obj.attribute("status")
            pointsPoligon = []
            pointsHole = []

            poligon = PoligonZU(idPoligon, statusPoligon,
                                pointsPoligon, pointsHole)

            geometry = obj.geometry()

            asMuPL = geometry.asMultiPolygon()

            poligonList = asMuPL[0]

            for pointsList in poligonList:

                for point in pointsList:
                    pointValue = PointValue(j, point)
                    for pointIter in allPoints:
                        if pointValue.coordinates == pointIter.coordinates:
                            pointValue.id = pointIter.id
                            break
                    allPoints.append(pointValue)
                    poligon.pointsPoligon.append(pointValue)
                    j += 1

                    print (point)
                print ("Конец печати полигона")

            count = len(poligonList)
            print (allPoints)

            print ("Список точек:", type(poligonList))
            print ("Количество списков:", count, type(count))

            allPoligons.append(poligon)

        for poligon in allPoligons:
            for point in poligon.pointsPoligon:
                print (point.id, point.coordinates)

