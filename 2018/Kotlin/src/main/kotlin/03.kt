// #1 @ 1,3: 4x4
private val REGEX = Regex("@\\s(\\d+),(\\d+):\\s(\\d+)x(\\d+)\$")

fun main() {
    val inputs = "src/main/inputs/"
    var claimedInches_g1 = 0

    claimedInches_g1 = getClaimedInchesG1(inputs + "03-claimed_inches-t1.txt", true)
    println("rez: $claimedInches_g1")

    claimedInches_g1 = getClaimedInchesG1(inputs + "03-claimed_inches-p1.txt")
    println("rez: $claimedInches_g1")
}

private fun getClaimedInchesG1(it: String, isDebug: Boolean = false): Int {
    val lines = readFileLines(it)

    // fabric[i][j] = how many times this inch was claimed
    val fabric: Array<Array<Int>> = Array(1000) { Array(1000) { 0 } }

    for (line in lines) {
        val (offsetLeft, offsetTop, width, height) = parseLine(line)

        if (isDebug)
            println("Parsed: offsetLeft = $offsetLeft, offsetTop = $offsetTop, width = $width, height = $height")

        for (i in offsetLeft until offsetLeft + width) {
            for (j in offsetTop until  offsetTop + height) {
                fabric[i][j] += 1
            }
        }
    }

    var total = 0
    // calculate inches claimed more than once.
    for (i in 0 until 1000) {
        for (j in 0 until 1000) {
            if (fabric[i][j] > 1) {total += 1}
        }
    }

    return total
}

private fun parseLine(line: String): IntArray {
    val matchResult = REGEX.find(line)!!
    val (offsetLeft, offsetTop, width, height) = matchResult.destructured
    return intArrayOf(offsetLeft.toInt(), offsetTop.toInt(), width.toInt(), height.toInt())
}