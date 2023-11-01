fun main() {
    val inputs = "src/main/inputs/"
    var polymer:String

    polymer = getAdjustedPolymer(inputs + "05-long_polymer-t1.txt", true)
    println("Fully reacted adjusted polymer length is ${polymer.length}")

    polymer = getAdjustedPolymer(inputs + "05-long_polymer-p1.txt")
    println("Fully reacted adjusted polymer length is ${polymer.length}")
}

private fun getAdjustedPolymer(fileName: String, isDebug: Boolean = false): String{
    val lines = readFileLines(fileName)
    val polymer = lines[0]

    var smallPolymer = ""
    var smallPolymerLength = polymer.length
    val uniqueChars = polymer.toCharArray().map{ c -> c.lowercase() }.toSet()

    for(charToRemove in uniqueChars)
    {
        val adjustedPolymer = polymer.filter { c -> c.lowercase() != charToRemove }
        val reducedPolymer = getReducedPolymer(adjustedPolymer)

        if (isDebug)
            println("Reduced polymer length '${reducedPolymer.length}' after char '$charToRemove' get removed")

        if (smallPolymerLength > reducedPolymer.length) {
            smallPolymer = reducedPolymer
            smallPolymerLength = smallPolymer.length
        }
    }

    return smallPolymer
}
private fun getReducedPolymer(polymer: String, isDebug: Boolean = false): String {
    var line = polymer

    var i = 0
    while(i < line.length - 1){
        val v1 = line[i]
        val v2 = line[i+1]
        if ((v1.lowercase() == v2.lowercase()) and (v1 != v2))
        {
            val units = line.substring(i..i+1)
            line = line.removeRange(i, i+2)

            if (isDebug)
                println("Polymer: $line after adjacent units destroyed: $units")

            i = if (i > 0) i - 1 else 0
        }
        else
        {
            i += 1
        }
    }

    return line
}