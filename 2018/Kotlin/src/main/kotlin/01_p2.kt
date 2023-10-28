import java.io.BufferedReader
import java.io.File
import java.io.FileReader
import java.io.IOException
import java.util.*

fun main() {
    val inputs = "src/main/inputs/"
    var frequency = 0

    frequency = readFrequency(inputs + "01-frequency_changes-t2.txt", true)
    println("rez t2: $frequency")

    frequency = readFrequency(inputs + "01-frequency_changes-p1.txt", true)
    println("rez p1: $frequency")
}

private fun readFrequency(it: String, isDebug: Boolean = false): Int {
    val file = File(it)

    var cumSum = 0
    var iter = 1
    val seen = mutableSetOf<Int>()

    try {
        while(true) {
            val sc = Scanner(File(it))

            while (sc.hasNextLine()) {
                cumSum += Integer.parseInt(sc.nextLine())
                if (seen.contains(cumSum)) {
                    if (isDebug)
                        println("seen");

                    return cumSum;
                }
                seen.add(cumSum)
            }

            if (isDebug)
                iter += 1
                println("loop $iter");
        }
    } catch (e: IOException) {
        e.printStackTrace()
    }

    return cumSum
}
