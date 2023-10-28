import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException

fun main() {
    val inputs = "src/main/inputs/"
    var frequency = 0

    frequency = readFrequency(inputs + "01-frequency_changes-t1.txt")
    println("rez: $frequency")

    frequency = readFrequency(inputs + "01-frequency_changes-p1.txt")
    println("rez: $frequency")
}

private fun readFrequency(it: String, isDebug: Boolean = false): Int {
    val file = File(it)

    var cumSum = 0
    val seen = mutableSetOf<Int>()

    try {
        BufferedReader(FileReader(file)).use { br ->
            br.lines().forEach lit@{
                cumSum += Integer.parseInt(it)
            }
        }

    } catch (e: IOException) {
        e.printStackTrace()
    }

    return cumSum
}
