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

    var totalDistance = 32
    var winningArea = getWinningArea(inputs + "06-places_coordinates-t1.txt", totalDistance, true)
    println("This area has a total size of ${mk.math.sum(winningArea)}.")

    totalDistance = 10000
    winningArea = getWinningArea(inputs + "06-places_coordinates-p1.txt", totalDistance)
    println("This area has a total size of ${mk.math.sum(winningArea)}.")
}

private fun getWinningArea(fileName: String, totalDistance : Int, isDebug: Boolean = false): D2Array<Int> {
    val lines = readFileLines(fileName)
    val points = getPoints(lines)
    if (isDebug)
        println(points)

    // To identify area Manhattan distance is used
    val closestTo = identifyAreas(points, totalDistance)
    if (isDebug)
        println(closestTo)

    return closestTo
}

private fun identifyAreas(points: MutableList<Point>, totalDistance: Int): D2Array<Int> {
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
        // Mark desired area
        if (distances.sum() < totalDistance) closestTo[i, j] = 1
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
