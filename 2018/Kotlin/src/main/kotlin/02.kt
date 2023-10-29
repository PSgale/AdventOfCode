import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException

fun main() {
    val inputs = "src/main/inputs/"
    var checksum = 0

    checksum = getChecksum(inputs + "02-box_ids-t1.txt")
    println("rez: $checksum")

    checksum = getChecksum(inputs + "02-box_ids-p1.txt")
    println("rez: $checksum")
}

private fun getChecksum(it: String, isDebug: Boolean = false): Int {
    val file = File(it)

    var cumSum2 = 0
    var cumSum3 = 0

    try {
        BufferedReader(FileReader(file)).use { br ->
            br.lines().forEach { line ->

                var is2 = 0
                var is3 = 0

                val charArray = line.toCharArray()
                val charMap = charArray.groupBy { it }

                charMap.forEach { entry ->
                    if ((entry.value).size == 2)
                        is2 = 1
                    else if ((entry.value).size == 3)
                        is3 = 1
                }

                cumSum2 += is2
                cumSum3 += is3
            }
        }
    } catch (e: IOException) {
        e.printStackTrace()
    }

    return cumSum2 * cumSum3
}