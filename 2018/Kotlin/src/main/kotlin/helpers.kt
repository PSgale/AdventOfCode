import java.io.BufferedReader
import java.io.File
import java.io.FileReader

fun readFileLines(fileName: String): MutableList<String> {
    val lineList = mutableListOf<String>()

    val file = File(fileName)
    BufferedReader(FileReader(file)).use { br ->
        br.lines().forEach { lineList.add(it) }
    }
    return lineList
}