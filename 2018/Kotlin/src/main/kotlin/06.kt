import org.jetbrains.kotlinx.multik.api.mk
import org.jetbrains.kotlinx.multik.api.zeros
import kotlin.math.abs
import org.jetbrains.kotlinx.multik.ndarray.data.D2Array
import org.jetbrains.kotlinx.multik.ndarray.data.get
import org.jetbrains.kotlinx.multik.ndarray.data.set
import org.jetbrains.kotlinx.multik.ndarray.operations.groupNDArrayBy
import kotlin.reflect.KProperty1


fun main() {
    val inputs = "src/main/inputs/"

    val (maxArea, winningPoint) = getWinningPoint(inputs + "06-places_coordinates-t1.txt", true)
    println("${winningPoint.id} wins with an area of $maxArea")

    val (maxArea2, winningPoint2) = getWinningPoint(inputs + "06-places_coordinates-p1.txt")
    println("${winningPoint2.id} wins with an area of $maxArea2")
}

private fun getWinningPoint(fileName: String, isDebug: Boolean = false): Pair<Int, Point> {
    val lines = readFileLines(fileName)
    val points = getPoints(lines)
    if (isDebug)
        println(points)

    // To calculate area Manhattan distance is used
    val closestTo = calculateAreas(points)
    if (isDebug)
        println(closestTo)

    // Any point areas touching the borders will expand into infinity, so these need to be excluded
    val uniquesFiltered = removeBorderAreas(closestTo, points)
    val uniquesFilteredIDs = uniquesFiltered.listOfField(Point::id)

    val countByUnique = closestTo.groupNDArrayBy{it}.toSortedMap().filter{ map -> map.key in uniquesFilteredIDs }.maxBy{ it.value.size }
    val maxArea = countByUnique.value.size
    val winningPoint = points.filter{ p -> p.id == countByUnique.key }.first

    return Pair(maxArea, winningPoint)
}

private fun removeBorderAreas(closestTo: D2Array<Int>, points: MutableList<Point>): List<Point> {
    val maxRow = closestTo.shape[0] - 1
    val maxCol = closestTo.shape[1] - 1

    val onBorderTop = closestTo[0].groupNDArrayBy{ it }.keys.toSet()
    val onBorderBottom = closestTo[maxRow].groupNDArrayBy{ it }.keys.toSet()
    val onBorderLeft = closestTo[0..maxRow, 0].groupNDArrayBy{ it }.keys.toSet()
    val onBorderRight = closestTo[0..maxRow, maxCol].groupNDArrayBy{ it }.keys.toSet()

    val onBorder = onBorderTop + onBorderBottom + onBorderLeft + onBorderRight

    return points.filter { it.id !in onBorder }
}
private fun calculateAreas(points: MutableList<Point>): D2Array<Int> {
    /*
    Set up a 2D matrix of the area spanned by the points.
    For each element of the matrix, store the id of the point it's closest to if it is unique.
    */
    val xMin = points.minBy { it.x }.x
    val xMax = points.maxBy { it.x }.x
    val yMin = points.minBy { it.y }.y
    val yMax = points.maxBy { it.y }.y

    val rows = xMax - xMin + 1
    val cols = yMax - yMin + 1

    val closestTo = mk.zeros<Int>(rows, cols)
    for ((i, j) in closestTo.multiIndices) {
        val distances = points.map { it.distanceTo(xMin + i, yMin + j) }
        val minDistances = distances.sorted().groupBy{it}.minBy { it.key }
        val numOccurrences = minDistances.value.size
        if (numOccurrences == 1) {
            val closestPoint = points[distances.indexOf(minDistances.key)]
            if (closestPoint in points) closestTo[i, j] = closestPoint.id
        }
    }
    return closestTo
}

private fun getPoints(lines: MutableList<String>): MutableList<Point> {
    val points = mutableListOf<Point>()
    for ((i, line) in lines.iterator().withIndex()) {
        val xy = line.split(", ")
        val p = Point(i + 1, xy[0].toInt(), xy[1].toInt())
        points.add(p)
    }
    return points
}

data class Point(val id: Int, val x: Int, val y: Int) {
    fun slope(p2: Point): Double {
        return if (p2.x != x) (p2.y - y).toDouble() / (p2.x - x) else Double.MAX_VALUE
    }

    fun distanceTo(x0: Int, y0: Int): Int {
        // Manhattan distance
        return abs(x - x0) + abs(y - y0)
    }
}

inline fun <reified T, Y> List<T>.listOfField(property: KProperty1<T, Y?>):List<Y> {
    val yy = ArrayList<Y>()
    this.forEach { t: T ->
        yy.add(property.get(t) as Y)
    }
    return yy
}