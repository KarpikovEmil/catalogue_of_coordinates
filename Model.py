from qgis.core import *


class PoligonZU:

    def __init__(self, idPoligon, status, coordinatesPoligon, coordinatesHole):
        self.id = idPoligon
        self.status = status
        self.coordinatesPoligon = coordinatesPoligon
        self.coordinatesHole = coordinatesHole


class PointValue:

    def __init__(self, idPoint, coordinates):
        self.id = idPoint
        self.coordinates = coordinates


class Model:

    allPoligons = []
    allPoints = []
    
    j = 1

    def findSimilarPoint(poligonZU, pointsList, coordinatesType):
        for point in pointsList:
            pointValue = PointValue(Model.j, point)
            for pointIter in Model.allPoints:
                if pointValue.coordinates == pointIter.coordinates:
                    pointValue.id = pointIter.id
                    Model.j -= 1
                    break
            Model.allPoints.append(pointValue)
            coordinatesType.append(pointValue)
            Model.j += 1

    def numeration(layer):

        layerFeat = layer.getFeatures()

        for obj in layerFeat:

            # Создание объекта класса PoligonZU
            idPoligon = obj.attribute("id")
            statusPoligon = obj.attribute("status")
            coordinatesPoligon = []
            coordinatesHole = []
            poligonZU = PoligonZU(idPoligon, statusPoligon,
                                  coordinatesPoligon, coordinatesHole)

            # Получаем геомертию объекта как геометрию мульти полигона
            asMuPL = obj.geometry().asMultiPolygon()
            poligonList = asMuPL[0]

            i = 1
            for pointsList in poligonList:
                if i == 1:
                    coordinatesType = poligonZU.coordinatesPoligon
                    print("Печать коорд полигона")
                else:
                    coordinatesType = poligonZU.coordinatesHole
                    print("Печать коорд дырки")
                Model.findSimilarPoint(poligonZU, pointsList, coordinatesType)
                print("Конец печати полигона")
                i += 1

            Model.allPoligons.append(poligonZU)

        Model.allPoligons.sort(key=lambda poligon: poligon.id)
        for poligonZU in Model.allPoligons:
            print(poligonZU.id)
            print(poligonZU.status)
            for point in poligonZU.coordinatesPoligon:
                print(point.id, point.coordinates)
            for point in poligonZU.coordinatesHole:
                print(point.id, point.coordinates)
