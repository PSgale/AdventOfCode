fun main() {
    val inputs = "src/main/inputs/"
    var polymer:String

    polymer = getReducedPolymer(inputs + "05-long_polymer-t1.txt", true)
    println("Fully reacted polymer length is ${polymer.length}")

    polymer = getReducedPolymer(inputs + "05-long_polymer-p1.txt")
    println("Fully reacted polymer length is ${polymer.length}")
}

private fun getReducedPolymer(fileName: String, isDebug: Boolean = false): String {
    val lines = readFileLines(fileName)
    var line = lines[0]

    if (isDebug)
        println("Provided polymer: $line")

    var cursor = 0
    while(cursor < line.length - 1){
        val v1 = line[cursor]
        val v2 = line[cursor+1]
        if ((v1.lowercase() == v2.lowercase()) and (v1 != v2))
        {
            val units = line.substring(cursor..cursor+1)
            line = line.removeRange(cursor, cursor+2)

            if (isDebug)
                println("Polymer: $line after adjacent units destroyed: $units")

            cursor = if (cursor > 0) cursor - 1 else 0
        }
        else
        {
            cursor += 1
        }
    }

    return line
}